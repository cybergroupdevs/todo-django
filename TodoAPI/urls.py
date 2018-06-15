from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from TodoAPI import views

urlpatterns = {
  url(r'^$', views.index, name="index"),
  url(r'^todos/$', views.TodoList.as_view(), name="todo-list"),
  url(r'^todos/(?P<pk>[0-9]+)/$',
      views.TodoDetail.as_view(), name="todo-details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)