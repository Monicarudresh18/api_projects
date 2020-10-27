from django.shortcuts import render
from CRUDapp.models import Student
from django.http import HttpResponse
from django.views.generic import View
from CRUDapp.utils import is_data_json
import json
from CRUDapp.mixins import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from CRUDapp.forms import StudentForm


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCompleteCRUDusingCbv(MixinHttpResponse,SerializeMixin,View):
	#getting/fetching the information from the existing data
	def get_object_data_by_id(self, id):
		try:
			stu = Student.objects.get(id = id)
		except Student.DoesNotExist:
			stu = None
		return stu
	def get(self, request, *args, **kwargs):
		data = request.body
		#checking whether the data is json or not
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json_data = json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)
		#converting json data into dict
		provided_data = json.loads(data)
		id = provided_data.get('id', None)
		if id is not None:
			stu = self.get_object_data_by_id(id)
			if stu is None:
				json_data = json.dumps({'msg':'the required source is not available'})
				return self.render_to_http_response(json_data, status=404)
			json_data = self.serialize([stu,])
			return self.render_to_http_response(json_data)
		#if the id is None
		query_string = Student.objects.all()
		json_data = self.serialize(query_string)
		return self.render_to_http_response(json_data)

	#creating the resource using post()
	def post(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data, status=400)
		stu_data = json.loads(data)

		form = StudentForm(stu_data)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'resource created successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status=400)

	#updating the data
	def put(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data, status=400)
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is None:
			json.dumps({'msg':'please provide the id, id is mandatory inorder to update'})
			return self.render_to_http_response(json_data, status=400)

		stu = self.get_object_data_by_id(id)

		if stu is None:
			json_data = json.dumps({'msg':'the required source is not available'})
			return self.render_to_http_response(json_data, status=404)

		original_data = {'student_name':stu.student_name,'student_mail':stu.student_mail,'student_phoneno':stu.student_phoneno,'student_address':stu.student_address}

		print('data before updation')
		print(original_data)

		print('data after updation')
		original_data.update(provided_data)
		print(original_data)

		form = StudentForm(original_data, instance= stu)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'resource updated successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status=400)
	#deletion of data
	def delete(self,request,*args,**kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data, status=400)
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is not None:
			stu = self.get_object_data_by_id(id)
			if stu is None:
				json_data=json.dumps({'msg':'no matched resource found, deletion not possible'})
				return self.render_to_http_response(json_data, status=404)
			#if the data is getting deleted we need to get the status code and the deleted items n placed within tuple
			(status,deleted_item)=stu.delete()
			if status==1:
				json_data=json.dumps({'msg':'resource deleted successfully'})
				return self.render_to_http_response(json_data)
			json_data=json.dumps({'msg':'resource not deleted successfully'})
			return self.render_to_http_response(json_data)
		json_data=json.dumps({'msg':'please provide the id, id is mandatory inorder to perform deletion'})
		return self.render_to_http_response(json_data, status=400)

	def patch(self,request,*args,**kwargs):
		data = request.body
		valid_json_data = is_data_json(data)
		if not valid_json_data:
			json.dumps({'msg':'please send the valid json data'})
			return self.render_to_http_response(json_data, status=400)
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is None:
			json.dumps({'msg':'please provide the id, id is mandatory inorder to patch'})
			return self.render_to_http_response(json_data, status=400)

		stu = self.get_object_data_by_id(id)

		if stu is None:
			json_data = json.dumps({'msg':'the required source is not available'})
			return self.render_to_http_response(json_data, status=404)

		original_data = {'student_name':stu.student_name,'student_mail':stu.student_mail,'student_phoneno':stu.student_phoneno,'student_address':stu.student_address}

		print('data before patching')
		print(original_data)

		print('data after patching')
		original_data.update(provided_data)
		print(original_data)

		form = StudentForm(original_data, instance= stu)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'resource patched successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status=400)



