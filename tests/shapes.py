# -*- coding: utf-8 -*-

"""Pre-defined shapes in various formats for tests."""

import geojson


# Points
geo_point = geojson.Point((-115.81, 37.24))
wkt_point = 'POINT (30 10)'


# LineStrings
geo_linestring = geojson.LineString([(8.919, 44.4074), (8.923, 44.4075)])
wkt_linestring = 'LINESTRING (30 10, 10 30, 40 40)'
wkt_linestring_ne = 'LINESTRING (58.612 34.642,58.613 34.641)'
wkt_linestring_sw = 'linestring (-58.612 -34.642,-58.613 -34.641)'
wkt_linestring_se = 'LINESTRING(58.612 -34.642,58.613 -34.641)'
wkt_linestring_nw = 'linestring(-58.612 34.642,-58.613 34.641)'


# Polygons
geo_polygon = geojson.Polygon(
    [
        [
            (2.38, 57.322), (23.194, -20.28),
            (-120.43, 19.15), (2.38, 57.322)
        ]
    ]
)
wkt_polygon = 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))'


# Polygons with holes
geo_polygon_with_hole = geojson.Polygon(
    [
        [
            (2.38, 57.322), (23.194, -20.28),
            (-120.43, 19.15), (2.38, 57.322)
        ],
        [
            (-5.21, 23.51), (15.21, -10.81),
            (-20.51, 1.51), (-5.21, 23.51)
        ]
    ]
)
wkt_polygon_with_hole = ('POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10),'
                         ' (20 30, 35 35, 30 20, 20 30))')


# MultiPoints
geo_multipoint = geojson.MultiPoint(
    [
        (-155.52, 19.61), (-156.22, 20.74),
        (-157.97, 21.46)
    ]
)
wkt_multipoint = 'MULTIPOINT (10 40, 40 30, 20 20, 30 10)'
wkt_multipoint_alternate = 'MULTIPOINT ((10 40), (40 30), (20 20), (30 10))'


# MultiLineStrings
geo_multilinestring = geojson.MultiLineString(
    [
        [
            (3.75, 9.25), (-130.95, 1.52)
        ],
        [
            (23.15, -34.25), (-1.35, -4.65), (3.45, 77.95)
        ]
    ]
)
wkt_multilinestring = ('MULTILINESTRING ((10 10, 20 20, 10 40),'
                       ' (40 40, 30 30, 40 20, 30 10))')


# MultiPolygons
geo_multipolygon = geojson.MultiPolygon(
    [
        [
            (
                [
                    (30, 20), (45, 40),
                    (10, 40), (30, 20)
                ]
            ),
            (
                [
                    (15, 5), (40, 10), (10, 20),
                    (5, 10), (15, 5)
                ]
            )
        ]
    ]
)
wkt_multipolygon = ('MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)),'
                    ' ((15 5, 40 10, 10 20, 5 10, 15 5)))')


# MultiPolygons with holes
wkt_multipolygon_with_hole = ('MULTIPOLYGON (((40 40, 20 45, 45 30, 40 40)),'
                              ' ((20 35, 10 30, 10 10, 30 5, 45 20, 20 35),'
                              ' (30 20, 20 15, 20 25, 30 20)))')


geo_interface_shapes = [geo_point, geo_linestring, geo_polygon,
                        geo_polygon_with_hole, geo_multipoint,
                        geo_multilinestring, geo_multipolygon]


geojson_shapes = [geojson.dumps(x) for x in geo_interface_shapes]


wkt_shapes = [wkt_point, wkt_linestring, wkt_polygon, wkt_polygon_with_hole,
              wkt_multipoint, wkt_multilinestring, wkt_multipolygon,
              wkt_multipolygon_with_hole, wkt_linestring_ne,
              wkt_linestring_nw, wkt_linestring_se, wkt_linestring_sw]
