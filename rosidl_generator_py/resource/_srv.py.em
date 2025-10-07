@# Included from rosidl_generator_py/resource/_idl.py.em
@{
from rosidl_pycommon import convert_camel_case_to_lower_case_underscore

service_name = '_' + convert_camel_case_to_lower_case_underscore(service.namespaced_type.name)
module_name = '_' + convert_camel_case_to_lower_case_underscore(interface_path.stem)

type_annotations_import_statements.add(f'from {".".join(service.namespaced_type.namespaces)} import {service.request_message.structure.namespaced_type.name}')
type_annotations_import_statements.add(f'from {".".join(service.namespaced_type.namespaces)} import {service.response_message.structure.namespaced_type.name}')

TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=service.request_message, import_statements=import_statements,
    type_annotations_import_statements=type_annotations_import_statements)
TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=service.response_message, import_statements=import_statements,
    type_annotations_import_statements=type_annotations_import_statements)
TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=service.event_message, import_statements=import_statements,
    type_annotations_import_statements=type_annotations_import_statements)

# Can be removed in rhel10 since TypeAlias will exist in typing
TYPE_ALIAS_IMPORT = 'from typing_extensions import TypeAlias'
}@
@[if TYPE_ALIAS_IMPORT not in type_annotations_import_statements]@


if typing.TYPE_CHECKING:
    @(TYPE_ALIAS_IMPORT)
@[end if]@
@{
type_annotations_import_statements.add(TYPE_ALIAS_IMPORT)
}@


class Metaclass_@(service.namespaced_type.name)(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service '@(service.namespaced_type.name)'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @@classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('@(package_name)')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                '@('.'.join(service.namespaced_type.namespaced_name()))')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__@('__'.join(service.namespaced_type.namespaces[1:]))_@(service_name)

            from @('.'.join(service.namespaced_type.namespaces)) import @(module_name)
            if @(module_name).Metaclass_@(service.request_message.structure.namespaced_type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(service.request_message.structure.namespaced_type.name).__import_type_support__()
            if @(module_name).Metaclass_@(service.response_message.structure.namespaced_type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(service.response_message.structure.namespaced_type.name).__import_type_support__()
            if @(module_name).Metaclass_@(service.event_message.structure.namespaced_type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(service.event_message.structure.namespaced_type.name).__import_type_support__()


class @(service.namespaced_type.name)(rosidl_pycommon.interface_base_classes.BaseService[
    @(service.request_message.structure.namespaced_type.name),
    @(service.response_message.structure.namespaced_type.name)
], metaclass=Metaclass_@(service.namespaced_type.name)):
    Request: TypeAlias = @(service.request_message.structure.namespaced_type.name)
    Response: TypeAlias = @(service.response_message.structure.namespaced_type.name)
    Event: TypeAlias = @(service.event_message.structure.namespaced_type.name)

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')
