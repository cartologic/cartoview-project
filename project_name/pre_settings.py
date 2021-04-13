import os
from distutils.sysconfig import get_python_lib

if os.name == 'nt':
    os.environ['Path'] = (r'%s\osgeo;' % (get_python_lib())) + os.environ['Path']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('APPS_DIR', os.path.abspath(os.path.join(BASE_DIR, "apps")))

os.environ.setdefault('DEFAULT_BACKEND_UPLOADER', 'geonode.importer')
