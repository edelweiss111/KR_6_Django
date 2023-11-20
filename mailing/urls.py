from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomeTemplateView, ClientCreateView, MessageCreateView, MailingCreateView, ClientListView, \
    MessageListView, MailingListView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home_page'),
    path('add', ClientCreateView.as_view(), name='add_client'),
    path('create_message', MessageCreateView.as_view(), name='create_message'),
    path('create_mailing', MailingCreateView.as_view(), name='create_mailing'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('mailing_list', MailingListView.as_view(), name='mailing_list'),
]
