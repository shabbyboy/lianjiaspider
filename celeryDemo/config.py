from __future__ import absolute_import
from kombu import Exchange,Queue
#CELERY_RESULT_BACKEND = 'redis://:abc@192.168.0.101:6379/2'
BROKER_URL = 'redis://:abc@192.168.0.101:6379/1'

CELERY_QUEUES = (
    Queue("default",Exchange("default"),routing_key="default"),
    Queue("task_A",Exchange("task_A"),routing_key="task_a")
)

CELERY_ROUTES={
    'celeryDemo.tasks.spider':{"queue":"task_A","routing_key":"task_a"}
}