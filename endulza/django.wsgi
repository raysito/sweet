#import os
#import sys
 
#path = '/srv/www'
#if path not in sys.path:
#    sys.path.insert(0, '/srv/www')
 
#os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'
 
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
import os
import sys
import site
root_dir = os.path.abspath(os.path.dirname(__file__))
#site.addsitedir(os.path.join('/home/ray/Documentos/dev/django-mysql/lib/python2.7/site-packages'))
sys.path.append(root_dir)
sys.path.append('/home/ray/Documentos/dev/django-mysql/lib/python2.7/site-packages')
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'endulza.settings'
 
import django.core.handlers.wsgi
 
application = django.core.handlers.wsgi.WSGIHandler()
