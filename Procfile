release: python manage.py migrate
web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn standbyWebserver.wsgi --log-file -
worker: python manage.py rqworker default
scheduler: python manage.py rqscheduler --queue default
