# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavGpsData.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavGpsData(type):
    """Metaclass of message 'HtNavGpsData'."""

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
                'ht_nav_variables.msg.HtNavGpsData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_gps_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_gps_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_gps_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_gps_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_gps_data

            from ht_nav_variables.msg import HtNavPoint
            if HtNavPoint.__class__._TYPE_SUPPORT is None:
                HtNavPoint.__class__.__import_type_support__()

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


class HtNavGpsData(metaclass=Metaclass_HtNavGpsData):
    """Message class 'HtNavGpsData'."""

    __slots__ = [
        '_gps_pos',
        '_gps_vel',
    ]

    _fields_and_field_types = {
        'gps_pos': 'ht_nav_variables/HtNavPoint',
        'gps_vel': 'ht_nav_variables/HtNavVector3',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavPoint'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavVector3'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ht_nav_variables.msg import HtNavPoint
        self.gps_pos = kwargs.get('gps_pos', HtNavPoint())
        from ht_nav_variables.msg import HtNavVector3
        self.gps_vel = kwargs.get('gps_vel', HtNavVector3())

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
        if self.gps_pos != other.gps_pos:
            return False
        if self.gps_vel != other.gps_vel:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def gps_pos(self):
        """Message field 'gps_pos'."""
        return self._gps_pos

    @gps_pos.setter
    def gps_pos(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavPoint
            assert \
                isinstance(value, HtNavPoint), \
                "The 'gps_pos' field must be a sub message of type 'HtNavPoint'"
        self._gps_pos = value

    @property
    def gps_vel(self):
        """Message field 'gps_vel'."""
        return self._gps_vel

    @gps_vel.setter
    def gps_vel(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavVector3
            assert \
                isinstance(value, HtNavVector3), \
                "The 'gps_vel' field must be a sub message of type 'HtNavVector3'"
        self._gps_vel = value
