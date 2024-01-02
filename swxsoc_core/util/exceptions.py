"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""
import warnings

__all__ = [
    "SpaceWeatherWarning",
    "SpaceWeatherUserWarning",
    "SpaceWeatherDeprecationWarning",
    "SpaceWeatherPendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class SpaceWeatherWarning(Warning):
    """
    The base warning class from which all SpaceWeather warnings should inherit.

    Any warning inheriting from this class is handled by the SpaceWeather
    logger. This warning should not be issued in normal code. Use
    "SpaceWeatherUserWarning" instead or a specific sub-class.
    """


class SpaceWeatherUserWarning(UserWarning, SpaceWeatherWarning):
    """
    The primary warning class for SWxSOC.

    Use this if you do not need a specific type of warning.
    """


class SpaceWeatherDeprecationWarning(FutureWarning, SpaceWeatherWarning):
    """
    A warning class to indicate a deprecated feature.
    """


class SpaceWeatherPendingDeprecationWarning(
    PendingDeprecationWarning, SpaceWeatherWarning
):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `SpaceWeatherUserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, SpaceWeatherUserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `SpaceWeatherDeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, SpaceWeatherDeprecationWarning, stacklevel + 1)
