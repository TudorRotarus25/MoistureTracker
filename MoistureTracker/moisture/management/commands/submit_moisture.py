from moisture.models import MoistureAndTemperatureReport
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        temperature, moisture_level = 27.4, 55.5

        report = MoistureAndTemperatureReport.objects.create(temperature=temperature, moisture_level=moisture_level)
        report.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed report with id: "%d"' % report.id))
