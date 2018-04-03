# -*- coding: utf-8 -*-

"""
Geodaisy is a Python library for creating geo objects represented by types
and coordinates and translating between various standards and
representations, including GeoJSON, Well Known Text, and Python's
__geo_interface__ protcol, which is used by other geo libraries.

Geodaisy is lightweight and does not rely on C/C++ dependencies like libgeos.

Usage example:
   >>> from geodaisy.geo_object import GeoObject
   >>> geo_obj = GeoObject(thing)
   >>> geo_obj.geojson
   {'coordinates': XXX, 'type': xxx}

For more information about the library and how to use it, see README.md.
:copyright: (c) 2018 by Kevin Brochet-Nguyen.
:license: MIT—see LICENSE for more details.
"""

from .geo_object import GeoObject  # noqa: F401
