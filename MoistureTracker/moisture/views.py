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

    def get_last_reports(self):
        labels = []
        temperature = []
        moisture_level = []
        last_ten = MoistureAndTemperatureReport.objects.order_by('-reported_at')[:10]
        last_ten = last_ten.reverse()

        for report in last_ten:
            labels.append(report.reported_at.strftime('%H:%M'))
            temperature.append(report.temperature)
            moisture_level.append(report.moisture_level)

        return {'labels': labels, 'temperature': temperature, 'moisture_level': moisture_level}

    def get(self, request):
        context = {
            'latest_report': self.get_most_recent_report(),
            'report_chart_data': self.get_last_reports(),
        }
        return render(request, self.template_name, context)


class MoistureChartView(LayoutView):
    template_name = 'moisture/moisture_chart.html'

    def get(self, request):
        return render(request, self.template_name, {})
