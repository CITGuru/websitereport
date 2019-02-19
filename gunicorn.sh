NAME="websitereport"                                   # Name of the application
DJANGODIR=/root/websitereportapp                       # Django project directory
SOCKFILE=/root/websitereportapp/gunicorn.sock          # we will communicte using this unix socket
USER=root                                        # the user to run as
GROUP=www-data                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=websitereport.settings.base             # which settings file should Django use
DJANGO_WSGI_MODULE=websitereport.wsgi  