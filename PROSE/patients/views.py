from django.shortcuts import render_to_response
from patients.forms import PatientForm, PatientEditForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from patients.models import Patient
from django.contrib.auth.decorators import login_required

def get_patient_list(request):
    return Patient.objects.all()

def patient_list(request, template = 'patients/patients.html'):
    patients = get_patient_list(request)
    return render_to_response(template, {'patients': patients}, context_instance = RequestContext(request))

@login_required()
def add (request, template = 'patients/patients_add.html'):
    if request.method == 'POST':
        pk = save_add_user(request)

        return HttpResponseRedirect(reverse('patients.views.patient_list'))
    else:
        patientForm = PatientForm()

    return render_to_response(template, {
        'patientForm': patientForm
        }, context_instance = RequestContext(request))

@login_required()
def edit (request, pk, template = 'patients/patients_edit.html', as_string = False):
    pt = Patient.objects.get(pk = pk)
    if request.method == 'POST':  
        patientForm = PatientEditForm(request.POST, instance = pt) # A form bound to the POST data
        if patientForm.is_valid(): 
            #Compare fields in patient form, if different save and change modified by field
            if patientForm.changed_data:
                pf = patientForm.save(commit = False)
                pf.modified_by = request.user
                pf.save()
                patientForm.save_m2m()
            return HttpResponseRedirect(reverse('patients.views.patient_list'))     
    #show existing by pk reference
    else:
        patientForm = PatientEditForm(instance = pt)

    if not as_string:
        return render_to_response(template, {
                     'patient': pt, 'patientForm': patientForm,
                }, context_instance = RequestContext(request)) 
    else:
        return render_to_string(template, {
                     'patient': pt, 'patientForm': patientForm,
                }, context_instance = RequestContext(request)) 
