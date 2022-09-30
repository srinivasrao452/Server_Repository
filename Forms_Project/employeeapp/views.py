
from django.shortcuts import render
from employeeapp.models import Employee
from employeeapp.forms import Employee_Form, Employee_ModelForm

from django.http import HttpResponse 

def Employee_Form_View(request):
	if request.method == 'POST':
		form = Employee_Form(request.POST)

		if form.is_valid():
			eno = request.POST.get('eno')
			ename = request.POST.get('ename')
			salary = request.POST.get('salary')
			address = request.POST.get('address')

			emp = Employee(
				eno=eno,
				ename=ename,
				salary=salary,
				address=address
			)

			emp.save() # data stores into database

			return HttpResponse('form data saved into database successfully!')

		else:
			return HttpResponse('form data not saved into database successfully!')

	else:
		form = Employee_Form()
		context = {
           'form' : form
		}
		return render(request, 'employee_form.html', context)


def Employee_ModelForm_View(request):
	if request.method == 'POST':
		 form = Employee_ModelForm(request.POST)

		 if form.is_valid():
		 	form.save()
		 	return HttpResponse('ModelForm data  saved into database successfully!')

		 else:
		 	return HttpResponse('ModelForm data not saved into database successfully!')
 

	else:
		form = Employee_ModelForm()
		context = {
		   "form" : form
		}
		return render(request, 'employee_modelform.html', context)

