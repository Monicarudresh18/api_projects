from django import forms
from CRUDapp.models import Student

class StudentForm(forms.ModelForm):
	#form validation
	def clean_student_name(self):
		input_name=self.cleaned_data['student_name']
		if len(input_name)<=3:
			raise forms.ValidationError('characters should not be less than or equal to 3')
		return input_name
	class Meta:
		model = Student
		fields = '__all__'


