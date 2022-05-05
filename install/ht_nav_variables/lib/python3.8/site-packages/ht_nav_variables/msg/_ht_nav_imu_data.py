# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavImuData.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavImuData(type):
    """Metaclass of message 'HtNavImuData'."""

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
                'ht_nav_variables.msg.HtNavImuData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_imu_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_imu_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_imu_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_imu_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_imu_data

            from ht_nav_variables.msg import HtNavVector3
            if HtNavVector3.__class__._TYPE_SUPPORT is None:
                HtNavVector3.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HtNavImuData(metaclass=Metaclass_HtNavImuData):
    """Message class 'HtNavImuData'."""

    __slots__ = [
        '_time',
        '_vel_diff',
        '_ang_diff',
    ]

    _fields_and_field_types = {
        'time': 'double',
        'vel_diff': 'ht_nav_variables/HtNavVector3',
        'ang_diff': 'ht_nav_variables/HtNavVector3',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavVector3'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavVector3'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.time = kwargs.get('time', float())
        from ht_nav_variables.msg import HtNavVector3
        self.vel_diff = kwargs.get('vel_diff', HtNavVector3())
        from ht_nav_variables.msg import HtNavVector3
        self.ang_diff = kwargs.get('ang_diff', HtNavVector3())

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
        if self.time != other.time:
            return False
        if self.vel_diff != other.vel_diff:
            return False
        if self.ang_diff != other.ang_diff:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def time(self):
        """Message field 'time'."""
        return self._time

    @time.setter
    def time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'time' field must be of type 'float'"
        self._time = value

    @property
    def vel_diff(self):
        """Message field 'vel_diff'."""
        return self._vel_diff

    @vel_diff.setter
    def vel_diff(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavVector3
            assert \
                isinstance(value, HtNavVector3), \
                "The 'vel_diff' field must be a sub message of type 'HtNavVector3'"
        self._vel_diff = value

    @property
    def ang_diff(self):
        """Message field 'ang_diff'."""
        return self._ang_diff

    @ang_diff.setter
    def ang_diff(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavVector3
            assert \
                isinstance(value, HtNavVector3), \
                "The 'ang_diff' field must be a sub message of type 'HtNavVector3'"
        self._ang_diff = value
