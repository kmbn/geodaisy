# -*- coding: utf-8 -*-

"""
geodaisy.geo_object
~~~~~~~~~~~~~~~~

This module provides a GeoObject object for creating Python geo objects that
that translate to and from other geo libraries, mappings, and specificaions.
"""

import json
from typing import Any  # noqa: F401

from .converters import (dict_to_geo_interface,
                         geo_interface_to_geojson,
                         geo_interface_to_wkt,
                         wkt_to_geo_interface,
                         wkt_types)


class GeoObject(object):
    """
    Creates an object from an object's geo_interface or from WKT or GeoJSON.

    GeoJSON (serialized and raw), WKT (Well Known Text), and normalized
    geo_interface representations of the object are available as attributes.
    """

    def __init__(self, geo_thing):
        # type: (Any) -> None
        """
        Creates a GeoObject if geo_thing has or represents a geo_interface.
        """
        geo_interface = self._get_geo_interface(geo_thing)
        self.type = geo_interface['type']
        self.coordinates = geo_interface['coordinates']

    def __repr__(self):
        # type: () -> str
        return str(self.__geo_interface__)

    __str__ = __repr__

    @property
    def __geo_interface__(self):
        # type: () -> dict
        """Returns the geo_interface representation of the object."""
        return {'type': self.type, 'coordinates': self.coordinates}

    def geojson(self):
        # type: () -> str
        """Returns the serialized GeoJSON representation of the object."""
        return json.dumps(self.rawgeojson())

    def rawgeojson(self):
        # type: () -> dict
        """Returns the unserialized GeoJSON representation of the object."""
        return geo_interface_to_geojson(self.__geo_interface__)

    def wkt(self):
        # type: () -> str
        """Returns the Well Known Text representation of the object."""
        return geo_interface_to_wkt(self.__geo_interface__)

    def _get_geo_interface(self, geo_thing):
        # type: (Any) -> dict
        """Attempts to get an object's geo_interface."""
        # Input might be GeoJSON or WKT
        if isinstance(geo_thing, str):
            geo_interface = self._parse_string(geo_thing)
        # Input might be raw GeoJSON or a geo_interface dictionary
        elif isinstance(geo_thing, dict):
            geo_interface = dict_to_geo_interface(geo_thing)
        # Input might be an object with a geo_interface
        else:
            try:
                geo_interface = dict_to_geo_interface(
                    geo_thing.__geo_interface__)
            except AttributeError:
                raise AttributeError('Object has no geo_interface.')

        return geo_interface

    def _parse_string(self, geo_thing):
        # type: (str) -> dict
        """Checks to see if the string is geojson or WKT."""
        error_msg = 'Strings must be valid GeoJSON or WKT'
        if geo_thing.startswith('{'):
            try:
                geo_dict = json.loads(geo_thing)
                return dict_to_geo_interface(geo_dict)
            except ValueError:
                raise ValueError(error_msg)
        else:
            wkt_type = geo_thing.split(' ')[0]
            if wkt_type not in wkt_types:
                raise ValueError(error_msg)
            else:
                return wkt_to_geo_interface(geo_thing)
