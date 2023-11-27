from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing


class HomeTemplateView(TemplateView):
    """Контроллер главной страницы"""
    template_name = 'mailing/index.html'


class ClientCreateView(CreateView):
    """Контроллер страницы добавления нового клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home_page')


class ClientListView(ListView):
    """Контроллер страницы клиентов"""
    model = Client


class ClientUpdateView(UpdateView):
    """Контроллер страницы редактирования клиентов"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    """Контроллер удаления клиента"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageCreateView(CreateView):
    """Контроллер страницы добавления нового сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    """Контроллер страницы редактирования сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    """Контроллер страницы удаления сообщения"""
    model = Message
    success_url = reverse_lazy('mailing:home_page')


class MessageListView(ListView):
    """Контроллер страницы сообщений"""
    model = Message


class MailingCreateView(CreateView):
    """Контроллер страницы добавления новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home_page')


class MailingUpdateView(UpdateView):
    """Контроллер страницы редактирования рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    """Контроллер страницы удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingListView(ListView):
    """Контроллер страницы рассылок"""
    model = Mailing
