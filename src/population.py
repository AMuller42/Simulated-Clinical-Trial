import numpy as np
import pandas as pd
from scipy.stats import bernoulli
import random

# set variables
pop_size = 300

# create person class
class Person:
    def __init__(self, person_id):
        self.id = person_id
        self.age = round(np.random.normal(60, 10), 3)
        self.sex = bernoulli.rvs(0.5)
        self.BMI = round(np.random.normal(29, 5), 1)
        self.smoker = bernoulli.rvs(0.2)
        self.diabetes = bernoulli.rvs(0.15)
        self.baselineSBP = round(np.random.normal(150, 15))
        self.baselineDBP = round(np.random.normal(95, 10))
        self.cholesterol = round(np.random.normal(200, 30))

    def __repr__(self):
        return (f"Person {self.id}: age: {self.age}, sex: {self.sex}, BMI: {self.BMI}, smoker? {self.smoker}, diabetes? {self.diabetes}, baseline SBP: {self.baselineSBP}, baseline DBP: {self.baselineDBP}, cholesterol: {self.cholesterol}")
    
# create population
population = [Person(i) for i in range(pop_size)]

#/ test
"""
for person in population[:5]:
    print(person)
"""