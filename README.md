# PreDoc - AI powered pre-consultation health assistant

Patients often visit doctors without clear symptom summaries or records. This leads to rushed, incomplete consultations, misdiagnoses, or repeated tests.
There’s a gap between self-observed health and what is communicated to the doctor.


> **PreDoc** is a smart pre-consultation app that collects health data from smartwatches and user inputs, uses AI to summarize symptoms, detect concerns, and generate a report to improve doctor consultations.


## 🗂️ Database Schema

#### 1. Users Table
Stores login and authentication details.

- `user_id (PK)`
- `email`
- `password_hash`
- `created_at`


#### 2. Patient_Details Table
Captures demographic and basic health details.

- `user_id (FK → Users)`
- `full_name`
- `dob`
- `gender`
- `contact_number`
- `address`
- `blood_group`
- `height_cm`
- `weight_kg`
- `bmi`


#### 3. Lifestyle Table
Stores day-to-day lifestyle factors that influence health.

- `user_id (FK → Users)`
- `smoking_status (Never/Former/Current)`
- `alcohol_use (Yes/No/Occasional)`
- `substance_use (Yes/No)`
- `exercise_frequency (None/Weekly/Daily)`
- `sleep_hours`
- `diet_pattern (Veg/Non-Veg/Vegan/etc.)`



#### 4. Medical_History Table
Keeps track of past illnesses, chronic conditions, and surgeries.

- `user_id (FK → Users)`
- `diabetes (Yes/No/Type)`
- `hypertension (Yes/No)`
- `cardiac_disease`
- `respiratory_disease`
- `epilepsy`
- `mental_health_conditions (Depression/Anxiety/etc.)`
- `past_surgeries (text)`
- `past_surgeries_type (text)`
- `family_history (text)`


#### 5. Allergies Table
Critical for avoiding harmful prescriptions.

- `allergy_id (PK)`
- `user_id (FK → Users)`
- `allergy_type (Drug/Food/Environmental)`
- `allergen_name (e.g., Penicillin, Peanuts)`
- `reaction (e.g., Rash, Anaphylaxis)`


#### 6. Current_Medications Table
Helps doctors avoid duplicate or conflicting prescriptions.

- `medication_id (PK)`
- `user_id (FK → Users)`
- `drug_name`
- `dosage`
- `frequency`
- `start_date`
- `end_date`

#### 🔗 Relationships

- Users Table provides the user_id (Primary Key).

- All other tables use user_id as a Foreign Key to maintain one-to-many or one-to-one relationships with users.

- This ensures a centralized schema, where every patient’s information is tied back to a unique identity.
