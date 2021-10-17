# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavKalmanOut.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavKalmanOut(type):
    """Metaclass of message 'HtNavKalmanOut'."""

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
                'ht_nav_variables.msg.HtNavKalmanOut')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_kalman_out
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_kalman_out
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_kalman_out
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_kalman_out
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_kalman_out

            from ht_nav_variables.msg import HtNavErrorVector
            if HtNavErrorVector.__class__._TYPE_SUPPORT is None:
                HtNavErrorVector.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HtNavKalmanOut(metaclass=Metaclass_HtNavKalmanOut):
    """Message class 'HtNavKalmanOut'."""

    __slots__ = [
        '_pos_err',
        '_vel_err',
        '_att_err',
        '_bias',
        '_drift',
    ]

    _fields_and_field_types = {
        'pos_err': 'ht_nav_variables/HtNavErrorVector',
        'vel_err': 'ht_nav_variables/HtNavErrorVector',
        'att_err': 'ht_nav_variables/HtNavErrorVector',
        'bias': 'ht_nav_variables/HtNavErrorVector',
        'drift': 'ht_nav_variables/HtNavErrorVector',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavErrorVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavErrorVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavErrorVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavErrorVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavErrorVector'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ht_nav_variables.msg import HtNavErrorVector
        self.pos_err = kwargs.get('pos_err', HtNavErrorVector())
        from ht_nav_variables.msg import HtNavErrorVector
        self.vel_err = kwargs.get('vel_err', HtNavErrorVector())
        from ht_nav_variables.msg import HtNavErrorVector
        self.att_err = kwargs.get('att_err', HtNavErrorVector())
        from ht_nav_variables.msg import HtNavErrorVector
        self.bias = kwargs.get('bias', HtNavErrorVector())
        from ht_nav_variables.msg import HtNavErrorVector
        self.drift = kwargs.get('drift', HtNavErrorVector())

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
        if self.pos_err != other.pos_err:
            return False
        if self.vel_err != other.vel_err:
            return False
        if self.att_err != other.att_err:
            return False
        if self.bias != other.bias:
            return False
        if self.drift != other.drift:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def pos_err(self):
        """Message field 'pos_err'."""
        return self._pos_err

    @pos_err.setter
    def pos_err(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavErrorVector
            assert \
                isinstance(value, HtNavErrorVector), \
                "The 'pos_err' field must be a sub message of type 'HtNavErrorVector'"
        self._pos_err = value

    @property
    def vel_err(self):
        """Message field 'vel_err'."""
        return self._vel_err

    @vel_err.setter
    def vel_err(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavErrorVector
            assert \
                isinstance(value, HtNavErrorVector), \
                "The 'vel_err' field must be a sub message of type 'HtNavErrorVector'"
        self._vel_err = value

    @property
    def att_err(self):
        """Message field 'att_err'."""
        return self._att_err

    @att_err.setter
    def att_err(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavErrorVector
            assert \
                isinstance(value, HtNavErrorVector), \
                "The 'att_err' field must be a sub message of type 'HtNavErrorVector'"
        self._att_err = value

    @property
    def bias(self):
        """Message field 'bias'."""
        return self._bias

    @bias.setter
    def bias(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavErrorVector
            assert \
                isinstance(value, HtNavErrorVector), \
                "The 'bias' field must be a sub message of type 'HtNavErrorVector'"
        self._bias = value

    @property
    def drift(self):
        """Message field 'drift'."""
        return self._drift

    @drift.setter
    def drift(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavErrorVector
            assert \
                isinstance(value, HtNavErrorVector), \
                "The 'drift' field must be a sub message of type 'HtNavErrorVector'"
        self._drift = value
