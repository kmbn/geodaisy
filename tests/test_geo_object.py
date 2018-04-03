# -*- coding: utf-8 -*-

"""Tests for GeoObject."""

import geojson
import pytest
import shapely.wkt

from geodaisy.geo_object import GeoObject

from .shapes import (geo_interface_shapes,
                     geojson_shapes,
                     wkt_shapes)


@pytest.mark.parametrize('shape', geo_interface_shapes)
def test_geo_interface_to_geojson(shape):
    """Verify that a GeoObject has a valid geojson attribute."""
    geo_obj = GeoObject(shape)

    check = geojson.loads(geo_obj.geojson())

    assert check.is_valid
    assert geo_obj.geojson() == geojson.dumps(shape)


@pytest.mark.parametrize('shape', geo_interface_shapes)
def test_wkt_from_geo_interface(shape):
    geo_obj = GeoObject(shape)

    check = shapely.wkt.loads(geo_obj.wkt())

    assert check.is_valid
    # Shapely introduces extra precision and seems to distort floats,
    # so we can't just assert geo_obj.wkt == shapely.wkt.dumps(check)


@pytest.mark.parametrize('shape', geojson_shapes)
def test_wkt_from_geojson(shape):
    geo_obj = GeoObject(shape)

    check = shapely.wkt.loads(geo_obj.wkt())

    assert check.is_valid
    # Shapely introduces extra precision and seems to distort floats,
    # so we can't just assert geo_obj.wkt == shapely.wkt.dumps(check)


@pytest.mark.parametrize('shape', wkt_shapes)
def test_geojson_from_wkt(shape):
    geo_obj = GeoObject(shape)
    check = geojson.loads(geo_obj.geojson())

    assert check.is_valid
