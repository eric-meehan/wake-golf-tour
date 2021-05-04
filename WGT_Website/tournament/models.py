from django.db import models
from golf_course.models import GolfCourse

# Create your models here.
class Tournament(models.Model):
    tourn_id = models.AutoField(primary_key=True)
    tourn_name = models.TextField()
    tourn_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    tourn_start_date = models.DateField()
    tourn_num_rounds = models.IntegerField()
    tourn_num_golfers = models.IntegerField()
    
    def __str__(self):
        return self.tourn_name


    class Meta:
        managed = False
        db_table = 'Tournament'


class Round(models.Model):
    round_id = models.AutoField(primary_key=True)
    round_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    round_day = models.TextField()
    
    def __str__(self):
        return ("{}".format (self.round_day))

    class Meta:
        managed = False
        db_table = 'Round'
