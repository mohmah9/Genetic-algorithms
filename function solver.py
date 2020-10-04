import random
  
# Number of individuals in each generation 
POPULATION_SIZE = 200
n_iterations =100

class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self,child): 

        geneT = int(random.random() * len(child))
        while (geneT == 0) :
            geneT = int(random.random() * len(child))
        if child[geneT] == "0":
            child[geneT] = "1"
        else:
            child[geneT] = "0"
        return child
  
    @classmethod
    def create_gnome(self): 
        ''' 
        create chromosome or string of genes 
        '''
        gnome='1'
        for _ in range(15):
            gnome+=str(random.randint(0,1))
        gnome=int(gnome)
        return gnome
  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring (crossover)
        '''
        parent1= list(str(self.chromosome))
        parent2 = list(str(par2.chromosome))
        
        geneA = int(random.random() * len(parent1))
        geneB = int(random.random() * len(parent1))
        while (geneA == geneB) :
            geneB = int(random.random() * len(parent1))
        
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        parent2[startGene:endGene] = parent1[startGene:endGene]
        child = parent2
        '''mutation'''
        prob = random.random()
        if prob < 0.05:
            child = self.mutated_genes(child)
        child = int("".join(child))
        return Individual(child) 
  
    def cal_fitness(self):
        inn = str(self.chromosome)
        decimal = int(inn[2:9],2)
        floating = int(inn[9:],2)
        x = decimal + (floating / (10 ** len(str(floating))))
        if inn[1]=="1":
            x = -x
        f = (9*(x**5))-(194.7*(x**4))+(1680.1*(x**3))-(7227.94*(x**2))+(15501.2*x)-13257.2
        f = abs(f)
        return f
   
def main():   
    generation = 1
    population = [] 
  
    # create initial population 
    for _ in range(POPULATION_SIZE): 
                gnome = Individual.create_gnome() 
                population.append(Individual(gnome)) 
    print("Generation: {}".format(0))
    print("Best chromosome : ", str(population[0].chromosome)[1:], "fitness: ", population[0].fitness)
    # for i in range(len(population)):
    #     print(population[i].chromosome , population[i].fitness)

    for _ in range(n_iterations):
        # sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 

        #if the accuracy(fitness) is under 0.02 then stop the algorithm
        if population[0].fitness < 0.02:
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
        print("Best chromosome : ",str(population[0].chromosome)[1:] , "fitness: " ,population[0].fitness)
        # for i in range(len(population)):
        #     print("chromosome : ",population[i].chromosome , "fitness: " ,population[i].fitness)
  
        generation += 1
    inn = str(population[0].chromosome)
    decimal = int(inn[2:9], 2)
    floating = int(inn[9:], 2)
    x = decimal + (floating / (10 ** len(str(floating))))
    if inn[1] == "1":
        x = -x
    print("Final best solution: " + str(x)+", Score is : "+str(population[0].fitness))
  
if __name__ == '__main__':
    main()