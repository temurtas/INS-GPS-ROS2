# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavJointState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavJointState(type):
    """Metaclass of message 'HtNavJointState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ht_nav_variables')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ht_nav_variables.msg.HtNavJointState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_joint_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_joint_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_joint_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_joint_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_joint_state

            from ht_nav_variables.msg import HtNavWheelVector
            if HtNavWheelVector.__class__._TYPE_SUPPORT is None:
                HtNavWheelVector.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HtNavJointState(metaclass=Metaclass_HtNavJointState):
    """Message class 'HtNavJointState'."""

    __slots__ = [
        '_steering_angle',
        '_wheel_rotation',
    ]

    _fields_and_field_types = {
        'steering_angle': 'ht_nav_variables/HtNavWheelVector',
        'wheel_rotation': 'ht_nav_variables/HtNavWheelVector',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ht_nav_variables.msg import HtNavWheelVector
        self.steering_angle = kwargs.get('steering_angle', HtNavWheelVector())
        from ht_nav_variables.msg import HtNavWheelVector
        self.wheel_rotation = kwargs.get('wheel_rotation', HtNavWheelVector())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.steering_angle != other.steering_angle:
            return False
        if self.wheel_rotation != other.wheel_rotation:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def steering_angle(self):
        """Message field 'steering_angle'."""
        return self._steering_angle

    @steering_angle.setter
    def steering_angle(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'steering_angle' field must be a sub message of type 'HtNavWheelVector'"
        self._steering_angle = value

    @property
    def wheel_rotation(self):
        """Message field 'wheel_rotation'."""
        return self._wheel_rotation

    @wheel_rotation.setter
    def wheel_rotation(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'wheel_rotation' field must be a sub message of type 'HtNavWheelVector'"
        self._wheel_rotation = value
