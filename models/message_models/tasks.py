from protorpc import messages
from models.message_models import task


class Tasks(messages.Message):
    tasks = messages.MessageField(task.Task, 1, repeated=True)
