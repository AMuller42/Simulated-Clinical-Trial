import numpy as np
import pandas as pd
from scipy.stats import bernoulli
from scipy.stats import skewnorm
import random

# set variables
pop_size = 300

# Create trial class 
class ClinicalTrial:
    def __init__ (
            self,
            n_patients = 300,
            duration_weeks = 52,
            treatment_effect = 30,
            placebo_effect = 8,
            dropout_rate = 0.3,
            adverse_event_rate = 0.2,
            random_seed = None,
            treatment_probability = 0.5
    ):
        self.n_patients = n_patients
        self.next_patient_id = 1
        self.duration_weeks = duration_weeks

        self.treatment_effect = treatment_effect
        self.placebo_effect = placebo_effect

        self.dropout_rate = dropout_rate
        self.adverse_event_rate = adverse_event_rate

        self.patients = []

        self.results = {}
        return
    
    def enroll_patients(self):
        for i in range(self.n_patients):
            patient = Person(person_id = self.next_patient_id)
            self.patients.append(patient)
            self.next_patient_id += 1
        return 

    def assign_patients(self, seed = 42, treatment_probability = 0.5):
        for patient_id in range(self.n_patients):
            if seed is not None:
                random.seed(seed) # can use for verifying and debugging
        for patient in self.patients:
            if random.random() < treatment_probability:
                patient.group = "treatment"
            else:
                patient.group = "placebo"
        return population
    
    def treat(self):
        # Counting
        adverse_event_counter = 0
        dropout_counter = 0
        treatment_counter = 0
        placebo_counter = 0
        high_BMI_counter = 0
        elderly_counter = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        low_cholesterol_counter = 0
        female_counter = 0
        for patient in self.patients:
            if patient.group == "treatment":
                treatment_effect = round(np.random.normal(30, 9)) + round(np.random.normal(0, 6))
                treatment_counter += 1
                if patient.BMI >= 30:
                    # scale effect by obesity level. More obese, treatment works worse
                    treatment_effect -= round(np.random.normal(patient.BMI*0.20 , 4))
                    high_BMI_counter += 1
            else: # placebo group 
                treatment_effect = round(np.random.normal(5, 2)) + round(np.random.normal(0, 6))
                placebo_counter += 1
                if patient.BMI >= 30:
                    # scale effect by obesity level. More obese, treatment works worse
                    treatment_effect -= round(np.random.normal(patient.BMI*0.20 , 4))
                    high_BMI_counter += 1

            if patient.age >= 80:
                treatment_effect += round(np.random.normal(-10, 5)) #adj value is already negative
                elderly_counter += 1

            # adverse event
            if patient.baselineSBP >= 130 or patient.baselineDBP >= 100 or patient.age >= 75 or patient.smoker:
                adverse_event = bernoulli.rvs(self.adverse_event_rate + 0.15)
                if adverse_event == 1:
                    adverse_event_counter += 1
            else:
                adverse_event = bernoulli.rvs(self.adverse_event_rate)
                if adverse_event == 1:
                    adverse_event_counter += 1

            # dropout
            if patient.cholesterol <= 120:
                dropout = bernoulli.rvs(self.dropout_rate + 0.1) 
                low_cholesterol_counter += 1
                if dropout == 1:
                    dropout_counter += 1  
            else: 
                dropout = bernoulli.rvs(self.dropout_rate)
                if dropout == 1:
                    dropout_counter += 1

            if patient.sex == 0: #women
                patient.pain_score -= round(np.random.normal(7, 2))
                female_counter += 1

            patient.final = patient.pain_score - treatment_effect
            patient.treatment_score = treatment_effect
            if treatment_effect > 70:
                print(f"############################### HIGH SCORE ALERT {patient.id}: ")

            print(f"Person {patient.id}: dropout?: {dropout}, adverse event?: {adverse_event}, treatment: {patient.group}, treatment effect: {treatment_effect}. Total: {patient.final}")

        print("-------------------- Counting Stats ---------------------")
        print(f"Treatments: {treatment_counter}"
        f"\nPlacebos: {placebo_counter}"
        f"\nAdverse Events: {adverse_event_counter}"
        f"\nDropouts: {dropout_counter}"
        f"\nHigh BMIs: {high_BMI_counter}"
        f"\nElderly Participants: {elderly_counter}"
        f"\nLow Cholesterols: {low_cholesterol_counter}")
        return population

    def calculate_stats(self):
        avg_treatment = np.mean([patient.treatment_score for patient in self.patients if patient.group == "treatment"])
        avg_placebo = np.mean([patient.treatment_score for patient in self.patients if patient.group == "placebo"])
        max_placebo = 0
        min_placebo = 999
        for p in self.patients:
            if p.group == "placebo":
                if p.treatment_score > max_placebo:
                    max_placebo = p.treatment_score
                elif p.treatment_score < min_placebo:
                    min_placebo = p.treatment_score

        print("----------------------- Summary ----------------------")
        print(f"Average treatment improvement: {round(avg_treatment)}")
        print(f"Average placebo improvement: {round(avg_placebo)}")
        print(f"Max placebo improvement: {max_placebo}")
        print(f"Min placebo improvement: {min_placebo}")
        return


# create person class
class Person:
    def __init__(self, person_id):
        self.id = person_id
        # Pain scores will only be between 50 and 100. If someone only has moderate knee osteoarthritis, they will not participate
        self.pain_score = round(skewnorm.rvs(a = -8, loc = 80, scale=15))
        while self.pain_score < 51 or self.pain_score > 100:
            self.pain_score = round(skewnorm.rvs(a = -8, loc = 80, scale=15))

        self.age = round(np.random.normal(60, 10))
        self.sex = bernoulli.rvs(0.5)
        self.BMI = round(np.random.normal(29, 5))
        self.smoker = bernoulli.rvs(0.2)
        self.diabetes = bernoulli.rvs(0.15)
        self.baselineSBP = round(np.random.normal(120, 15))
        self.baselineDBP = round(np.random.normal(80, 10))
        self.cholesterol = round(np.random.normal(200, 30))
        self.treatment_score = 0
        self.final = 0

    def __repr__(self):
        return (f"Person {self.id}: age: {self.age}, sex: {self.sex}, BMI: {self.BMI}, smoker? {self.smoker}, diabetes? {self.diabetes}, baseline SBP: {self.baselineSBP}, baseline DBP: {self.baselineDBP}, cholesterol: {self.cholesterol}")
    
# create population
population = [Person(i) for i in range(pop_size)]

#/ test
"""
for person in population[:5]:
    print(person)
"""