from django.contrib import admin

# Register your models here.
from .models import PatientData

@admin.register(PatientData)
class PatientDataAdmin(admin.ModelAdmin):
    list_display = ('id','age','gender','blood_pressure','cholesterol','heart_rate','quantum_pattern_feature','prediction')