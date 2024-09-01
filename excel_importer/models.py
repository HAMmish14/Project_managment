from django.db import models

class Phase1(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    criteria_a = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_b = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_c = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_d = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_e = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_f = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.usn}'
    
class Phase2(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    criteria_a = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_b = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_c = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_d = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_e = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.usn}'
    
class Phase3(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    criteria_a = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_b = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_c = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_d = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_e = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.usn}'
    
class Phase4(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    criteria_a = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_b = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_c = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_d = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_e = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_f = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.usn}'

class Phase5(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    criteria_a = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_b = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_c = models.DecimalField(max_digits=5, decimal_places=2)
    criteria_d = models.DecimalField(max_digits=5, decimal_places=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.usn}'
    
class Criteria1(models.Model):
    criteria_id = models.IntegerField(primary_key=True)
    phase_number = models.IntegerField()
    criteria_name = models.CharField(max_length=255)
    description = models.TextField()
    max_marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.criteria_name} (Phase {self.phase_number})'

# Create your models here.
