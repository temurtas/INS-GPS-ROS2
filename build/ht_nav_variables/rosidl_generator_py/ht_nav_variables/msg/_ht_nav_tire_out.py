# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ht_nav_variables:msg/HtNavTireOut.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HtNavTireOut(type):
    """Metaclass of message 'HtNavTireOut'."""

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
                'ht_nav_variables.msg.HtNavTireOut')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ht_nav_tire_out
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ht_nav_tire_out
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ht_nav_tire_out
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ht_nav_tire_out
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ht_nav_tire_out

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


class HtNavTireOut(metaclass=Metaclass_HtNavTireOut):
    """Message class 'HtNavTireOut'."""

    __slots__ = [
        '_effective_radius_est',
        '_vehicle_mass_est',
        '_wheel_side_slip_ang',
        '_wheel_longitudinal_slip_ratio',
        '_tire_lateral_forces',
        '_tire_longitudinal_forces',
    ]

    _fields_and_field_types = {
        'effective_radius_est': 'double',
        'vehicle_mass_est': 'double',
        'wheel_side_slip_ang': 'ht_nav_variables/HtNavWheelVector',
        'wheel_longitudinal_slip_ratio': 'ht_nav_variables/HtNavWheelVector',
        'tire_lateral_forces': 'ht_nav_variables/HtNavWheelVector',
        'tire_longitudinal_forces': 'ht_nav_variables/HtNavWheelVector',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ht_nav_variables', 'msg'], 'HtNavWheelVector'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.effective_radius_est = kwargs.get('effective_radius_est', float())
        self.vehicle_mass_est = kwargs.get('vehicle_mass_est', float())
        from ht_nav_variables.msg import HtNavWheelVector
        self.wheel_side_slip_ang = kwargs.get('wheel_side_slip_ang', HtNavWheelVector())
        from ht_nav_variables.msg import HtNavWheelVector
        self.wheel_longitudinal_slip_ratio = kwargs.get('wheel_longitudinal_slip_ratio', HtNavWheelVector())
        from ht_nav_variables.msg import HtNavWheelVector
        self.tire_lateral_forces = kwargs.get('tire_lateral_forces', HtNavWheelVector())
        from ht_nav_variables.msg import HtNavWheelVector
        self.tire_longitudinal_forces = kwargs.get('tire_longitudinal_forces', HtNavWheelVector())

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
        if self.effective_radius_est != other.effective_radius_est:
            return False
        if self.vehicle_mass_est != other.vehicle_mass_est:
            return False
        if self.wheel_side_slip_ang != other.wheel_side_slip_ang:
            return False
        if self.wheel_longitudinal_slip_ratio != other.wheel_longitudinal_slip_ratio:
            return False
        if self.tire_lateral_forces != other.tire_lateral_forces:
            return False
        if self.tire_longitudinal_forces != other.tire_longitudinal_forces:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def effective_radius_est(self):
        """Message field 'effective_radius_est'."""
        return self._effective_radius_est

    @effective_radius_est.setter
    def effective_radius_est(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'effective_radius_est' field must be of type 'float'"
        self._effective_radius_est = value

    @property
    def vehicle_mass_est(self):
        """Message field 'vehicle_mass_est'."""
        return self._vehicle_mass_est

    @vehicle_mass_est.setter
    def vehicle_mass_est(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vehicle_mass_est' field must be of type 'float'"
        self._vehicle_mass_est = value

    @property
    def wheel_side_slip_ang(self):
        """Message field 'wheel_side_slip_ang'."""
        return self._wheel_side_slip_ang

    @wheel_side_slip_ang.setter
    def wheel_side_slip_ang(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'wheel_side_slip_ang' field must be a sub message of type 'HtNavWheelVector'"
        self._wheel_side_slip_ang = value

    @property
    def wheel_longitudinal_slip_ratio(self):
        """Message field 'wheel_longitudinal_slip_ratio'."""
        return self._wheel_longitudinal_slip_ratio

    @wheel_longitudinal_slip_ratio.setter
    def wheel_longitudinal_slip_ratio(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'wheel_longitudinal_slip_ratio' field must be a sub message of type 'HtNavWheelVector'"
        self._wheel_longitudinal_slip_ratio = value

    @property
    def tire_lateral_forces(self):
        """Message field 'tire_lateral_forces'."""
        return self._tire_lateral_forces

    @tire_lateral_forces.setter
    def tire_lateral_forces(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'tire_lateral_forces' field must be a sub message of type 'HtNavWheelVector'"
        self._tire_lateral_forces = value

    @property
    def tire_longitudinal_forces(self):
        """Message field 'tire_longitudinal_forces'."""
        return self._tire_longitudinal_forces

    @tire_longitudinal_forces.setter
    def tire_longitudinal_forces(self, value):
        if __debug__:
            from ht_nav_variables.msg import HtNavWheelVector
            assert \
                isinstance(value, HtNavWheelVector), \
                "The 'tire_longitudinal_forces' field must be a sub message of type 'HtNavWheelVector'"
        self._tire_longitudinal_forces = value
