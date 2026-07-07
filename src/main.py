from population import Person
from assign import assign_treatment

population = [Person(i) for i in range(300)]
population = assign_treatment(population, treatment_prob=0.5)

for person in population[295:300]:
    print(f"{person}, {person.group}")