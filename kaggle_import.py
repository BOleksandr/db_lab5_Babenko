import csv
import psycopg2


username = 'Babenko'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE1 = 'cellphones data.csv'
INPUT_CSV_FILE2 = 'cellphones users.csv'
INPUT_CSV_FILE3 = 'cellphones ratings.csv'


query_0 = '''
delete from characteristic;
delete from rating;
delete from users;
delete from cellphone;
'''

query_1 ='''
insert into Cellphone(cellphone_id, brand, model) values (%s, %s, %s)
'''

query_2 ='''
insert into Characteristic(cellphone_id, os, internal_memory, ram, main_camera, selfie_camera, battery_size)
values (%s, %s, %s, %s, %s, %s, %s)
'''

query_3 ='''
insert into	Users(user_id, age, gender, profession) values (%s, %s, %s, %s)
'''

query_4 ='''
insert into Rating(user_id, cellphone_id, grade) values (%s, %s, %s)
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_0)
    
    with open(INPUT_CSV_FILE1, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            cellphone_id = int(row['cellphone_id'])
            values = (cellphone_id, row['brand'], row['model'])
            cur.execute(query_1, values)

    with open(INPUT_CSV_FILE1, 'r') as f:
        reader = csv.DictReader(f)
        name_colomn = ['cellphone_id', 'internal memory', 'RAM', 'main camera', 'selfie camera', 'battery size']
        for idx, row in enumerate(reader):
            values_int = [int(row[i]) for i in name_colomn]
            values = (values_int[0], row['operating system'], values_int[1], values_int[2],
                      values_int[3], values_int[4], values_int[5])
            cur.execute(query_2, values)

    with open(INPUT_CSV_FILE2, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            user_id = int(row['user_id'])
            age = int(row['age'])
            if row['gender'] == '-Select Gender-': 
                row['gender'] = None
            if row['occupation'].lower() == 'null':
                row['occupation'] = None

            values = (user_id, age, row['gender'], row['occupation'])    
            cur.execute(query_3, values)

    with open(INPUT_CSV_FILE3, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            cellphone_id = int(row['cellphone_id'])
            user_id = int(row['user_id'])
            grade = int(row['rating'])
            values = (user_id, cellphone_id, grade)
            cur.execute(query_4, values)

    conn.commit()
 

