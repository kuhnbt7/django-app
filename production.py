import os

import dj_database_url

from .settings import *

DATABASES = {
	'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static_')
SECRET_KEY = os.environ.get('SECRET_KEY')


Ubuntu server username: py230admin
Ubuntu server password:  vdNgp6t#XmRhMRv6n
Ubuntu server DNS: py230-ubuntu-00502.westus.cloudapp.azure.com
Ubuntu server SSH Port: 22
Postgres server username: postgres
Postgres server password: 8dB8t!c7bFHFnThYw
Postgres server DNS string: postgresql-00112.westus.cloudapp.azure.com
Postgres DB Name:  djangoblog
Github blog repository name: django-app (I think...)
New secret key: AFm+3p%t^6ZA5wJW+<6wMWu_-(W$biaeWyoq[y%:AT#+D?+(Xf
Database url: postgres://postgres:8dB8t!c7bFHFnThYw@postgresql-00112.westus.cloudapp.azure.com:5432/djangoblog