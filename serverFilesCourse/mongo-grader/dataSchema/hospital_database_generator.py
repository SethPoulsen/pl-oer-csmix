from dataSchema.random_generator import get_random_fullNames, get_random_medicine, get_random_roomID, get_random_company, get_random_country
from random import randint, choice
from os import system
import json

class MDBHospitalGenerator():
    mdb_js_path = '/grade/tests/setup-hospital.js'
    
    def __init__(self):
        self.patient_name = get_random_fullNames(80)
        self.doctor_name = get_random_fullNames(50)
        self.contact_name = get_random_fullNames(80)
        self.medicine_name = get_random_medicine(70)
        self.rids = get_random_roomID(randint(20,40))
        self.oids = get_random_roomID(randint(20,40), digit=2)
        self.company_name = get_random_company(20)
        self.country = get_random_country(10)

        self.patients = []
        self.doctors = []
        self.medicine = []
        self.wards = []

        # this should become a constraint function
        self.doctor_name += ["Ti-Chung Cheng", "Abdu Alawini", "Blair Huang", "Sophia Yang", "Sunny Lin", "Jamie Chen", "Jo Lin"]
        self.country += ["Canada", "United Kingdom", "Canada", "United Kingdom"]

    def set_up_database(self):
        file = open(self.mdb_js_path, 'w')
        file.write('db.Medicine.deleteMany({});\n')
        file.write('db.Patients.deleteMany({});\n')
        file.write('db.Wards.deleteMany({});\n')
        file.write('db.Doctors.deleteMany({});\n')

        # create wards first
        for rid in self.rids:
            ward = {
                "ward_id": rid,
                "num_of_beds": randint(1, 8),
                "floor": randint(2, 10),
                "bathroom": randint(1, 3),
                "thermometer": randint(0, 4),
                "ventilator": randint(0, 4)
            }
            self.wards.append(ward)

        for ward in self.wards:
            insert = ''.join(['db.Wards.insert(', str(ward), ");\n"])
            file.write(insert)
            # print(insert, end="")

        # create medicines
        for idx, med in enumerate(self.medicine_name):
            medicine = {
                "med_id": idx,
                "name": med,
                "prod_year": randint(1970, 2022),
                "prod_country": choice(self.country),
                "reviews": randint(10, 100)/10,
                "prod_company": {
                    "company_name": choice(self.company_name),
                    "company_country": choice(self.country),
                    "company_founded": randint(1950, 2010)
                }
            }
            self.medicine.append(medicine)
        
        for med in self.medicine:
            insert = ''.join(['db.Medicine.insert(', str(med), ");\n"])
            file.write(insert)
            # print(insert, end="")

        # create doctors
        for idx, doctor_name in enumerate(self.doctor_name):
            birth = randint(1970, 2000)
            doctor = {
                "doc_id": idx,
                "doc_name": doctor_name,
                "doc_birth": birth,
                "service_length": choice(range(1, 10)),
                "resp_wards": list(set([choice(self.wards)['ward_id'] for _ in range(randint(1,7))])),
                "office": choice(self.oids),
                "salary": randint(90, 155)*1000
            }
            self.doctors.append(doctor)

        for doc in self.doctors:
            insert = ''.join(['db.Doctors.insert(', str(doc), ");\n"])
            file.write(insert)
            # print(insert, end="")

        # create patients
        for idx, p_name in enumerate(self.patient_name):

            patient = {
                "pid": idx,
                "name": p_name,
                "days_admit": randint(1, 200),
                "birth_year": randint(1940, 2020),
                "birth_country": choice(self.country),
                "wards": choice(self.wards)['ward_id'],
                "medicine": list(set([choice(self.medicine)['med_id'] for _ in range(randint(1,5))])),
                "doctors": list(set([choice(self.doctors)['doc_id'] for _ in range(randint(1,3))])),
                "contact": {
                    "name": self.contact_name[idx],
                    "phone": randint(111111111, 999999999)
                }
            }

            self.patients.append(patient)

        for pat in self.patients:
            insert = ''.join(['db.Patients.insert(', str(pat), ");\n"])
            file.write(insert)
            # print(insert, end="")


    def inject_mongodb_data(self):
        """injects generated mdb js into db"""
        system("mongo --quiet " + self.mdb_js_path)
        system('echo "Injected Data into MongoDB Database"')