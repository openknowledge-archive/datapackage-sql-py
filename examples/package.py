# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import sys
import json
from sqlalchemy import create_engine

sys.path.insert(0, '.')
import jtssql
import dpsql


def run(import_descriptor='examples/data/spending/datapackage.json',
        export_descriptor='tmp/datapackage.json',
        prefix='test_'):

    # Storage
    engine = create_engine('sqlite:///:memory:')
    storage = jtssql.Storage(engine=engine, prefix=prefix)

    # Import
    print('[Import]')
    dpsql.import_package(
           storage=storage,
           descriptor=import_descriptor,
           force=True)
    print('imported')

    # Export
    print('[Export]')
    dpsql.export_package(
            storage=storage,
            descriptor=export_descriptor)
    print('exported')

    return locals()


if __name__ == '__main__':
    run()
