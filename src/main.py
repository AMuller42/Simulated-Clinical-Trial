from population import Person
from assign import assign_treatment
from treatment import treat
import numpy as np

population = [Person(i) for i in range(300)]
population = assign_treatment(population, treatment_prob=0.5)
population = treat(population)


avg_treatment = np.mean([person.treatment_score for person in population if person.group == "treatment"])
avg_placebo = np.mean([person.treatment_score for person in population if person.group == "placebo"])
max_placebo = 0
min_placebo = 999
for person in population:
    if person.group == "placebo":
        if person.treatment_score > max_placebo:
            max_placebo = person.treatment_score
        elif person.treatment_score < min_placebo:
            min_placebo = person.treatment_score

print("----------------------- Summary ----------------------")
print(f"Average treatment improvement: {round(avg_treatment)}")
print(f"Average placebo improvement: {round(avg_placebo)}")
print(f"Max placebo improvement: {max_placebo}")
print(f"Min placebo improvement: {min_placebo}")