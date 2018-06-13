from rest_framework import serializers
from TodoAPI.models import Todo
 
class TodoSerializer(serializers.HyperlinkedModelSerializer):
  # user = serializers.ReadOnlyField(source='user.username')

  class Meta:
    model = Todo
    fields = ('text', 'done', 'id')
    # field = __all__
    extra_kwargs = {
      'url': {
          'view_name': 'todos:todo-detail',
      }
    }