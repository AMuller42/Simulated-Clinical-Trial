# assign each person to a group
# random 1 = treatment, random 0 = placebo

import random

# assign variables
treatment_probability = 0.5
def assign_treatment(population, treatment_prob = treatment_probability, seed = None):
    if seed is not None:
        random.seed(seed)
    for person in population:
        if random.random() < treatment_prob:
            person.group = "treatment"
        else:
            person.group = "placebo"
    return population