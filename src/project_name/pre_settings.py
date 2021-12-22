import os
from distutils.sysconfig import get_python_lib

if os.name == 'nt':
    os.environ['Path'] = (r'%s\osgeo;' % (get_python_lib())) + os.environ['Path']
    os.environ['PROJ_LIB'] = r'%s\osgeo\data\proj' % (get_python_lib())

    os.environ.setdefault('CELERY_RESULT_BACKEND_PATH',
                              os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), '.celery_results'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('APPS_DIR', os.path.abspath(os.path.join(BASE_DIR, "apps")))