# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavVehicleDebug.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavVehicleDebug(type):
    """Metaclass of message 'HtNavVehicleDebug'."""

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
                'ht_nav_variables.msg.HtNavVehicleDebug')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_vehicle_debug
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_vehicle_debug
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_vehicle_debug
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_vehicle_debug
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_vehicle_debug

            from ht_nav_variables.msg import HtNavStrapOut
            if HtNavStrapOut.__class__._TYPE_SUPPORT is None:
                HtNavStrapOut.__class__.__import_type_support__()

            from ht_nav_variables.msg import HtNavTireOut
            if HtNavTireOut.__class__._TYPE_SUPPORT is None:
                HtNavTireOut.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HtNavVehicleDebug(metaclass=Metaclass_HtNavVehicleDebug):
    """Message class 'HtNavVehicleDebug'."""

    __slots__ = [
        '_time',
        '_wheel_variables',
        '_imu_link_pva',
        '_fl_wheel_pva',
        '_fr_wheel_pva',
        '_rl_wheel_pva',
        '_rr_wheel_pva',
    ]

    _fields_and_field_types = {
        'time': 'double',
        'wheel_variables': 'ht_nav_variables/HtNavTireOut',
        'imu_link_pva': 'ht_nav_variables/HtNavStrapOut',
        'fl_wheel_pva': 'ht_nav_variables/HtNavStrapOut',
        'fr_wheel_pva': 'ht_nav_variables/HtNavStrapOut',
        'rl_wheel_pva': 'ht_nav_variables/HtNavStrapOut',
        'rr_wheel_pva': 'ht_nav_variables/HtNavStrapOut',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavTireOut'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavStrapOut'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavStrapOut'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavStrapOut'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavStrapOut'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavStrapOut'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.time = kwargs.get('time', float())
        from ht_nav_variables.msg import HtNavTireOut
        self.wheel_variables = kwargs.get('wheel_variables', HtNavTireOut())
        from ht_nav_variables.msg import HtNavStrapOut
        self.imu_link_pva = kwargs.get('imu_link_pva', HtNavStrapOut())
        from ht_nav_variables.msg import HtNavStrapOut
        self.fl_wheel_pva = kwargs.get('fl_wheel_pva', HtNavStrapOut())
        from ht_nav_variables.msg import HtNavStrapOut
        self.fr_wheel_pva = kwargs.get('fr_wheel_pva', HtNavStrapOut())
        from ht_nav_variables.msg import HtNavStrapOut
        self.rl_wheel_pva = kwargs.get('rl_wheel_pva', HtNavStrapOut())
        from ht_nav_variables.msg import HtNavStrapOut
        self.rr_wheel_pva = kwargs.get('rr_wheel_pva', HtNavStrapOut())

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
        if self.wheel_variables != other.wheel_variables:
            return False
        if self.imu_link_pva != other.imu_link_pva:
            return False
        if self.fl_wheel_pva != other.fl_wheel_pva:
            return False
        if self.fr_wheel_pva != other.fr_wheel_pva:
            return False
        if self.rl_wheel_pva != other.rl_wheel_pva:
            return False
        if self.rr_wheel_pva != other.rr_wheel_pva:
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
    def wheel_variables(self):
        """Message field 'wheel_variables'."""
        return self._wheel_variables

    @wheel_variables.setter
    def wheel_variables(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavTireOut
            assert \
                isinstance(value, HtNavTireOut), \
                "The 'wheel_variables' field must be a sub message of type 'HtNavTireOut'"
        self._wheel_variables = value

    @property
    def imu_link_pva(self):
        """Message field 'imu_link_pva'."""
        return self._imu_link_pva

    @imu_link_pva.setter
    def imu_link_pva(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavStrapOut
            assert \
                isinstance(value, HtNavStrapOut), \
                "The 'imu_link_pva' field must be a sub message of type 'HtNavStrapOut'"
        self._imu_link_pva = value

    @property
    def fl_wheel_pva(self):
        """Message field 'fl_wheel_pva'."""
        return self._fl_wheel_pva

    @fl_wheel_pva.setter
    def fl_wheel_pva(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavStrapOut
            assert \
                isinstance(value, HtNavStrapOut), \
                "The 'fl_wheel_pva' field must be a sub message of type 'HtNavStrapOut'"
        self._fl_wheel_pva = value

    @property
    def fr_wheel_pva(self):
        """Message field 'fr_wheel_pva'."""
        return self._fr_wheel_pva

    @fr_wheel_pva.setter
    def fr_wheel_pva(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavStrapOut
            assert \
                isinstance(value, HtNavStrapOut), \
                "The 'fr_wheel_pva' field must be a sub message of type 'HtNavStrapOut'"
        self._fr_wheel_pva = value

    @property
    def rl_wheel_pva(self):
        """Message field 'rl_wheel_pva'."""
        return self._rl_wheel_pva

    @rl_wheel_pva.setter
    def rl_wheel_pva(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavStrapOut
            assert \
                isinstance(value, HtNavStrapOut), \
                "The 'rl_wheel_pva' field must be a sub message of type 'HtNavStrapOut'"
        self._rl_wheel_pva = value

    @property
    def rr_wheel_pva(self):
        """Message field 'rr_wheel_pva'."""
        return self._rr_wheel_pva

    @rr_wheel_pva.setter
    def rr_wheel_pva(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavStrapOut
            assert \
                isinstance(value, HtNavStrapOut), \
                "The 'rr_wheel_pva' field must be a sub message of type 'HtNavStrapOut'"
        self._rr_wheel_pva = value
