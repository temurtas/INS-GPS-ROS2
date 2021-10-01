# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavErrorVector.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavErrorVector(type):
    """Metaclass of message 'HtNavErrorVector'."""

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
                'ht_nav_variables.msg.HtNavErrorVector')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_error_vector
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_error_vector
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_error_vector
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_error_vector
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_error_vector

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HtNavErrorVector(metaclass=Metaclass_HtNavErrorVector):
    """Message class 'HtNavErrorVector'."""

    __slots__ = [
        '_err_x',
        '_err_y',
        '_err_z',
    ]

    _fields_and_field_types = {
        'err_x': 'double',
        'err_y': 'double',
        'err_z': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.err_x = kwargs.get('err_x', float())
        self.err_y = kwargs.get('err_y', float())
        self.err_z = kwargs.get('err_z', float())

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
        if self.err_x != other.err_x:
            return False
        if self.err_y != other.err_y:
            return False
        if self.err_z != other.err_z:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def err_x(self):
        """Message field 'err_x'."""
        return self._err_x

    @err_x.setter
    def err_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'err_x' field must be of type 'float'"
        self._err_x = value

    @property
    def err_y(self):
        """Message field 'err_y'."""
        return self._err_y

    @err_y.setter
    def err_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'err_y' field must be of type 'float'"
        self._err_y = value

    @property
    def err_z(self):
        """Message field 'err_z'."""
        return self._err_z

    @err_z.setter
    def err_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'err_z' field must be of type 'float'"
        self._err_z = value
