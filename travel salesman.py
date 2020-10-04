import random 
  
# Number of individuals in each generation 
POPULATION_SIZE = 20
City_count= 5
n_generations=50
  
lengths = [[ 0, 2, 999, 12, 5 ], 
    [ 2, 0, 4, 8, 999 ], 
    [ 999, 4, 0, 3, 3 ], 
    [ 12, 8, 3, 0, 10 ], 
    [ 5, 999, 3, 10, 0]]

class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self,child): 

        geneT1 = int(random.random() * len(child))
        while (geneT1 == 0 or geneT1 == len(child)-1) :
            geneT1 = int(random.random() * len(child))
        geneT2 = int(random.random() * len(child))
        while (geneT2 == 0 or geneT2 == len(child)-1) :
            geneT2 = int(random.random() * len(child))
        child[geneT1],child[geneT2] = child[geneT2],child[geneT1]
        return child
  
    @classmethod
    def create_gnome(self): 
        ''' 
        create chromosome or string of genes 
        '''            
        gnome = [0]
        while (True):
            if len(gnome) == City_count:
                gnome.append(0)
                # print(gnome)
                break
            temp = random.randint(1,City_count-1)
            if temp not in gnome:
                gnome.append(temp)
        
        return gnome
  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring (crossover)
        '''        
        child = []
        childP1 = []
        childP2 = []
        
        geneA = int(random.random() * len(self.chromosome))
        geneB = int(random.random() * len(self.chromosome))
        while (geneA == geneB) :
            geneB = int(random.random() * len(self.chromosome))
        
        startGene = min(geneA, geneB)
        # print(startGene)
        endGene = max(geneA, geneB)
        # print(endGene)

        for i in range(startGene, endGene):
            childP1.append(self.chromosome[i])
        for i in range(len(par2.chromosome)):
            if (par2.chromosome[i] not in childP1) and len(childP2)< startGene :
                childP2.append(par2.chromosome[i])
        child = childP2 + childP1
        for i in range(len(par2.chromosome)):
            if par2.chromosome[i] not in child:
                child.append(par2.chromosome[i])
        child.append(0)
        '''mutation'''
        prob = random.random()
        if prob < 0.01:
            child = self.mutated_genes(child)
        
        return Individual(child) 
  
    def cal_fitness(self): 
        
        f=0
        for i in range(len(self.chromosome)-1):
            f += lengths[self.chromosome[i]][self.chromosome[i+1]]
        return f
   
def main():   
    generation = 1
    Minnn=99999999999
    population = [] 
  
    # create initial population 
    for _ in range(POPULATION_SIZE): 
                gnome = Individual.create_gnome() 
                population.append(Individual(gnome)) 
    print("Generation: {}".format(0))
    print("Chromosome : Fitness")
    for i in range(len(population)):
        print("".join(str(x) for x in population[i].chromosome) ," : ", population[i].fitness)
        if population[i].fitness < Minnn:
            Minnn = population[i].fitness

    for _ in range(n_generations):
        # sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 
  
        # if 90 percent of the individuals have the minimum path then it`s finished
        count = 0 
        s = int((90*POPULATION_SIZE)/100)
        for i in range(len(population)):
            if population[i].fitness == Minnn:
                count+=1
        if count>= s:
            break
        # Otherwise generate new offsprings for new generation 
        new_generation = [] 
  
        # Perform Elitism, that mean 30% of fittest population 
        # goes to the next generation 
        s = int((30*POPULATION_SIZE)/100) 
        new_generation.extend(population[:s]) 
  
        # From 50% of fittest population, Individuals  
        # will mate to produce offspring 
        s = int((70*POPULATION_SIZE)/100) 
        for _ in range(s): 
            parent1 = random.choice(population[:50]) 
            parent2 = random.choice(population[:50]) 
            child = parent1.mate(parent2) 
            new_generation.append(child) 
  
        population = new_generation 
  
        print("Generation: {}".format(generation))
        print("Chromosome : Fitness" )
        for i in range(len(population)):
            print("".join(str(x) for x in population[i].chromosome) ," : ", population[i].fitness)
            if population[i].fitness < Minnn:
                Minnn = population[i].fitness
  
        generation += 1

    print("\nBest path :" , "".join(str(x) for x in population[0].chromosome), ", path cost :" ,population[0].fitness)
if __name__ == '__main__':
    main()