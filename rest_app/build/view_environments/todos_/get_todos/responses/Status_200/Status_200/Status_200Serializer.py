from rest_framework import serializers
from rest_app.build.serializers.definitions.Todo.TodoSerializer import TodoSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = TodoSerializer()
