# datapackage-sql-py

[![Travis](https://img.shields.io/travis/okfn/datapackage-sql-py.svg)](https://travis-ci.org/okfn/datapackage-sql-py)
[![Coveralls](http://img.shields.io/coveralls/okfn/datapackage-sql-py.svg?branch=master)](https://coveralls.io/r/okfn/datapackage-sql-py?branch=master)

Generate and load SQL tables based on Data Package.

## Usage

This section is intended to be used by end-users of the library.

### Import/Export

> See section below how to get SQL engine.

High-level API is easy to use.

Having Data Package in current directory we can import it to sql database:

```python
import jtssql
import dpsql

storage = jtssql.Storage(<engine>)
dpsql.import_package(storage, 'descriptor.json')
```

Also we can export it from sql database:

```python
import jtssql
import dpsql

storage = jtssql.Storage(<engine>)
dpsql.export_package(storage, 'descriptor.json')
```

### SQL Engine

SQLAlchemy is used as sql wrapper. We can get engine this way:

```python
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
```

### Design Overview

#### Storage & Drivers

See jsontableschema layer [readme](https://github.com/okfn/jsontableschema-sql-py/tree/update).

#### Mappings

```
datapackage.json -> *not stored*
datapackage.json resources -> sql  tables
data/data.csv schema -> sql table schema
data/data.csv data -> sql table data
```

## Development

This section is intended to be used by tech users collaborating
on this project.

### Getting Started

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code
and get `run` command as unified developer interface:

```
$ source activate.sh
```

### Reviewing

The project follow the next style guides:
- [Open Knowledge Coding Standards and Style Guide](https://github.com/okfn/coding-standards)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

To check the project against Python style guide:

```
$ run review
```

### Testing

To run tests with coverage check:

```
$ run test
```

Coverage data will be in the `.coverage` file.
