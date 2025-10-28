# 🩺 **Predoc — Preconsultation Report Assistant**

### *Bridging the gap between patients and doctors through structured, data-driven preconsultation reports.*

---

## Overview

**Predoc (Preconsultation Report Assistant)** is an intelligent healthcare tool designed to **summarize patient information before consultations**, helping doctors make better, faster, and more informed decisions.

It addresses a real-world problem — **patients often struggle to describe their symptoms clearly**, leading to **incomplete or inaccurate consultations**. Predoc simplifies this process by collecting, analyzing, and organizing user inputs (symptoms, lifestyle, medical history, etc.) into a structured **preconsultation report** that doctors can review before appointments.

Predoc also includes disease-specific sections like **Dermatology and Oral Health**, powered by **CNN models** for image-based disease classification.

---

## Problem Statement

In most doctor consultations, **patients arrive unprepared**, and doctors spend a major portion of time just understanding the complaint rather than solving it.
This leads to:

* Incomplete or rushed consultations
* Misdiagnosis or repeated tests
* Poor doctor–patient communication

---

## Solution

Predoc bridges this communication gap by:

* Collecting structured patient data before consultation
* Summarizing key health insights automatically
* Using **ML + CNN models** to assist in image-based disease analysis
* Presenting everything in an easy-to-read **Preconsultation Report**

This ensures doctors receive **well-organized health data upfront**, allowing consultations to focus on **treatment, not information gathering**.

---

## Features

### 1. Smart Report Generation

Collects user inputs about symptoms, medical history, allergies, and lifestyle — then generates a **structured preconsultation report**.


### 2. CNN-Powered Disease Classification

Analyzes **dermatology and oral health images** with trained **CNN models** to classify probable disease categories.

### 3. Multi-Database Architecture

Uses **PostgreSQL** for structured data and **MongoDB** for flexible, dynamic inputs like allergies, medications, and accidents.

### 4. Clean Report

Displays all user information, symptom summaries, and uploaded images in a clear, organized format — with options to download the preconsultation report.

---

## Tech Stack

| Category            | Technologies                                      |
| ------------------- | ------------------------------------------------- |
| **Frontend**        | HTML5, CSS3, Jinja Templates           |
| **Backend**         | Flask (Python), JS                                    |
| **Database**        | PostgreSQL + MongoDB                              |
| **ML Models**       | CNN (PyTorch)                        |
| **Authentication**  | Google OAuth, Microsoft OAuth                     |
| **Version Control** | Git & GitHub                                      |
| **Other Tools**     | Jupyter, VS Code, Render for  deployment |

---

## Architecture

```
                 ┌──────────────────────────┐
                 │        User Input        │
                 │ (Symptoms, Images, etc.) │
                 └────────────┬─────────────┘
                              │
             ┌────────────────┴────────────────┐
             │                                 │
     ┌──────────────┐                 ┌────────────────┐
     │   Flask API  │  <────────────► │ PostgreSQL DB  │
     │ (Data Logic) │                 │ + Mongo DB     │
     └──────────────┘                 └────────────────┘
             │
             ▼
      ┌──────────────┐
      │   ML / CNN   │
      │ (Diagnosis)  │
      └──────────────┘
             │
             ▼
      ┌────────────────────────────┐
      │   Preconsultation Report   │
      │ (Organized health summary) │
      └────────────────────────────┘
```

---

## How It Works

1. **User Registration** → Secure login via Google/Microsoft OAuth.
2. **Data Collection** → User fills personal, lifestyle, and medical details.
3. **Image Upload** → Optional disease image (skin/oral) for CNN analysis.
4. **Report Generation** → Flask compiles user data + model output into a structured report.
5. **Download** → Report available in web and downloadable PDF format.

---

## Machine Learning Component

Predoc integrates two ML pipelines:

1. **Dermatology CNN Model** – Classifies common skin diseases.
2. **Oral Health CNN Model** – Detects dental and oral conditions like caries, ulcers, or discoloration.

Both models are **transfer learning-based CNNs** (EfficientNet) fine-tuned on curated datasets.


---

## Installation Guide

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/predoc.git
   cd predoc
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Databases**

   * Configure PostgreSQL URI in `config.py`
   * Connect MongoDB (local or Atlas)
   * Run initial migrations if needed

5. **Run the App**

   ```bash
   flask run
   ```

6. **Access App**

   ```
   http://127.0.0.1:5000/
   ```

---

## Future Scope

* Integration of **voice-based symptom input**
* Expanding disease classification models
* Doctor-side dashboard for report review
* Integration with wearable (IoT) health data
* Predictive health risk scoring using ML

---



## 🌐 Connect with Me

* [LinkedIn](https://www.linkedin.com/in/gaurav-s-yadav)
* [GitHub](https://github.com/GAuravY19)


