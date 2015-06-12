from django.forms import ModelForm
from django import forms
from patients.models import Patient, Diagnosis

def _shared_validation_(dob = None, dod = None, dot = None):
        validation_errors = []
        if dob and dod:
            # Only do something if both fields are valid so far.
            if dob > dod:
                validation_errors.append("Date of Birth can't occur after Date of Death")
        if dot and dod:      
            if dot > dod:
                validation_errors.append("Date of Transplant can't occur after Date of Death")
        if dot and dob:   
            if dot < dob:
                validation_errors.append("Date of Transplant can't occur before Date of Birth")
        
        return validation_errors
    
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ('created_by', 'created', 'name', 'modified', 'modified_by')
        widgets = {
                  'dob': forms.widgets.DateInput(attrs = {'class':'calendar'}),
                  'dod': forms.widgets.DateInput(attrs = {'class':'calendar'}),
                  'dot': forms.widgets.DateInput(attrs = {'class':'calendar'}),
        }
        
    required_css_class = "required"
    error_css_class = "error"

        
    def clean(self):
        cleaned_data = self.cleaned_data
        dob = cleaned_data.get("dob")
        dod = cleaned_data.get("dod")
        dot = cleaned_data.get("dot")
        mrn = cleaned_data.get("mrn")
        transplant = cleaned_data.get("transplant")
        
        validation_errors = (_shared_validation_(dob, dod, dot))
        
        if Patient.objects.filter(mrn = mrn):
            validation_errors.append("The MRN you entered already exists - Please enter another")
        
        if dot:
            if not transplant: 
                validation_errors.append("There has to be a transplant in order to have a date of transplant")
        
        if validation_errors:
            raise forms.ValidationError(validation_errors)
        # Always return the full collection of cleaned data.
        return cleaned_data 

class PatientEditForm(PatientForm):
    class Meta(PatientForm.Meta):
        exclude = ('mrn', 'created', 'created_by', 'modified', 'modified_by', 'name_first', 'name_last', 'name', 'dob')
      
    def clean(self):
        cleaned_data = self.cleaned_data
        dob = cleaned_data.get("dob")
        dod = cleaned_data.get("dod")
        dot = cleaned_data.get("dot")

        if dob == None:
            dob = self.instance.dob
            
        if dod == None:
            dod = self.instance.dod
        
        if dot == None:
            dot = self.instance.dot
        
        validation_errors = (_shared_validation_(dob, dod, dot))

        if validation_errors:
            raise forms.ValidationError(validation_errors)
        # Always return the full collection of cleaned data.
        return cleaned_data 
                  
class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        exclude = ('accepted_status')
    
    required_css_class = "required"
    error_css_class = "error"
        
        
