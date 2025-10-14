from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['predoc_no_sql_db']

# Allergy Table
validators_allergy = {
    "bsonType": "object",
    "required": ["allergy_id", "user_id", "allergyStatus", 'created_at'],
    "properties": {
        "allergy_id": {
            "bsonType": "string",
            "description": "Should be integer and required"
        },
        "user_id": {
            "bsonType": "number",
            "description": "Should be string and required"
        },
        "allergyStatus": {
            "bsonType": "bool",
            "description": "Should be Boolean and required"
        },
        "created_at":{
            "bsonType": 'date',
            "description": 'should be date, required'
        },
        "allergy_details": {
            "bsonType": "array",
            "description": "Should be array of allergy objects",
            "items": {
                "bsonType": "object",
                "required": ["allergy_type", "allergy_name", "allergy_reaction"],
                "properties": {
                    "allergy_type": {
                        "bsonType": "string",
                        "description": "Type of allergy, required"
                    },
                    "allergy_name": {
                        "bsonType": "string",
                        "description": "Name of allergy, required"
                    },
                    "allergy_reaction": {
                        "bsonType": "string",
                        "description": "Reaction description, required"
                    }
                }
            }
        }
    }
}

db.create_collection(
    'allergy',
    validator = {
        "$jsonSchema": validators_allergy
    }
)


validators_medication = {
    "bsonType": "object",
    "required": ["medicationId", "user_id","medicationStatus", 'created_at'],
    "properties": {
        "medicationId": {
            "bsonType": "string",
            "description": "Should be integer and required"
        },
        "user_id": {
            "bsonType": "number",
            "description": "Should be string and required"
        },
        "medicationStatus": {
            "bsonType": "bool",
            "description": "Should be Boolean and required"
        },
        "created_at":{
            "bsonType": 'date',
            "description": 'should be date, required'
        },
        "medicationDetails": {
            "bsonType": "array",
            "description": "Should be array of Medication objects",
            "items": {
                "bsonType": "object",
                "required": ["medicineName", "dosage", "frequency", 'start_date', 'end_date'],
                "properties": {
                    "medicineName": {
                        "bsonType": "string",
                        "description": "Name of Medicine, required"
                    },
                    "dosage": {
                        "bsonType": "string",
                        "description": "Dosage, required"
                    },
                    "frequency": {
                        "bsonType": "string",
                        "description": "Reaction description, required"
                    },
                    "start_date":{
                        'bsonType': 'date',
                        "description": 'Start date of medicine, required'
                    },
                    "end_date":{
                        'bsonType': 'date',
                        "description": 'Start date of medicine, required'
                    }
                }
            }
        }
    }
}


db.create_collection(
    'medication',
    validator = {
        "$jsonSchema": validators_medication
    }
)


validators_accidents = {
    "bsonType": "object",
    "required": ["accidentId", "user_id","accidentStatus", 'created_at'],
    "properties": {
        "accidentId": {
            "bsonType": "string",
            "description": "Should be integer and required"
        },
        "user_id": {
            "bsonType": "number",
            "description": "Should be string and required"
        },
        "accidentStatus": {
            "bsonType": "bool",
            "description": "Should be Boolean and required"
        },
        "created_at":{
            "bsonType": 'date',
            "description": 'should be date, required'
        },
        "accidentdetails": {
            "bsonType": "array",
            "description": "Should be array of Medication objects",
            "items": {
                "bsonType": "object",
                "required": ["accidentDate", "type", "bodypartInjured", 'Hospitalized', 'Surgery', "CurrentProblems", "ReportStatus"],
                "properties": {
                    "accidentDate": {
                        "bsonType": "date",
                        "description": "should be date, required"
                    },
                    "type": {
                        "bsonType": "string",
                        "description": "should be string, required"
                    },
                    "bodypartInjured": {
                        "bsonType": "string",
                        "description": "Should be string, required"
                    },
                    "Hospitalized":{
                        'bsonType': 'bool',
                        "description": 'should be True or False, required'
                    },
                    "Surgery":{
                        'bsonType': 'bool',
                        "description": 'should be True or False, required'
                    },
                    "CurrentProblems":{
                        'bsonType': 'string',
                        "description": 'should be string, required'
                    },
                    "ReportStatus":{
                        'bsonType': 'bool',
                        "description": 'should be True or False, required'
                    }
                }
            }
        }
    }
}

db.create_collection(
    'accidents',
    validator = {
        '$jsonSchema': validators_accidents
    }
)




# allergy_data = db['allergy'].find({'user_id': 9}).sort({"created_at": -1}).limit(1)
# allergy_data = list(allergy_data)

# for allergy in allergy_data[0]['allergy_details']:
#     print(allergy['allergy_type'])
#     print(allergy['allergy_name'])
#     print(allergy['allergy_reaction'])
#     # print(allergy)
