-- Creating users tables
CREATE TABLE IF NOT EXISTS users(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(10) NOT NULL UNIQUE,
	email VARCHAR NOT NULL UNIQUE,
	password_hash VARCHAR NOT NULL,
	created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

INSERT INTO users(username, email, password_hash) VALUES ('testuser', 'test@gmail.com', 'test1234');

SELECT * FROM users;

-- creating patients personal details table
CREATE TABLE IF NOT EXISTS personal_details(
	personal_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	full_name VARCHAR(100) NOT NULL,
	date_of_birth DATE NOT NULL,
	gender CHAR(1) NOT NULL,
	contact_country_code VARCHAR(10) NOT NULL,
	contact_number VARCHAR NOT NULL,
	address TEXT,
	blood_group VARCHAR(4) NOT NULL,
	height_cm INTEGER NOT NULL,
	weight_kg INTEGER NOT NULL,
	bmi INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO personal_details (personal_id, user_id, full_name, date_of_birth, gender, contact_country_code, contact_number, address, blood_group, height_cm, weight_kg, bmi)
VALUES (
	'PD01',
    1,
    'John Doe',
    '1990-05-15',
    'M',
    '+1',
    '1234567890',
    '1234 Elm Street, Springfield, USA',
    'O+',
    180,
    75,
    23
);

SELECT * FROM personal_details;

-- Creating lifestyle table
CREATE TABLE IF NOT EXISTS lifestyle(
	lifestyle_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	smoking_status VARCHAR NOT NULL,
	alcohol_use VARCHAR NOT NULL,
	substance_use VARCHAR NOT NULL,
	exercise_frequency VARCHAR NOT NULL,
	sleep_hours INTEGER NOT NULL,
	diet_pattern VARCHAR NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO lifestyle (
    lifestyle_id, user_id, smoking_status, alcohol_use, substance_use, exercise_frequency, sleep_hours, diet_pattern
) VALUES (
    'LS01',
    1,
    'Non-smoker',
    'Occasional',
    'None',
    '3 times a week',
    7,
    'Vegetarian'
);

SELECT * FROM lifestyle;

-- creating medical history table
CREATE TABLE IF NOT EXISTS medical_history(
	medical_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	diabetes VARCHAR(100) NOT NULL,
	hypertension VARCHAR(100) NOT NULL,
	cardiac_disease VARCHAR(100) NOT NULL,
	respiratory_disease VARCHAR(100) NOT NULL,
	epilepsy VARCHAR(100) NOT NULL,
	mental_health_condition VARCHAR(100) NOT NULL,
	past_surgeries BOOLEAN NOT NULL,
	past_surgeries_type TEXT NOT NULL,
	family_history TEXT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO medical_history (
    medical_id, user_id, diabetes, hypertension, cardiac_disease, respiratory_disease, epilepsy, mental_health_condition,
    past_surgeries, past_surgeries_type, family_history
) VALUES (
    'MD01',
	1,
    'None',
    'Mild',
    'None',
    'Asthma',
    'None',
    'None',
    true,
    'Appendectomy',
    'No significant family history'
);

SELECT * FROM medical_history;


-- Creating allergies table
CREATE TABLE IF NOT EXISTS allergies(
	allergy_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	allergy_status BOOLEAN NOT NULL,
	allergy_type VARCHAR,
	allergy_name VARCHAR,
	allergy_reaction VARCHAR,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO allergies (allergy_id, user_id, allergy_status, allergy_type, allergy_name, allergy_reaction) VALUES (
    'AL01',
	1,
    true,
    'Food',
    'Peanuts',
    'Anaphylaxis'
);

SELECT * FROM allergies;

-- Creating table for current medication details
CREATE TABLE IF NOT EXISTS current_medication_details(
	medication_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	medication BOOLEAN NOT NULL,
	drug_name VARCHAR,
	dosage VARCHAR,
	frequency VARCHAR,
	start_date DATE,
	end_date DATE,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO current_medication_details (
    medication_id, user_id, medication, drug_name, dosage, frequency, start_date, end_date
) VALUES (
	'MDO1',
    1,
    true,
    'Aspirin',
    '100 mg',
    'Once daily',
    '2023-01-01',
    '2023-03-01'
);

SELECT * FROM current_medication_details;

ALTER TABLE users
ADD profile_photo VARCHAR;

SELECT * FROM users;

CREATE TABLE IF NOT EXISTS report(
	report_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	file_path VARCHAR NOT NULL,
	created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

INSERT INTO report (report_id, user_id, file_path, created_at) VALUES
('RPT001', 101, '/reports/101_blood_test.pdf', '2025-08-28 10:15:00+05:30'),
('RPT002', 101, '/reports/101_xray_chest.pdf', '2025-08-28 10:20:00+05:30'),
('RPT003', 102, '/reports/102_urine_test.pdf', '2025-08-27 09:45:00+05:30'),
('RPT004', 103, '/reports/103_ecg.pdf', '2025-08-26 14:30:00+05:30'),
('RPT005', 104, '/reports/104_mri_brain.pdf', '2025-08-25 16:00:00+05:30');


SELECT * FROM report;

ALTER TABLE personal_details
ADD COLUMN created_at TIMESTAMPTZ;

ALTER TABLE personal_details
ALTER COLUMN created_at
SET DEFAULT NOW();

SELECT * FROM personal_details;

ALTER TABLE current_medication_details
ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL;

SELECT * FROM current_medication_details;

ALTER TABLE lifestyle
ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL;

SELECT * FROM lifestyle;

ALTER TABLE medical_history
ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL;

SELECT * FROM medical_history;

ALTER TABLE allergies
ADD COLUMN created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL;

SELECT * FROM allergies;

DROP TABLE report;


CREATE TABLE IF NOT EXISTS report(
	report_id VARCHAR PRIMARY KEY,
	user_id INTEGER NOT NULL,
	file_path BYTEA NOT NULL,
	created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

SELECT * FROM report;

CREATE TABLE IF NOT EXISTS accidents (
    accident_id VARCHAR PRIMARY KEY,
    user_id INTEGER NOT NULL,
    any_accident BOOLEAN NOT NULL,
    accident_date DATE,
    accident_type VARCHAR,
    body_part_injured VARCHAR,
    hospitalized BOOLEAN,
    any_surgery BOOLEAN,
    lasting_problem VARCHAR,
    reports_available BOOLEAN,
    created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO accidents (
    accident_id,user_id, any_accident, accident_date, accident_type,
    body_part_injured, hospitalized, any_surgery, lasting_problem, reports_available
) VALUES (
	'AI1',
    1,
    '2022-08-15',
    'Road Accident',
    'Left Leg',
    TRUE,
    FALSE,
    'Occasional knee pain',
    TRUE
);

select * from accidents;


DROP TABLE allergies;
DROP TABLE accidents;
DROP TABLE current_medication_details;

