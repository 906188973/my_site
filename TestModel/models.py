from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)


class course(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=20)
    cpno = models.ForeignKey('self', on_delete=models.SET_NULL
                             , null=True)
    ccredit = models.IntegerField()

    def __str__(self):
        return "{}".format(self.cname)

class student(models.Model):
    sno = models.CharField(max_length=9, primary_key=True)
    sname = models.CharField(max_length=10)
    ssex = models.CharField(max_length=2)
    sage = models.IntegerField()
    sdept = models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.sname)

class sc(models.Model):
    sno = models.ForeignKey("student", on_delete=models.CASCADE)
    cno = models.ForeignKey("course", on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return  "学号：{} 科目号：{} 成绩：{}".format(sno, cno, grade)