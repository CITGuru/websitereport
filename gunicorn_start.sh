#!/bin/bash

NAME="websitereport"                                   # Name of the application
DJANGODIR=/root/websitereportapp     
DJANGOENV=/root/venv-websitereportapp                  # Django project directory
SOCKFILE=/root/websitereportapp/gunicorn.sock          # we will communicte using this unix socket
USER=root                                        # the user to run as
GROUP=www-data                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=websitereport.settings.prod            # which settings file should Django use
DJANGO_WSGI_MODULE=websitereport.wsgi  

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $DJANGOENV/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $DJANGOENV/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-