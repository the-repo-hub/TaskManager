from rest_framework.serializers import ModelSerializer

from tasks.models import Task, User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields =  ('id', 'username', 'email')

class TaskSerializer(ModelSerializer):

    executor = UserSerializer()

    class Meta:
        model = Task
        fields = '__all__'
