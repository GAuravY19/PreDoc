from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['predoc_no_sql_db']

# Allergy Table
validators_allergy = {
    "bsonType": "object",
    "required": ["allergy_id", "user_id", "allergyStatus"],
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
    "required": ["medicationId", "user_id","medicationStatus"],
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
    "required": ["accidentId", "user_id","accidentStatus"],
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


