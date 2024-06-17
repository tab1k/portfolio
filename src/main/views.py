from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from me import settings
from .forms import ContactForm
from django.core.mail import send_mail
from .mixins import *

app_name = 'main'


class HomePageView(AjaxableResponseMixin, RedirectAuthenticatedUserMixin, TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        pass


class ResumePageView(AjaxableResponseMixin, RedirectAuthenticatedUserMixin, TemplateView):
    template_name = 'main/resume.html'


class PortfolioPageView(AjaxableResponseMixin, RedirectAuthenticatedUserMixin, TemplateView):
    template_name = 'main/portfolio.html'


class ContactsPageView(AjaxableResponseMixin, FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        fullname = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Отправка письма
        subject = f'Сообщение от {fullname}'
        sender_email = settings.EMAIL_HOST_USER
        recipient_list = [sender_email]  # Ваш адрес электронной почты
        message_body = f'Имя: {fullname}\n\nПочта отправителя: {email}\n\nСообщение: {message}'

        send_mail(subject, message_body, sender_email, recipient_list)

        # Возвращаем ответ пользователю после отправки
        return super().form_valid(form)

