print("Session 14 assignment")

import csv
from itertools import islice
from collections import namedtuple
from datetime import datetime
from typing import NamedTuple
    
def improved_iterator(filename,datatypes):
    "An iterator that opens the file and creates a generator to iterate over it"
    with open(filename) as file:
        filerows=csv.reader(file,delimiter=",",quotechar='"')
        file_tuple=namedtuple(filename.split(".")[0],next(filerows))
        for row in filerows:
            for x,y in zip(row,datatypes):
                if y=="STRING":
                    pass
                elif y=="INT":
                    x=int(x)
                elif y=="datetime":
                    x=datetime.strptime(x,"%Y-%m-%dT%H:%M:%SZ")
                elif y=="SSN":
                    x=int(x.replace("-",""))
            yield file_tuple(*row)

def convert_all_to_one(employment_tuple:NamedTuple,personal_info_tuple:NamedTuple,update_status_tuple:NamedTuple,vehicles_tuple:NamedTuple):
    "Combines all iterators into one iterator using a dictionary to remove repeated fields"
    temporary_dictionary={}
    tupleoftuples=(employment_tuple,update_status_tuple,vehicles_tuple)
    final_dictionary={}
    temporary_dictionary=personal_info_tuple._asdict()
    final_dictionary.update({**temporary_dictionary})
    for tup in tupleoftuples:
        temporary_dictionary=tup._asdict()
        temporary_dictionary.pop('ssn')
        final_dictionary.update({**temporary_dictionary})
    return_tuple=namedtuple('All_information',final_dictionary.keys())
    return return_tuple(**final_dictionary)
    
def get_all_tuples_into_one_iterator():
    "Combines all iterators into one iterator"
    employrows=improved_iterator('employment.csv',('STRING','STRING','SSN','SSN'))
    personalrows=improved_iterator('personal_info.csv',['SSN','STRING','STRING','STRING','STRING'])
    update_statusrows=improved_iterator('update_status.csv',['SSN','datetime','datetime'])
    vehiclesrows=improved_iterator('vehicles.csv',['SSN','STRING','STRING','INT'])
    for w,x,y,z in zip(employrows,personalrows,update_statusrows,vehiclesrows):
        yield convert_all_to_one(w,x,y,z)

rows=improved_iterator('personal_info.csv',['SSN','STRING','STRING','STRING','STRING'])



date_minimum=datetime.strptime('030117','%m%d%y')

def filter_stale_records_iterator():
    "Returns records which are later than 3/1/17"
    yield from filter(lambda x:datetime.strptime(x.last_updated,"%Y-%m-%dT%H:%M:%SZ")>date_minimum,get_all_tuples_into_one_iterator())
    
def return_dict_of_carmakers():
    "Returns a dictionary of the carmakes per gender"
    rows=get_all_tuples_into_one_iterator()
    male={}
    female={}
    for row in rows:
        if row.gender=='Male':
            dictionary_to_be_updated=male
        else:
            dictionary_to_be_updated=female
        count=dictionary_to_be_updated.get(row.vehicle_make,0)
        dictionary_to_be_updated.update({row.vehicle_make:count+1})
    return male,female

def return_highest_carmaker():
    "Returns a list of highest carmakers per gender."
    male,female=return_dict_of_carmakers()
    highestnumber=max(male.values())
    male_return_list=[]
    if tuple(male.values()).count(highestnumber)>1:
        for x,y in male.items():
            if y==highestnumber:
                male_return_list.append(x)
    else:
        male_return_list=[max(male,key=lambda x:male[x])]
    highestnumber=max(female.values())
    female_return_list=[]
    if tuple(female.values()).count(highestnumber)>1:
        for x,y in female.items():
            if y==highestnumber:
                female_return_list.append(x)
    else:
        female_return_list=[max(female,key=lambda x:female[x])]
    return male_return_list,female_return_list
print(return_highest_carmaker())