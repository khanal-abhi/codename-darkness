#!/usr/bin/env python
#
from google.appengine.ext import endpoints
from protorpc import remote

from models.message_models.task import Task
from models.ndb_models import task


@endpoints.api(name='tasks', version='v1', description='A simple task api')
class TaskAPI(remote.service):
    """This is the main class for the api. The methods defined here that are
    decorated with the endpoints wrapper will be the endpoint methods."""
    @endpoints.method(Task, Task,
                      name='task',
                      path='task',
                      http_method='POST')
    def insert_task(self, request):
        task.Task(name=request.name, owner=request.owner).put()
        return request


Application = endpoints.api_server([TaskAPI], restricted=False)