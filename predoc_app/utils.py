def generate_primary_key_personal_details(tablename, conn, curr):
    curr.execute(f'SELECT COUNT(*) FROM {str(tablename)};')
    count = curr.fetchone()

    if tablename == 'personal_details':
        primary_key = f'PD{count[0]+1}'

    elif tablename == 'lifestyle':
        primary_key = f'LS{count[0]+1}'

    elif tablename == 'medical_history':
        primary_key = f'MD{count[0]+1}'

    elif tablename == 'allergies':
        primary_key = f'AL{count[0]+1}'

    elif tablename == 'current_medication_details':
        primary_key = f'CM{count[0]+1}'

    elif tablename == 'report':
        primary_key = f'RP{count[0]+1}'

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
