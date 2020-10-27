import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resource(id=None):
	data={}
	if id is not None:
		data={'id':id}
	response = requests.get(BASE_URL+END_POINT, data=json.dumps(data))
	print(response.status_code)
	print(response.json())
# get_resource()


def create_resource():
	student_name = input('enter the student name:\t')
	student_mail = input('enter the email id:\t')
	student_phoneno = int(input('enter the phone number:\t'))
	student_address = input('enter the student address:\t')
	stu_data = {'student_name':student_name,'student_mail':student_mail,'student_phoneno':student_phoneno,'student_address':student_address}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(stu_data))
	print(response.status_code)
	print(response.json())
# create_resource()



def update_resource(id):
	update_data={'id':id,'student_address':'kgf'}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.status_code)
	print(response.json())
update_resource(1)


def delete_resource(id):
	data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)
delete_resource(1)

def patch_resource(id):
	patch_data = {'id':id,'student_mail':'dolly12345@gmail.com'}
	response = requests.patch(BASE_URL+END_POINT,data=json.dumps(patch_data))
	print(response.json())
	print(response.status_code)
patch_resource(1)

if __name__ == '__main__':
	while True:
		print('1. to CREATE the data')
		print('2. to SELECT the complete data')
		# print('3. to UPDATE the data completely')
		# print('4. to UPDATE the data partially')
		# print('5. to DELETE the data')
		select=int(input('select any one of them from 1, 2 :\t'))

		if select == 1:
			create_resource()
		elif select == 2:
			get_resource()
		elif select == 3:
		 	update_resource()
		elif select == 4:
		 	patch_resource(id)
		elif select == 5:
		 	delete_resource(id)
		else:
			print('please select any one of the option!!!')

