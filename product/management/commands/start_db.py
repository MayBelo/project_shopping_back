from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
class Command(BaseCommand):
   help = 'Closes the specified poll for voting'


#    def add_arguments(self, parser):
#        parser.add_argument('car_id', nargs='+', type=int)


   def handle(self, *args, **options):
    #    print("these are the arguments got:")
    #    print(args, options)
    #    car_ids = options.get('car_id')
    #    print(type(car_ids))
    #    if car_ids[0] != 0:
    #        cars = [Car.objects.get(pk=car_ids[0])]
        users = User.objects.all()
        for user in users:
            print(user)
