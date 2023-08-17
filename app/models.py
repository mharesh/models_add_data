from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField()
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Empno=models.IntegerField(unique=True,primary_key=True)
    Ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    Hiredate=models.DateField()
    Comm=models.IntegerField(null=True)


    def __str__(self):
        return self.Ename