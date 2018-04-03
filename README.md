# Geodaisy: Python GeoJSON, WKT, and \_\_geo_interface\_\_ made easy

[![GitHub license](https://img.shields.io/github/license/kmbn/geodaisy.svg?style=flat-square)](https://raw.githubusercontent.com/kmbn/geodaisy/master/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/geodaisy.svg?style=flat-square)](https://pypi.org/project/geodaisy/)
[![Travis](https://img.shields.io/travis/kmbn/geodaisy.svg?style=flat-square)](https://travis-ci.org/kmbn/geodaisy)

Geodaisy helps you convert to and from GeoJSON, Well Known Text (WKT), and Python objects that support the \_\_geo_interface\_\_ standard.

Geodaisy works with Python 2 and Python 3.

## What's this for?

Geodaisy is for you if you:
- Have GeoJSON and need WKT
- Have WKT and need GeoJSON
- Have GeoJSON or WKT and need a Python dictionary or array
- Have a Pyshp shape object after reading a shapefile and need GeoJSON or WKT
- Have a Shapely shape object and need GeoJSON or WKT
- Have any other Python object with a \_\_geo_interface\_\_ and need GeoJSON or WKT
- Want a \_\_geo_interface\_\_ dictionary that correctly and consistently implements the [specification](https://gist.github.com/sgillies/2217756)

Geodaisy provides a GeoObject that can be created from any of the formats or objects above. GeoObject methods output GeoJSON, WKT, etc. representations of the object. Geodaisy also includes individual converters that can be used separately if you do not need an object.

### Examples

#### Convert WKT to GeoJSON
```python
>>> import geodaisy.converters as convert
>>> wkt = 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))'
>>> convert.wkt_to_geojson(wkt)
'{"type": "Polygon", "coordinates": [[[30, 10], [40, 40], [20, 40], [10, 20], [30, 10]]]}'
```

#### Convert GeoJSON to WKT
```python
>>> import geodaisy.converters as convert
>>> geojson = '{"type": "Polygon", "coordinates": [[[30, 10], [40, 40], [20, 40], [10, 20], [30, 10]]]}'
>>> convert.geojson_to_wkt(geojson)
'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))'
```

#### Create a GeoObject from any Python object with a geo_interface
```python
>>> from shapely.geometry import Polygon
>>> polygon = Polygon([(30, 10), (40, 40), (20, 40), (10, 20), (30, 10)])
>>> from geodaisy import GeoObject
>>> geo_obj = GeoObject(polygon)
>>> geo_obj
{'type': 'Polygon', 'coordinates': [[(30.0, 10.0), (40.0, 40.0), (20.0, 40.0), (10.0, 20.0), (30.0, 10.0)]]}
>>> geo_obj.type
'Polygon'
>>> geo_obj.coordinates
[[(30.0, 10.0), (40.0, 40.0), (20.0, 40.0), (10.0, 20.0), (30.0, 10.0)]]
>>> geo_obj.geojson()
'{"type": "Polygon", "coordinates": [[[30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0]]]}'
>>> geo_obj.wkt()
'POLYGON ((30.0 10.0, 40.0 40.0, 20.0 40.0, 10.0 20.0, 30.0 10.0))'
```

## Why use this instead Shapely or geojson, etc.?
Other libraries are only offer translations to and from specific formats. For example, Shapely can go to and from WKT and \_\_geo_interface\_\_, but not GeoJSON. geojson can go to and from GeoJSON and \_\_geo_interface\_\_, but not WKT. If you need more than one kind of translation, you need to use more than one library. Geodaisy translates to and from multiple formats.

In addition, some other libraries, like Shapely, are much heavier. That makes sense, since they also do a lot more—but it also makes installing them more of a chore. Geodaisy is lightweight and has no dependencies beyond Python core.

## When should I use something else?

### If you need to validate coordinates
Geodaisy does not validate coordinates. Yet. If you need to validate coordinates, you might find libraries like [Shapely](https://pypi.org/project/Shapely/) or [geojson](https://pypi.org/project/geojson/) helpful, depending on what your expected inputs and outputs are. Note that neither of them fully validate coordinates when creating a shape object—you need to create an object first, and then validate it, meaning that whether you use Geodaisy or one of the other libraries, you may wind up creating an invalid shape.

In the future, Geodaisy will validate coordinates when creating objects. (If you'd like to help make that possible, [contributions are welcome!](#contributions))

Note that you can still use Geodaisy _with_ other geo libraries, or as a go-between or intermediary _between_ other libraries or types of object.

### If you need geometric predicates, relationships, transformations and other operations on geometric objects
If you need any of the above, you probably need [Shapely](https://pypi.org/project/Shapely/).

## How to install
`pip install geodaisy`

## Running the tests
(The following commands assume you're in the `geodaisy` root directory.)

Geodaisy uses the pytest testing framework as well as the Shapely and geojson libraries for testing. You'll need to install them first by doing `pip install -r dev-requirements.txt`.

If you're using Python 2 or a version of Python 3 prior to 3.5, you'll need to make sure that the `typing` module is installed: `pip install -r py2-requirements.txt`or `pip install typing`

To run the tests, just do `pytest`.

## <a id="contributing"></a>Contributing
Contributions are very welcome! In addition to the tests mentioned above, Geodaisy also uses flake8 for linting and Mypy for type checking. Pull requests will need to pass the tests as well as flake8 and Mypy checks (unless you're developing with Python 2, in which case you'll have to skip Mypy, since it requires Python 3.

(The following commands assume you're in the Geodaisy root directory and have already pip-installed the dev requirements (see above).)

To run flake8: `flake8 src tests`

To run Mypy (if you're using Python 3): `mypy --py2 src`

## License
Geodaisy is licensed under the [MIT License](https://raw.githubusercontent.com/kmbn/geodaisy/master/LICENSE) and is free for commercial and private use.

## Copyright
Copyright &copy; 2018 Kevin Brochet-Nguyen
