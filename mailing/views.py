from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing


class HomeTemplateView(TemplateView):
    template_name = 'mailing/index.html'


class ClientCreateView(CreateView):
    """Контроллер страницы добавления нового клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home_page')


class ClientListView(ListView):
    """Контроллер страницы клиентов"""
    model = Client


class MessageCreateView(CreateView):
    """Контроллер страницы добавления нового клиента"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:home_page')


class MessageListView(ListView):
    """Контроллер страницы сообщений"""
    model = Message


class MailingCreateView(CreateView):
    """Контроллер страницы добавления нового клиента"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home_page')


class MailingListView(ListView):
    """Контроллер страницы сообщений"""
    model = Mailing
