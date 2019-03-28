# Copyright 2016-2017 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import array
from collections import OrderedDict
import sys

import numpy
import yaml


def register_yaml_representer():
    # Register our custom representer for YAML output
    yaml.add_representer(OrderedDict, represent_ordereddict)


# Custom representer for getting clean YAML output that preserves the order in
# an OrderedDict.
# Inspired by:
# http://stackoverflow.com/a/16782282/7169408
def represent_ordereddict(dumper, data):
    items = []
    for k, v in data.items():
        items.append((dumper.represent_data(k), dumper.represent_data(v)))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', items)


def msg_to_yaml(args, msg):
    return yaml.dump(
        msg_to_ordereddict(
            msg,
            truncate_length=args.truncate_length if not args.full_length else None
        ), width=sys.maxsize)


def msg_to_csv(args, msg):
    def to_string(val):
        nonlocal args
        r = ''
        if (any(
            isinstance(val, t)
            for t in [list, tuple, array.array, numpy.ndarray]
        )):
            for i, v in enumerate(val):
                if r:
                    r += ','
                if not args.full_length and i >= args.truncate_length:
                    r += '...'
                    break
                r += to_string(v)
        elif (any(
            isinstance(val, t)
            for t in [bool, bytes, float, int, str, numpy.number]
        )):
            if any(isinstance(val, t) for t in [bytes, str]):
                if not args.full_length and len(val) > args.truncate_length:
                    val = val[:args.truncate_length]
                    if isinstance(val, bytes):
                        val += b'...'
                    else:
                        val += '...'
            r = str(val)
        else:
            r = msg_to_csv(args, val)
        return r
    result = ''
    # We rely on __slots__ retaining the order of the fields in the .msg file.
    for field_name in msg.__slots__:
        value = getattr(msg, field_name, None)
        if result:
            result += ','
        result += to_string(value)
    return result


# Convert a msg to an OrderedDict. We do this instead of implementing a generic
# __dict__() method in the msg because we want to preserve order of fields from
# the .msg file(s).
def msg_to_ordereddict(msg, truncate_length=None):
    d = OrderedDict()
    # We rely on __slots__ retaining the order of the fields in the .msg file.
    for field_name in msg.__slots__:
        value = getattr(msg, field_name, None)
        value = _convert_value(value, truncate_length=truncate_length)
        # remove leading underscore from field name
        d[field_name[1:]] = value
    return d


def _convert_value(value, truncate_length=None):
    if isinstance(value, bytes):
        if truncate_length is not None and len(value) > truncate_length:
            value = ''.join([chr(c) for c in value[:truncate_length]]) + '...'
        else:
            value = ''.join([chr(c) for c in value])
    elif isinstance(value, str):
        if truncate_length is not None and len(value) > truncate_length:
            value = value[:truncate_length] + '...'
    elif (any(
        isinstance(value, t) for t in [list, tuple, array.array, numpy.ndarray]
    )):
        # since arrays and ndarrays can't contain mixed types convert to list
        typename = tuple if isinstance(value, tuple) else list
        if truncate_length is not None and len(value) > truncate_length:
            # Truncate the sequence
            value = value[:truncate_length]
            # Truncate every item in the sequence
            value = typename(
                [_convert_value(v, truncate_length) for v in value] + ['...'])
        else:
            # Truncate every item in the list
            value = typename(
                [_convert_value(v, truncate_length) for v in value])
    elif isinstance(value, dict) or isinstance(value, OrderedDict):
        # convert each key and value in the mapping
        new_value = {} if isinstance(value, dict) else OrderedDict()
        for k, v in value.items():
            # don't truncate keys because that could result in key collisions and data loss
            new_value[_convert_value(k)] = _convert_value(v, truncate_length=truncate_length)
        value = new_value
    elif (
        not any(isinstance(value, t) for t in (bool, float, int, numpy.number))
    ):
        # assuming value is a message
        # since it is neither a collection nor a primitive type
        value = msg_to_ordereddict(value, truncate_length=truncate_length)
    return value
