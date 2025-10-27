import os
from dotenv import load_dotenv
import psycopg2
from pymongo import MongoClient

load_dotenv()

def generate_primary_key_SQL(tablename, conn, curr):
    curr.execute(f'SELECT COUNT(*) FROM {str(tablename)};')
    count = curr.fetchone()

    if tablename == 'personal_details':
        primary_key = f'PD{count[0]+1}'

    elif tablename == 'lifestyle':
        primary_key = f'LS{count[0]+1}'

    elif tablename == 'medical_history':
        primary_key = f'MD{count[0]+1}'

    elif tablename == 'report':
        primary_key = f'RP{count[0]+1}'

    elif tablename == 'accidents':
        primary_key = f'AI{count[0]+1}'

    return primary_key


def generate_primary_key_Mongo(collectionName, db):
    counting = db[collectionName].count_documents({}) + 1

    if collectionName == 'allergy':
        primary_key = f'AL{counting}'

    elif collectionName == 'medication':
        primary_key = f'MD{counting}'

    elif collectionName == 'accidents':
        primary_key = f'AC{counting}'

    return primary_key



def gender_code(gender):
    if gender.lower() == 'male':
        return 'M'
    elif gender.lower() == 'female':
        return 'F'
    else:
        return 'O'



def height_converter(height:str):
    ft, inch = height.split(" ")
    height_cm = (int(ft[0]) * 30.48) + (int(inch[0:-2]) * 2.54)
    return height_cm



def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def clear_country_code_input(value):
    return value.strip().strip("'")


def connectDb():
    host = os.getenv('DB_HOST')
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')

    conn = psycopg2.connect(host = host,
                        dbname = dbname,
                        user = user,
                        password = password,
                        port = port)

    curr = conn.cursor()

    return (conn, curr)

def connectMongoDB():
    client = MongoClient('mongodb://localhost:27017')
    db = client['predoc_no_sql_db']
    return db


def generate_primary_key_dermat(tablename, conn, curr):
    curr.execute(f'SELECT COUNT(*) FROM {str(tablename)};')
    count = curr.fetchone()

    if tablename == 'dermat_symptom_description':
        primary_key = f'SD{count[0]+1}'

    elif tablename == 'dermat_medical_lifestyle':
        primary_key = f'ML{count[0]+1}'

    elif tablename == 'dermat_severity':
        primary_key = f'SD{count[0]+1}'

    elif tablename == 'dermat_habits_hygiene':
        primary_key = f'HD{count[0]+1}'

    return primary_key

def generate_primary_key_oral(tablename, conn, curr):
    curr.execute(f'SELECT COUNT(*) FROM {str(tablename)};')
    count = curr.fetchone()

    if tablename == 'oral_symptom_description':
        primary_key = f'SO{count[0]+1}'

    elif tablename == 'oral_medical_lifestyle':
        primary_key = f'MO{count[0]+1}'

    elif tablename == 'oral_severity':
        primary_key = f'SO{count[0]+1}'

    elif tablename == 'oral_habits_hygiene':
        primary_key = f'HO{count[0]+1}'

    return primary_key


def generate_primary_key_pictures(tablename, conn, curr):
    curr.execute(f'SELECT COUNT(*) FROM {str(tablename)};')
    count = curr.fetchone()

    return f'IM{count[0]+1}'
