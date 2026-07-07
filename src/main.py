from population import Person
from assign import assign_treatment
from treatment import treat
import numpy as np

population = [Person(i) for i in range(300)]
population = assign_treatment(population, treatment_prob=0.5)
population = treat(population)

for person in population[:5]:
    print(f"Person: {person.id}, initial pain: {person.pain_score}, treatment score: {person.treatment_score}")

avg_treatment = np.mean([person.treatment_score for person in population if person.group == "treatment"])
avg_placebo = np.mean([person.treatment_score for person in population if person.group == "placebo"])
max_placebo = np.maximum([person.treatment_score for person in population if person.group == "placebo"])
min_placebo = np.minimum([person.treatment_score for person in population if person.group == "placebo"])
print(f"Average treatment improvement: {avg_treatment}")
print(f"Average placebo improvement: {avg_placebo}")