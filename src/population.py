import numpy as np
import pandas as pd
from scipy.stats import bernoulli
from scipy.stats import skewnorm
import random

# set variables
pop_size = 300

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
        self.baselineSBP = round(np.random.normal(150, 15))
        self.baselineDBP = round(np.random.normal(95, 10))
        self.cholesterol = round(np.random.normal(200, 30))
        self.treatment_score = 0

    def __repr__(self):
        return (f"Person {self.id}: age: {self.age}, sex: {self.sex}, BMI: {self.BMI}, smoker? {self.smoker}, diabetes? {self.diabetes}, baseline SBP: {self.baselineSBP}, baseline DBP: {self.baselineDBP}, cholesterol: {self.cholesterol}")
    
# create population
population = [Person(i) for i in range(pop_size)]

#/ test
"""
for person in population[:5]:
    print(person)
"""