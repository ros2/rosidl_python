# generated from rosidl_generator_py/resource/_action.py.em
# generated code does not contain a copyright notice

@#######################################################################
@# EmPy template for generating _<action>.py files
@#
@# Context:
@#  - module_name
@#  - package_name
@#  - spec (rosidl_parser.ActionSpecification)
@#    Parsed specification of the .action file
@#  - convert_camel_case_to_lower_case_underscore (function)
@#######################################################################
@
import logging
import traceback


class Metaclass(type):
    """Metaclass of action '@(spec.action_name)'."""

    _TYPE_SUPPORT = None

    @@classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('@(package_name)')
        except ImportError:
            logger = logging.getLogger('rosidl_generator_py.@(spec.action_name)')
            logger.debug(
                'Failed to import needed modules for type support:\n' + traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__@(subfolder)_@(module_name)
@{
preffix = '_' + convert_camel_case_to_lower_case_underscore(spec.action_name) + '__'
suffixes = ['feedback', 'goal', 'result']
for field_name in [preffix + suffix for suffix in suffixes]:
    print('%sfrom %s.%s import %s' % (' ' * 4 * 3, package_name, subfolder, field_name))
    print('%sif %s.Metaclass._TYPE_SUPPORT is None:' % (' ' * 4 * 3, field_name))
    print('%s%s.Metaclass.__import_type_support__()' % (' ' * 4 * 4, field_name))
print('%sfrom %s.%s import %s' % (' ' * 4 * 3, 'action_msgs', 'msg', '_goal_status'))
print('%sif %s.Metaclass._TYPE_SUPPORT is None:' % (' ' * 4 * 3, '_goal_status'))
print('%s%s.Metaclass.__import_type_support__()' % (' ' * 4 * 4, '_goal_status'))
print('%sfrom %s.%s import %s' % (' ' * 4 * 3, 'action_msgs', 'srv', '_cancel_goal'))
print('%sif %s.Metaclass._TYPE_SUPPORT is None:' % (' ' * 4 * 3, '_cancel_goal'))
print('%s%s.Metaclass.__import_type_support__()' % (' ' * 4 * 4, '_cancel_goal'))
}@

class @(spec.action_name)(metaclass=Metaclass):
    from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
    from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage
    from @(package_name).@(subfolder)._@convert_camel_case_to_lower_case_underscore(spec.action_name)__goal import @(spec.action_name)_Goal as GoalRequestService
    from @(package_name).@(subfolder)._@convert_camel_case_to_lower_case_underscore(spec.action_name)__result import @(spec.action_name)_Result as GoalResultService
    from @(package_name).@(subfolder)._@convert_camel_case_to_lower_case_underscore(spec.action_name)__feedback import @(spec.action_name)_Feedback as Feedback

    Goal = GoalRequestService.Request
    Result = GoalResultService.Response

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
