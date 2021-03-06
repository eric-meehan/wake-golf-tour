import csv

# Generated by Django 3.1.7 on 2021-04-05 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0003_add_golfer_city'),
    ]
    
    def add_city_data (apps, schema_editor):
        f = open("golfersInput.csv", "r")
        csvReader = csv.reader(f)
        golfers = list(csvReader)
        for each in golfers:
            for item in each:
                item.strip()
        f.close()
        Golfer = apps.get_model('golfer', 'Golfer')
        for name, bdate, city in golfers:
            golfer = Golfer.objects.get(golfer_name=name)
            golfer.golfer_city = city
            golfer.save()
            
    def remove_city_data(apps, schema_editor):
        Golfer = apps.get_model('golfer', 'Golfer')
        Golfer.objects.update(golfer_city = 'unknown')

    operations = [migrations.RunPython(add_city_data, reverse_code=remove_city_data)
    ]
