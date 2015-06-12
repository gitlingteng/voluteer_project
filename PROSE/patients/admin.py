from patients.models import Patient
from patients.models import Diagnosis
from django.contrib import admin


class PatientAdmin(admin.ModelAdmin):
    list_display = ('mrn', 'name_last','name_first')
    
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('name', 'accepted_status')


admin.site.register(Patient,PatientAdmin)
admin.site.register(Diagnosis,DiagnosisAdmin)
