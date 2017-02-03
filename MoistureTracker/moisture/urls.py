from django.conf.urls import url

from views import HomepageView, MoistureChartView

app_name = 'moisture'
urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^moisture/$', MoistureChartView.as_view(), name='moisture_chart'),
]