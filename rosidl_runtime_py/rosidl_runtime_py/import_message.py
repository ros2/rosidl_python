# Copyright 2019 Mikael Arguedas.
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
from typing import Any

from rosidl_parser.definition import NamespacedType


def import_message_from_namespaced_type(message_type: NamespacedType) -> Any:
    module = importlib.import_module(
        '.'.join(message_type.value_type.namespaces))
    return getattr(module, message_type.value_type.name)
