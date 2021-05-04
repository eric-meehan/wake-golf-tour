from django.db import models

# Create your models here.
class GolfCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()
    
    def getParList(self):
        holes = Hole.objects.filter(hole_course_id = self.course_id)
        par_values = []
        for hole in holes:
            par_values.append(hole.hole_par)
        return par_values
    
    def __str__(self):
        return self.course_name

    class Meta:
        managed = False
        db_table = 'GolfCourse'
        verbose_name = "Golf Course"
        verbose_name_plural = "Golf Courses"


class Hole(models.Model):
    hole_id = models.AutoField(primary_key=True)
    hole_course = models.ForeignKey(GolfCourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()
    
    def __str__(self):
        return "{}, Hole {}, Par {}".format (self.hole_course.course_name,
                                             self.hole_number, self.hole_par)

    class Meta:
        managed = False
        db_table = 'Hole'
