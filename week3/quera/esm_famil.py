import csv
from csv import DictWriter
data=[]
def ready_up():
    with open("esm_famil_data.csv",'r', encoding='utf8') as f:
        data = f.readlines()
    
# def add_participant(**kwargs):
#     add_data = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'}
#     schoolname  = add_data['school']
#     cityname = add_data['city']
#     standard = add_data['class']
#     studentname = add_data['name']

answers = {'participant':'salib','esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 
    'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'}
def add_participant( answers):
	
	field_names = ['participant','esm','famil','keshvar',
			'rang','ashia','ghaza']

	

	with open('answers.csv', 'a') as f_object:
		dictwriter_object = DictWriter(f_object, fieldnames=field_names)
		dictwriter_object.writerow(answers)
	
    	 

def calculate_all():
	
	with open('answers.csv','r') as f_answear:
		data_answear=f_answear.readlines()
		for i in data_answear:
			if i in data:
				if i not in data_answear:


ready_up()
add_participant( answers)