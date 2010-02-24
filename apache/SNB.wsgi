import os
import sys

sys.path.append('/home/stepheno/development/')
sys.path.append('/home/stepheno/development/StrangeBrew')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
