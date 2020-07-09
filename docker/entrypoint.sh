#!/bin/bash
set -e

case $1 in
    supervisor)
        python3.6 manage.py compress --extension=.haml --force
        python3.6 docker/clear-compressor-cache.py
        python3.6 manage.py migrate --noinput
        cat docker/nginx.conf > /etc/nginx/sites-enabled/nginx.conf
        cp -R /rapidpro/node_modules/@geocart/flow-editor/build/static/* /rapidpro/sitestatic/static/
        /usr/local/bin/supervisord -n -c docker/supervisor-app.conf
    ;;

esac

exec "$@"