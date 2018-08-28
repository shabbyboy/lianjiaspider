from __future__ import absolute_import
from celery import Celery

app=Celery('celeryDemo', include=['celeryDemo.tasks'])
app.config_from_object('celeryDemo.config')

if __name__ == '__main__':
    app.start()