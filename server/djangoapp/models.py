from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=500)
    description = models.CharField(null=False, max_length=1024)

    def __str__(self):
        return 'Cake Make ' + self.name + ':\n' + \
                'Description: ' + self.description + '\n'


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=500)
    dealer_id = models.IntegerField(null=True)
    model_type = models.CharField(null=True, max_length=20)
    year = models.DateField(null=True)

    def __str__(self):
        return 'Car Model ' + self.name + ': \n' + \
               'Make: ' + self.make.name + '\n' + \
               'Dealer ID: ' + str(self.dealer_id) + '\n' + \
               'Model Type: ' + self.model_type + '\n' +  \
               'Year: ' + str(self.year) + '\n'

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, id, full_name, short_name, city, address, state, st, zip, lat, long):
        self.id = id
        self.full_name = full_name
        self.short_name = short_name
        self.city = city
        self.address = address
        self.state = state
        self.st = st
        self.zip = zip
        self.lat = lat
        self.long = long

    def __str__(self):
        return 'Dealer Name: ' + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, id, car_make, car_model, car_year, dealership, name, purchase, purchase_date, review, sentiment):
         self.id = id
         self.car_make = car_make
         self.car_model = car_model
         self.car_year = car_year
         self.dealership = dealership
         self.name = name
         self.purchase = purchase
         self.purchase_date = purchase_date
         self.review = review
         self.sentiment = sentiment

    def __str__(self):
        return 'Review name ' + self.name