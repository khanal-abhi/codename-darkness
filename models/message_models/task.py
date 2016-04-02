from protorpc import messages


class Task(messages.Message):
    name = messages.StringField(1, required=True)
    owner = messages.StringField(2)
