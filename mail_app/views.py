from django.views.generic import TemplateView

from mail_app.models import *


# Create your views here.


class HomeView(TemplateView):
    template_name = 'mail_app/base1.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mail_all'] = MailingSettings.objects.all().count()
        context_data['count_mail_active'] = MailingSettings.objects.filter(mailing_status__in=['started']).count()
        context_data['count_clients'] = Client.objects.distinct().count()
        # context_data['blog'] = Blog.objects.filter(is_published=True).order_by('?')[:3]
        # context_data['user'] = self.request.user
        return context_data
