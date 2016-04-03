#!/usr/bin/env python
#
from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import remote
from protorpc import messages
from protorpc import message_types


class Task(messages.Message):
    name = messages.StringField(1, required=True)
    owner = messages.StringField(2)


class TaskModel(ndb.Model):
    name = ndb.StringProperty(required=True)
    owner = ndb.StringProperty()


class Tasks(messages.Message):
    items = messages.MessageField(Task, 1, repeated=True)


@endpoints.api(name='tasks', version='v1', description='A simple task api')
class TaskAPI(remote.Service):
    """This is the main class for the api. The methods defined here that are
    decorated with the endpoints wrapper will be the endpoint methods."""

    @endpoints.method(Task, Task,
                      name='task.insert',
                      path='task',
                      http_method='POST')
    def insert_task(self, request):
        # TaskModel(name=request.name, owner=request.owner).put()
        return request

    @endpoints.method(message_types.VoidMessage, Tasks,
                      name='task.list_tasks',
                      path='tasks',
                      http_method='GET')
    def list_tasks(self, unused_request):
        pass
        # tasks = []
        # queried_tasks = TaskModel.query()
        # for single_task in queried_tasks:
        #     tasks.append(single_task)
        #
        # return Tasks(items=tasks)


Application = endpoints.api_server([TaskAPI])
