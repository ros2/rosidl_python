# Copyright 2016 Open Source Robotics Foundation, Inc.
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

import importlib
import os


class UnsupportedTypeSupport(Exception):
    """Raised when typesupport couldn't be imported."""

    def __init__(self, pkg_name):
        message = "Could not import 'rosidl_typesupport_c' for package '{0}'".format(pkg_name)
        super(UnsupportedTypeSupport, self).__init__(message)
        self.pkg_name = pkg_name


def import_type_support(pkg_name):
    """
    Import the rosidl_typesupport_c module of a package.

    The module will provide the C typesupport for the rosidl files in the
    specified package, such that the ROS message structures in the package can
    be converted to and from message structures used by the rmw implementation.

    :param pkg_name str: name of the package
    :returns: the typesupport Python module for the specified package
    """
    module_name = '.{}_s__rosidl_typesupport_c'.format(pkg_name)
    # New in Python 3.8: on Windows we should call 'add_dll_directory()' for directories
    # containing DLLs we depend on.
    # https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew
    dll_dir_handles = []
    if os.name == 'nt' and hasattr(os, 'add_dll_directory'):
        path_env = os.environ['PATH'].split(';')
        for prefix_path in path_env:
            if os.path.exists(prefix_path):
                dll_dir_handles.append(os.add_dll_directory(prefix_path))
    try:
        return importlib.import_module(module_name, package=pkg_name)
    except ImportError:
        raise UnsupportedTypeSupport(pkg_name)
    finally:
        for handle in dll_dir_handles:
            handle.close()
