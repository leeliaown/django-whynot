from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.conf import settings as st
# Create your models here.
class Engineer(models.Model):
    name = models.CharField(max_length=20)
    eng_id = models.CharField(max_length=50)
    created_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.name}"



class Task(models.Model):
    user = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    pm = models.ForeignKey(st.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    cr_date = models.DateField()
    project_name = models.CharField(max_length=200, blank=True)
    cr_description = models.CharField(max_length=100)
    cr_project_code = models.CharField(max_length=100)
    attendance_point = models.SmallIntegerField(
        choices=(
        (0, "Failed"),
        (1, "Okay"),
    )
    )
    result_point = models.SmallIntegerField(
        choices=(
        (0, "Failed"),
        (1, "Okay"),
    )   
    )

    def __str__(self):
        return f"{self.user} : {self.cr_description}  "

    



    