from django.core.validators import *
from django.db import models
from django.contrib.auth.models import User
import auth.models 
import datetime
import reversion

# Create your models here.

class Patient(models.Model):
    TRANSPLANT_CHOICES = {
       0:"None",
       1:"Auto",
       2:"Allo"                      
    }
    # Gathered from http://snipplr.com/view/4794/
    LANGUAGE_CHOICES = {
       0:"Amharic",
       1:"Arabic",
       2:"Armenian",
       3:"Bengali",
       4:"Cajun",
       5:"Chinese",
       6:"Croatian",
       7:"Czech",
       8:"Danish",
       9:"Dutch",
       10:"English",
       11:"Finnish",
       12:"Formosan",
       13:"French",
       14:"French Creole",
       15:"German",
       16:"Greek",
       17:"Gujarathi",
       18:"Hebrew",
       19:"Hindi (urdu)",
       20:"Hungarian",
       21:"Ilocano",
       22:"Italian",
       23:"Japanese",
       24:"Korean",
       25:"Kru",
       26:"Lithuanian",
       27:"Malayalam",
       28:"Miao (hmong)",
       29:"Mon-khmer (cambodian)",
       30:"Navaho",
       31:"Norwegian",
       32:"Panjabi",
       33:"Pennsylvania Dutch",
       34:"Persian",
       35:"Polish",
       36:"Portuguese",
       37:"Rumanian",
       38:"Russian",
       39:"Samoan",
       40:"Serbocroatian",
       41:"Slovak",
       42:"Spanish",
       43:"Swedish",
       44:"Syriac",
       45:"Tagalog",
       46:"Thai (laotian)",
       47:"Turkish",
       48:"Ukrainian",
       49:"Vietnamese",
       50:"Yiddish"
    }
        
    CLINIC_DAY_CHOICES = {
           0:"Monday",
           1:"Tuesday",
           2:"Wednesday",
           3:"Thursday",
           4:"Friday",
    
    }
    
    name_last = models.CharField('Last Name', max_length = 50)
    name_first = models.CharField('First Name', max_length = 50)
    name = models.CharField(max_length = 101, blank = True, null = True)
    dob = models.DateField('Date of Birth')
    dod = models.DateField('Date of Death', blank = True, null = True)
    mrn = models.CharField('MRN', max_length = 7, validators = [RegexValidator("[0-9]{7}", "Enter a valid MRN (Must be a 7 digit number)")])
    transplant = models.IntegerField(choices = TRANSPLANT_CHOICES.iteritems(), blank = True, null = True)
    dot = models.DateField('Date of Transplant', blank = True, null = True)
    diagnosis = models.ForeignKey('Diagnosis', blank = True, null = True)
    language = models.IntegerField(choices = LANGUAGE_CHOICES.iteritems(), blank = True, null = True)
    clinic_day = models.IntegerField(choices = CLINIC_DAY_CHOICES.iteritems(), blank = True, null = True)
    attendings = models.ManyToManyField(User, verbose_name = 'Attending(s)', limit_choices_to = {'userprofile__role': auth.models.get_role_index('Attending')}, related_name = 'attendings', blank = True, null = True)
    fellows = models.ManyToManyField(User, verbose_name = 'Fellow(s)', limit_choices_to = {'userprofile__role': auth.models.get_role_index('Fellow')}, related_name = 'fellows', blank = True, null = True)
    nps = models.ManyToManyField(User, verbose_name = 'Nurse Practitioner(s)', limit_choices_to = {'userprofile__role': auth.models.get_role_index('NP')}, related_name = 'nps', blank = True, null = True)
    ppus = models.ManyToManyField(User, verbose_name = 'Psychosocial Provider(s)', limit_choices_to = {'userprofile__role': auth.models.get_role_index('PPUS')}, related_name = 'ppus', blank = True, null = True)
    created = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name = 'creator')
    modified = models.DateTimeField(blank = True, null = True)
    modified_by = models.ForeignKey(User, related_name = 'modifier', blank = True, null = True)
    
    def __unicode__(self):
        return "%s: %s" % (self.mrn, self.name)
    
    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        
        self.modified = datetime.datetime.today()
        self.name = self.name_first + " " + self.name_last
        super(Patient, self).save()
        
    def get_providers(self):
        return self.attendings.all() | self.fellows.all() | self.nps.all() | self.ppus.all()
   
reversion.register(Patient)

class Diagnosis(models.Model):
    name = models.CharField('Diagnosis', max_length = 120, unique = True)
    accepted_status = models.BooleanField(default = False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

    
