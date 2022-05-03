# Copyright 2022 Open Source Robotics Foundation, Inc.
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

# lint_cmake: -convention/filename, -package/stdargs

if(NumpyHeaders_FOUND)
  return()
endif()
find_package(python_cmake_module REQUIRED)
find_package(PythonExtra MODULE REQUIRED)

find_file(_numpy_h numpy/numpyconfig.h
  PATHS ${PythonExtra_INCLUDE_DIRS}
)

if(APPLE OR WIN32 OR NOT _numpy_h)
  # add include directory for numpy headers
  set(_python_code
    "import numpy"
    "print(numpy.get_include())"
  )
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" "-c" "${_python_code}"
    OUTPUT_VARIABLE _output
    RESULT_VARIABLE _result
    OUTPUT_STRIP_TRAILING_WHITESPACE
  )
  if(NOT _result EQUAL 0)
    message(FATAL_ERROR
      "execute_process(${PYTHON_EXECUTABLE} -c '${_python_code}') returned "
      "error code ${_result}")
  endif()
  message(STATUS "Using numpy include directory: ${_output}")
  set(NumpyHeaders_INCLUDE_DIR ${_output})
else()
  set(NumpyHeaders_INCLUDE_DIR ${PythonExtra_INCLUDE_DIRS})
endif()

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(NumpyHeaders
    REQUIRED_VARS NumpyHeaders_INCLUDE_DIR
)

if(NumpyHeaders_FOUND)
    set(NumpyHeaders_INCLUDE_DIRS ${NumpyHeaders_INCLUDE_DIR})

    add_library(NumpyHeaders::NumpyHeaders INTERFACE IMPORTED)
    set_target_properties(NumpyHeaders::NumpyHeaders PROPERTIES
        INTERFACE_INCLUDE_DIRECTORIES "${NumpyHeaders_INCLUDE_DIR}"
    )
endif()