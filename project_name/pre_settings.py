# This settings file to setup setting must be imported before importing geonode settings to affect

import os
from distutils.sysconfig import get_python_lib

if os.name == 'nt':
    os.environ['Path'] = (r'%s\osgeo;' % (get_python_lib())) + os.environ['Path']

os.environ.setdefault('DEFAULT_BACKEND_UPLOADER', 'geonode.importer')
