import numpy as np
import pandas as pd
from scipy.stats import bernoulli
from scipy.stats import skewnorm
import random

# set variables
pop_size = 300

# Create trial class 
class ClinicalTrial:
    def __init__(
            self,
            n_patients = 300,
            duration_weeks = 52,
            treatment_effect = 30,
            placebo_effect = 8,
            dropout_rate = 0.3,
            adverse_event_rate = 0.2,
            random_seed = None
            treatment_probability = 0.5
    ):
        self.n_patients = n_patients
        self.duration_weeks = duration_weeks

        self.treatment_effect = treatment_effect
        self.placebo_effect = placebo_effect

        self.dropout_rate = dropout_rate
        self.adverse_event_rate = adverse_event_rate

        self.patients = []

        self.results = {}
    
    def enroll_patients(self):
        for patient_id in range(self.n_patients):
            self.patients.append(Person(patient_id))
        return 

    def assign_patients(self, seed, treatment_probability):
        for patient_id in range(self.n_patients):
            if seed is not None:
                random.seed(seed) # can use for verifying and debugging
        for person in population:
            if random.random() < treatment_probability:
                person.group = "treatment"
            else:
                person.group = "placebo"
        return population


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