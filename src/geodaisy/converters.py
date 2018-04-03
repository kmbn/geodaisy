# -*- coding: utf-8 -*-

"""
geodaisy.converters
~~~~~~~~~~~~~~~~

This module provides converters to and from GeoJSON, WKT, geo_interface, etc.

geodaisy.geo_object uses these converters; they can also be used directly.
"""

import json
import re
from ast import literal_eval
from typing import Union  # noqa: F401


geo_types = {'Point', 'MultiPoint', 'LineString', 'MultiLineString',
             'Polygon', 'MultiPolygon'}

wkt_types = {x.upper() for x in geo_types}

type_translations = {x.upper(): x for x in geo_types}


def geo_interface_to_wkt(geo_interface):
    # type: (dict) -> str
    """Converts a geo_interface dictionary to a Well Known Text string."""
    # Convert to string and change brackets to parentheses
    coords = str(geo_interface['coordinates'])
    coords = coords.replace('[', '(')
    coords = coords.replace(']', ')')

    # Remove commas within coordinate pairs
    coords = re.sub(r'(?<=\d),', '', coords)

    # Remove parentheses and commas separating coordinates
    coords = re.sub(r'(?<=\d)\), \(', ', ', coords)

    # Get the type and clean up extra parentheses in special cases
    geo_type = geo_interface['type'].upper()

    if geo_type == 'LINESTRING':
        coords = coords.replace('((', '(')
        coords = coords.replace('))', ')')
        coords = coords.replace('), (', ', ')
    elif geo_type in {'MULTILINESTRING', 'POLYGON'}:
        coords = coords.replace('(((', '((')
        coords = coords.replace(')))', '))')
        coords = coords.replace(')), ((', '), (')
    elif geo_type == 'MULTIPOINT':
        coords = coords.replace('((', '(')
        coords = coords.replace('))', ')')
    elif geo_type == 'MULTIPOLYGON':
        coords = coords.replace('((((', '(((')
        coords = coords.replace('))))', ')))')
        coords = coords.replace('))), (((', ')), ((')

    return '{} {}'.format(geo_type, coords)


def wkt_to_geo_interface(wkt):
    # type: (str) -> dict
    """Converts a WKT string to a geo_interface dictionary."""
    try:
        wkt_type, coords = re.split(r'(?<=[A-Z])\s', wkt)

        geo_type = type_translations[wkt_type]

        # Clean up the strings so they'll covert correctly
        if geo_type in {'Polygon', 'MultiLineString', 'MultiPolygon'}:
            coords = re.sub(r'(?<=\d)\), \((?=\d)', ')), ((', coords)

        # Pairs of coordinates must be enclosed in parentheses
        coords = re.sub(r'(?<=\d), (?=\d)', '), (', coords)

        # Coordinates within parentheses must be separated by commas
        coords = re.sub(r'(?<=\d) (?=\d)', ', ', coords)

        # Now we can turn the string into a tuple or a tuple of tuples
        coords = literal_eval(coords)

        coords = reformat_coordinates(coords, 'geo_interface')  # type: ignore  # noqa: E501

        # If we only have a simple polygon (no hole), the coordinate array
        # won't be deep enough to satisfy the GeoJSON/geo_interface spec, so
        # we need to enclose it in a list.
        numbers = {float, int}
        if geo_type == 'Polygon' and type(coords[0][0]) in numbers:
            coords = [coords]  # type: ignore
        elif geo_type == 'MultiPolygon' and type(coords[0][0][0]) in numbers:
            coords = [coords]  # type: ignore

    except Exception:
        raise ValueError('{} is not a WKT string'.format(wkt))

    return {'type': geo_type, 'coordinates': coords}


def dict_to_geo_interface(geo_dict):
    # type: (dict) -> dict
    """Converts a dictionary into a standardized geo_interface dictionary."""
    if not geo_dict.get('type') in geo_types:
        raise ValueError('A geo_interface-compatible dictionary must'
                         ' have a "type" key with one of the following'
                         'values: {}'.format(geo_types))
    try:
        coordinates = geo_dict['coordinates']
    except KeyError:
        raise KeyError('A geo_interface-compatible dictionary must'
                       ' have a "coordinates" key-value pair.')
    geo_dict['coordinates'] = reformat_coordinates(coordinates,
                                                   'geo_interface')

    return geo_dict


def geo_interface_to_geojson(geo_interface):
    # type: (dict) -> dict
    """Converts a geo_interface dictionary into a raw GeoJSON dictionary."""
    coords = reformat_coordinates(geo_interface['coordinates'], 'geojson')

    return {'type': geo_interface['type'], 'coordinates': coords}


def wkt_to_geojson(wkt):
    # type: (str) -> str
    """Converts a WKT string to serialized GeoJSON."""
    return json.dumps(geo_interface_to_geojson(wkt_to_geo_interface(wkt)))


def geojson_to_wkt(geojson):
    # type: (Union[str, dict]) -> str
    """Converts GeoJSON (serialize or raw) to a WKT string."""
    if isinstance(geojson, str):
        raw_geojson = json.loads(geojson)  # type: dict
    elif isinstance(geojson, dict):
        raw_geojson = geojson
    else:
        raise ValueError('{} is not GeoJSON'.format(geojson))

    return geo_interface_to_wkt(dict_to_geo_interface(raw_geojson))


def reformat_coordinates(item, style):
    # type: (Union[list, tuple], str) -> Union[list, tuple]
    """
    Converts tuples, tuples of tuples, lists of tuples, etc. into lists and
    lists of lists, etc. and preserves points/coordinate pairs as lists or
    tuples depending on the desired style.
    """
    if type(item) in {tuple, list} and type(item[0]) in {tuple, list}:
        return [reformat_coordinates(x, style) for x in item]
    else:
        if style == 'geojson':
            return list(item)
        elif style == 'geo_interface':
            return tuple(item)
        else:
            raise ValueError('style must be geojson or geo_interface.')
