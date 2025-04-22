from django.db import models

# Create your models here.

class PatientData(models.Model):
    age = models.IntegerField()
    gender = models.IntegerField()
    blood_pressure = models.IntegerField()
    cholesterol = models.IntegerField()
    heart_rate = models.IntegerField()
    quantum_pattern_feature = models.FloatField()
    prediction = models.IntegerField()  # 1 for heart disease, 0 for no heart disease

    def __str__(self):
        return f"Patient {self.id}: Prediction {self.prediction}"