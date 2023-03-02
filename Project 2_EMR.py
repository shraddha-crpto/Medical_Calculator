#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:54:05 2021

@author: shraddha_gupta
"""

from tkinter.constants import TRUE
import mysql.connector
from mysql.connector import errorcode
 
try:
    cnx = mysql.connector.connect(user= 'root', password= 'Healthcare@007', host='localhost', database='EHR')
except mysql.connector.Error as err:
    message = err.msg
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        message = "Something is wrong with your user name or password"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        message = "Database does not exist"
    
    print(message)
else:
    cursor = cnx.cursor()
    while(TRUE):
        print('Select Option: (Press 0 to terminate)')
        print('1. Patient Information')
        print('2. Seen by Doctor')
        print('3. Visit by Patient')
        print('4. Vist by Patient and Seen by Doctor')
        print('5. Look for icd9 description')
        inputInt = int(input())
       
        if inputInt == 0:
            break
        if inputInt == 1:
            p_name = input('Enter Patient Name: ')
            query = """
                select full_name, birth_date, gender, contact_num 
                from patient 
                where full_name like '%%%s%%'
                """ % (p_name)
            try:   
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err.msg)
            else: 
                print() 
                for (name, birth, gender, contact) in cursor:
                    print('Name:', name)
                    print('Date of Birth:', birth)
                    print('Gender:', gender)
                    print('Contact:', contact)
                    print()

        elif inputInt == 2:
            d_name = input('Enter Doctor Name: ')
            query = """
                select p.full_name, d.full_name, v.visitdate, cd.code, cd.description from visit as v
                join patient as p
                on p.patient_num = v.patient_num
                join doctor as d
                on d.doctor_id = v.doctor_id
                join icd9codes as cd
                on cd.code = v.icd_code
                where d.full_name like '%%%s%%'
                """ % (d_name)
            try:   
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err.msg)
            else: 
                print() 
                for (p_name, d_name, v_date, code, icddesc) in cursor:
                    print('Patient Name:', p_name)
                    print('Doctor Name:', d_name)
                    print('Visit Date:', v_date)
                    print('ICD Code:', code)
                    print('ICD Description:', icddesc)
                    print()
        elif inputInt == 3:
            p_name = input('Enter Patient Name: ')
            query = """
                select p.full_name, d.full_name, v.visitdate, cd.code, cd.description from visit as v
                join patient as p
                on p.patient_num = v.patient_num
                join doctor as d
                on d.doctor_id = v.doctor_id
                join icd9codes as cd
                on cd.code = v.icd_code
                where p.full_name like '%%%s%%'
                """ % (p_name)
            try:   
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err.msg)
            else: 
                print() 
                for (p_name, d_name, v_date, code, icddesc) in cursor:
                    print('Patient Name:', p_name)
                    print('Doctor Name:', d_name)
                    print('Visit Date:', v_date)
                    print('ICD Code:', code)
                    print('ICD Description:', icddesc)
                    print()
        elif inputInt == 4:
            p_name = input('Enter Patient Name: ')
            d_name = input('Enter Doctor Name: ')
            query = """
                select p.full_name, d.full_name, v.visitdate, cd.code, cd.description from visit as v
                join patient as p
                on p.patient_num = v.patient_num
                join doctor as d
                on d.doctor_id = v.doctor_id
                join icd9codes as cd
                on cd.code = v.icd_code
                where p.full_name like '%%%s%%' and d.full_name like '%%%s%%'
                """ % (p_name, d_name)
            try:   
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err.msg)
            else: 
                print() 
                for (p_name, d_name, v_date, code, icddesc) in cursor:
                    print('Patient Name:', p_name)
                    print('Doctor Name:', d_name)
                    print('Visit Date:', v_date)
                    print('ICD Code:', code)
                    print('ICD Description:', icddesc)
                    print()
            
        elif inputInt == 5:
            descrip = input('icd9 description: ')
            query = """
                select p.full_name, d.full_name, v.visitdate, cd.code, cd.description from visit as v
                join patient as p
                on p.patient_num = v.patient_num
                join doctor as d
                on d.doctor_id = v.doctor_id
                join icd9codes as cd
                on cd.code = v.icd_code
                where cd.description like '%%%s%%'
                """ % (descrip)
            try:   
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(err.msg)
            else: 
                print() 
                for (p_name, d_name, v_date, code, icddesc) in cursor:
                    print('Patient Name:', p_name)
                    print('Doctor Name:', d_name)
                    print('Visit Date:', v_date)
                    print('ICD Code:', code)
                    print('ICD Description:', icddesc)
                    print()
        else:
            print("Invalid")