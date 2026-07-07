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
adverse_event_baseline = bernoulli.rvs(0.2)
dropout_baseline = bernoulli.rvs(0.3)
# adjustments for 
obesity_adj = round(np.random.normal(-8, 3))
elderly_adj = round(np.random.normal(-10, 5))



# Treatment Function
def treat(population, adverse_event_prob = adverse_event_baseline, dropout = dropout_baseline):
    