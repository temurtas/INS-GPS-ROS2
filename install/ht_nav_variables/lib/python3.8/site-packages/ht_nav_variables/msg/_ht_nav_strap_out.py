# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavStrapOut.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavStrapOut(type):
    """Metaclass of message 'HtNavStrapOut'."""

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
                'ht_nav_variables.msg.HtNavStrapOut')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_strap_out
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_strap_out
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_strap_out
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_strap_out
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_strap_out

            from ht_nav_variables.msg import HtNavEuler
            if HtNavEuler.__class__._TYPE_SUPPORT is None:
                HtNavEuler.__class__.__import_type_support__()

            from ht_nav_variables.msg import HtNavQuaternion
            if HtNavQuaternion.__class__._TYPE_SUPPORT is None:
                HtNavQuaternion.__class__.__import_type_support__()

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


class HtNavStrapOut(metaclass=Metaclass_HtNavStrapOut):
    """Message class 'HtNavStrapOut'."""

    __slots__ = [
        '_time',
        '_pos',
        '_vel',
        '_euler',
        '_quaternion',
    ]

    _fields_and_field_types = {
        'time': 'double',
        'pos': 'ht_nav_variables/HtNavVector3',
        'vel': 'ht_nav_variables/HtNavVector3',
        'euler': 'ht_nav_variables/HtNavEuler',
        'quaternion': 'ht_nav_variables/HtNavQuaternion',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavVector3'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavVector3'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavEuler'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavQuaternion'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.time = kwargs.get('time', float())
        from ht_nav_variables.msg import HtNavVector3
        self.pos = kwargs.get('pos', HtNavVector3())
        from ht_nav_variables.msg import HtNavVector3
        self.vel = kwargs.get('vel', HtNavVector3())
        from ht_nav_variables.msg import HtNavEuler
        self.euler = kwargs.get('euler', HtNavEuler())
        from ht_nav_variables.msg import HtNavQuaternion
        self.quaternion = kwargs.get('quaternion', HtNavQuaternion())

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
        if self.pos != other.pos:
            return False
        if self.vel != other.vel:
            return False
        if self.euler != other.euler:
            return False
        if self.quaternion != other.quaternion:
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
    def pos(self):
        """Message field 'pos'."""
        return self._pos

    @pos.setter
    def pos(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavVector3
            assert \
                isinstance(value, HtNavVector3), \
                "The 'pos' field must be a sub message of type 'HtNavVector3'"
        self._pos = value

    @property
    def vel(self):
        """Message field 'vel'."""
        return self._vel

    @vel.setter
    def vel(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavVector3
            assert \
                isinstance(value, HtNavVector3), \
                "The 'vel' field must be a sub message of type 'HtNavVector3'"
        self._vel = value

    @property
    def euler(self):
        """Message field 'euler'."""
        return self._euler

    @euler.setter
    def euler(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavEuler
            assert \
                isinstance(value, HtNavEuler), \
                "The 'euler' field must be a sub message of type 'HtNavEuler'"
        self._euler = value

    @property
    def quaternion(self):
        """Message field 'quaternion'."""
        return self._quaternion

    @quaternion.setter
    def quaternion(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavQuaternion
            assert \
                isinstance(value, HtNavQuaternion), \
                "The 'quaternion' field must be a sub message of type 'HtNavQuaternion'"
        self._quaternion = value
