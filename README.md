# Python - Django - Proj1

## Setup virtual environment

```
python3 -m venv ./venv
```
 - activate environment
```
source ./venv/bin/activate
```
 - confirm environment success (should display latest Python)
```
python --version
```
 - test server works
```
python manage.py runserver
```
---

## Install Django
```
pip install django
```
 - confirm installed
```
django-admin help
```
 - create *'project'*
```
django-admin startproject NAME_OF_PROJECT .
```
 - verify by running the *manage.py* file
```
python manage.py help
```
---

## Create subsequent 'app' folders
```
python manage.py startapp NAME_OF_APP
```
 - for every new 'app' also add config to INSTALLED_APPS within {Project}/settings.py
```
INSTALLED_APPS = [
    '{NEW_APP_NAME}.apps.{NEW_APP_NAME}Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
---

## Create a templates folder for HTML
 - create the 'templates' folder in ROOT
 - in {PROJECT}/settings.py, update the TEMPLATES array field 'DIRS':
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
---

## Create a 'static' folder in {Project_Folder} for static content (css, js, fonts, etc.)

## in Project/settings.py, add extra static variables
 - command 'collectstatic' gathers each app's 'static' folder and combines them in a 'root' static folder
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'python_django_proj1/static')
]
```
---

## Install PostgreSQL via docker
```
docker pull postgres
```
 - run on port 5432
```
docker run -p 5432:5432 --name myPostgresDB -e POSTGRES_PASSWORD=narf -d postgres
```

## Install PGAdmin4 (PostgreSQL GUI Tool)
```
docker pull dpage/pgadmin4
```
 - run on port 5000
```
docker run -p 5000:80 --name pgadminApp -e 'PGADMIN_DEFAULT_EMAIL=user@domain.net' -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' -d dpage/pgadmin4
```
 - go to localhost:5000
 - in the left-sidebar, right-click 'Servers' -> Create -> Server
   - name it whatever
   - Connection:
     - Hostname/Address: the only thing that worked for me was to use the Mac's hostname 'CNC...', not 'localhost'
     - '-p HostPort:DockerAppPort', the HostPort is the port on your localhost which the program will run
     - Username defaults to 'postgres' and Password was specified in the docker command earlier
     - SAVE
---

## Setup Django for PostgreSQL
 - install psycopg2 and psycopg2-binary
```
pip install psycopg2 psycopg2-binary
```
 - within Project/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testDB',
        'USER': 'postgres',
        'PASSWORD': 'SuperSecret',
        'HOST': 'CNCL02TH18PG8WL', <!-- localhost didn't work for me -->
    }
}
```
 - stop the Django server first
 - run migrations
```
python manage.py migrate
```

### Create some models within an app
 - then update the database servers with the new migrations
```
python manage.py makemigrations
```

