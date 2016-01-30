# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
from sqlalchemy import create_engine

sys.path.insert(0, '.')
import jtssql
import dpsql


def run(url, prefix, source, target):

    # Storage
    engine = create_engine(url)
    storage = jtssql.Storage(engine=engine, prefix=prefix)

    # Import package
    dpsql.import_package(storage, source)
    print('Imported datapackage from "%s"' % source)

    # Export package
    dpsql.export_package(storage, target)
    print('Exported datapackage to "%s"' % target)
