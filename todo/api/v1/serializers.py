from rest_framework import serializers
from todo.models import TodoModel


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     level = serializers.CharField()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['level', 'job', 'dead_end', 'is_done']
