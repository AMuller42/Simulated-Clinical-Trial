from clinical_trial import Person
from clinical_trial import ClinicalTrial
import numpy as np

trial = ClinicalTrial()
trial.enroll_patients()
trial.assign_patients()
trial.treat()
trial.calculate_stats()