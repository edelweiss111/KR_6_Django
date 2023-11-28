from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing


class HomeTemplateView(TemplateView):
    """Контроллер главной страницы"""
    template_name = 'mailing/index.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер страницы добавления нового клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home_page')

    def form_valid(self, form):
        """Добавление пользователя к клиенту"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер страницы клиентов"""
    model = Client

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


class ClientUpdateView(UpdateView):
    """Контроллер страницы редактирования клиентов"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(DeleteView):
    """Контроллер удаления клиента"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер страницы добавления нового сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        """Добавление пользователя к сообщению"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    """Контроллер страницы редактирования сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(DeleteView):
    """Контроллер страницы удаления сообщения"""
    model = Message
    success_url = reverse_lazy('mailing:home_page')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер страницы сообщений"""
    model = Message

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер страницы добавления новой рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home_page')

    def form_valid(self, form):
        """Добавление пользователя к рассылке"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    """Контроллер страницы редактирования рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MailingDeleteView(DeleteView):
    """Контроллер страницы удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер страницы рассылок"""
    model = Mailing

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


def status_mailing(request, pk):
    """Контроллер смены статуса рассылки"""
    mailing = Mailing.objects.get(pk=pk)
    if request.user == mailing.user:
        if mailing.status == 'created':
            mailing.status = 'completed'
            mailing.save()
        elif mailing.status == 'completed':
            mailing.status = 'created'
            mailing.save()
    return redirect(reverse('mailing:mailing_list'))
