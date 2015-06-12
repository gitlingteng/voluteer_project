from models import Diagnosis

def get_approved_diagnosis_list():
    return Diagnosis.objects.filter(accepted_status = True)

def get_unapproved_diagnosis_list():
    return Diagnosis.objects.filter(accepted_status = False)

def save_add_patient(request):
    patientForm = PatientForm(request.POST) # A form bound to the POST data
    if patientForm.is_valid():
        pf = patientForm.save(commit = False)
        pf.created_by = request.user
        pf.save()
        patientForm.save_m2m()

    return pf
