#!/usr/bin/python3
"""
Advanced task
"""


class LockedClass():
    """A limited class"""
    def __setattr__(self, name, value):
        """Limiting the attribute setting feature"""
        if name != 'first_name':
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'")
        self.__dict__[f'{name}'] = value
