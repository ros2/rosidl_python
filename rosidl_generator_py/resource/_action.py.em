@# Included from rosidl_generator_py/resource/_idl.py.em
@{
from rosidl_cmake import convert_camel_case_to_lower_case_underscore

module_name = '_' + convert_camel_case_to_lower_case_underscore(action.structure_type.name)

TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=action.goal_request)
TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=action.result_response)
TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=action.feedback)
TEMPLATE(
    '_srv.py.em',
    package_name=package_name, interface_path=interface_path,
    service=action.goal_service)
TEMPLATE(
    '_srv.py.em',
    package_name=package_name, interface_path=interface_path,
    service=action.result_service)
TEMPLATE(
    '_msg.py.em',
    package_name=package_name, interface_path=interface_path,
    message=action.feedback_message)
}@


class Metaclass_@(action.structure_type.name)(type):
    """Metaclass of action '@(action.structure_type.name)'."""

    _TYPE_SUPPORT = None

    @@classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('@(package_name)')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger('@('.'.join(action.structure_type.namespaces + [action.structure_type.name]))')
            logger.debug(
                'Failed to import needed modules for type support:\n' + traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__@('__'.join(action.structure_type.namespaces[1:]))_@(module_name)

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass.__import_type_support__()

            if @(module_name).Metaclass_@(action.goal_service.structure_type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(action.goal_service.structure_type.name).__import_type_support__()
            if @(module_name).Metaclass_@(action.result_service.structure_type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(action.result_service.structure_type.name).__import_type_support__()
            if @(module_name).Metaclass_@(action.feedback.structure.type.name)._TYPE_SUPPORT is None:
                @(module_name).Metaclass_@(action.feedback.structure.type.name).__import_type_support__()


class @(action.structure_type.name)(metaclass=Metaclass_@(action.structure_type.name)):
    from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
    from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage
    from @('.'.join(action.structure_type.namespaces)).@(module_name) import @(action.goal_service.structure_type.name) as GoalService
    from @('.'.join(action.structure_type.namespaces)).@(module_name) import @(action.result_service.structure_type.name) as ResultService
    from @('.'.join(action.structure_type.namespaces)).@(module_name) import @(action.feedback.structure.type.name) as Feedback

    Goal = GoalService.Request
    Result = ResultService.Response

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
