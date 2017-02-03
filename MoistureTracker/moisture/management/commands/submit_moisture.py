from moisture.models import MoistureAndTemperatureReport
from django.core.management.base import BaseCommand, CommandError
import Adafruit_DHT

class Command(BaseCommand):
    sensor = Adafruit_DHT.AM2302
    pin = 4

    def handle(self, *args, **options):
	humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

	if humidity is not None and temperature is not None:
		humidity = round(humidity, 2)
		temperature = round(temperature, 1)
    		report = MoistureAndTemperatureReport.objects.create(temperature=temperature, moisture_level=humidity)
        	report.save()
		self.stdout.write(self.style.SUCCESS('Successfully closed report with id: "%d"' % report.id))
	else:
    		self.stdout.write(self.style.ERROR('Failed to read from sensor'))

