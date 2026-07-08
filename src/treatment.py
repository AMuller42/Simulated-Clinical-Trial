# Write the treatment function
# Things to note: 
# 1. placebo causes a slight reduction in pain over time (mostly caused by simple time)
# 2. Old (80+) slightly increase in pain over time in general
# 3. Obesity makes arthritis harder to treat (reduces effect of treatment)
# 4. Treatment doesn't affect everyone the same. There will be random variation in treatment effectiveness
# 5. High blood pressure, elderly, and smoker can give higher risk for serious adverse event
# 6. Extremely low cholesterol can cause depression and therefore dropout

# Imports
import numpy as np
from scipy.stats import bernoulli
import random

# Variables
# baseline expectations
drug_score_baseline = round(np.random.normal(30, 9))
placebo_score_baseline = round(np.random.normal(5, 2))
adverse_event_baseline = 0.2
dropout_baseline = 0.3
# adjustments
elderly_adj = round(np.random.normal(-10, 5))
random_variation = round(np.random.normal(0, 6))



# Treatment Function
def treat(population):
    # Counting
    adverse_event_counter = 0
    dropout_counter = 0
    treatment_counter = 0
    placebo_counter = 0
    high_BMI_counter = 0
    elderly_counter = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    low_cholesterol_counter = 0
    for person in population:
        if person.group == "treatment":
            treatment_effect = round(np.random.normal(30, 9)) + round(np.random.normal(0, 6))
            treatment_counter += 1
            if person.BMI >= 30:
                # scale effect by obesity level. More obese, treatment works worse
                treatment_effect -= round(np.random.normal(person.BMI*0.20 , 4))
                high_BMI_counter += 1
        else: # placebo group 
            treatment_effect = round(np.random.normal(5, 2)) + round(np.random.normal(0, 6))
            placebo_counter += 1
            if person.BMI >= 30:
                # scale effect by obesity level. More obese, treatment works worse
                treatment_effect -= round(np.random.normal(person.BMI*0.20 , 4))
                high_BMI_counter += 1
        
        if person.age >= 80:
            treatment_effect += round(np.random.normal(-10, 5)) #adj value is already negative
            elderly_counter += 1
        
        # adverse event
        if person.baselineSBP >= 130 or person.baselineDBP >= 100 or person.age >= 75 or person.smoker:
            adverse_event = bernoulli.rvs(adverse_event_baseline + 0.15)
            if adverse_event == 1:
                adverse_event_counter += 1
        else:
            adverse_event = bernoulli.rvs(adverse_event_baseline)
            if adverse_event == 1:
                adverse_event_counter += 1

        # dropout
        if person.cholesterol <= 120:
            dropout = bernoulli.rvs(dropout_baseline + 0.1) 
            low_cholesterol_counter += 1
            if dropout == 1:
                dropout_counter += 1  
        else: 
            dropout = bernoulli.rvs(dropout_baseline)
            if dropout == 1:
                dropout_counter += 1
    
        person.final = person.pain_score - treatment_effect
        person.treatment_score = treatment_effect
        if treatment_effect > 70:
            print(f"############################### HIGH SCORE ALERT {person.id}: ")

        print(f"Person {person.id}: dropout?: {dropout}, adverse event?: {adverse_event}, treatment effect: {treatment_effect}. Total: {person.final}")

    print("-------------------- Counting Stats ---------------------")
    print(f"Treatments: {treatment_counter}"
    f"\nPlacebos: {placebo_counter}"
    f"\nAdverse Events: {adverse_event_counter}"
    f"\nDropouts: {dropout_counter}"
    f"\nHigh BMIs: {high_BMI_counter}"
    f"\nElderly Participants: {elderly_counter}"
    f"\nLow Cholesterols: {low_cholesterol_counter}")
    return population
    

