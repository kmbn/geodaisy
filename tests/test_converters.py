# -*- coding: utf-8 -*-

"""Tests for geodaisy.converters."""

import geojson
import pytest
import shapely.wkt

import geodaisy.converters as convert

from .shapes import (geojson_shapes,
                     wkt_shapes)


@pytest.mark.parametrize('shape', wkt_shapes)
def test_geojson_from_wkt(shape):
    test_geojson = convert.wkt_to_geojson(shape)
    check = geojson.loads(test_geojson)

    assert check.is_valid


@pytest.mark.parametrize('shape', geojson_shapes)
def test_wkt_from_geojson(shape):
    wkt = convert.geojson_to_wkt(shape)
    check = shapely.wkt.loads(wkt)

    assert check.is_valid
