from django.urls import path
from forum import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.CommunitiesListView.as_view(), name='communities_view'),
    path('forum/<int:pk>', views.communities_view_board_topics, name='board_topics'),
    path('forum/<int:pk>/new', views.communities_view_new_topic, name='board_topics_new'),
    path('forum/<int:pk>/topics/<int:topic_pk>', views.MessageListView.as_view(), name='board_topic_message'),
    path('forum/<int:pk>/topics/<int:topic_pk>/reply', views.communities_view_topic_messages_reply, name='board_topic_message_reply'),
    path('forum/<int:pk>/topics/<int:topic_pk>/message/<int:message_pk>/edit', views.MessageUpdateView.as_view(), name='edit_message'),
    path('login', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
