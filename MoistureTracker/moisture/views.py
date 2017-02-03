from django.db.models import Max
from django.views.generic.base import TemplateView
from models import MoistureAndTemperatureReport
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.views.generic.detail import DetailView


class LayoutView(View):
    def get_most_recent_report(self):
        max_date = MoistureAndTemperatureReport.objects.values('temperature').aggregate(max=Max('reported_at'))['max']
        return MoistureAndTemperatureReport.objects.filter(reported_at=max_date).first()


class HomepageView(LayoutView):
    template_name = 'moisture/homepage.html'

    def get(self, request):
        context = {}
        context['last_report'] = self.get_most_recent_report()
        return render(request, self.template_name, {'latest_report': self.get_most_recent_report()})


class MoistureChartView(LayoutView):
    template_name = 'moisture/moisture_chart.html'

    def get(self, request):
        return render(request, self.template_name, {})
