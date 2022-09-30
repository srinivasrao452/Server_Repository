
####  forms.Form class ####

from django import forms 

class Employee_Form(forms.Form):
	eno     = forms.IntegerField()
	ename   = forms.CharField()
	salary  = forms.FloatField()
	address = forms.CharField()


#####  ModelForm Class ######

from employeeapp.models import Employee
#from django import forms

class Employee_ModelForm(forms.ModelForm):
	class Meta:
		models = Employee
		fields = '__all__'



