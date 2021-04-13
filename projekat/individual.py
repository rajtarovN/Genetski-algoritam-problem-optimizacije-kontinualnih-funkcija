from random import randint, random, uniform
from random import uniform as nesto
from copy import deepcopy
import math
class Individual(object):
    def __init__(self, dim):

        self.num_variables = dim-1
        self.genes = [None]*self.num_variables
        self.fitness = 0
        self.lotto = 0

    def set_genes(self, list_genes):
        self.genes = list_genes

    def set_fitness(self, num):
        self.fitness = num

    def set_lotto(self, lotto):
        self.lotto = lotto

    def create_genes(self):

        for i in range(0, self.num_variables):
            self.genes[i] = randint(-10, 10)

    def cross_over(self, individual,chance):

        child1 = Individual(self.num_variables + 1)
        child1.genes = [None]*self.num_variables
        child2 = Individual(self.num_variables + 1)
        child2.genes = [None] * self.num_variables

        for i in range(self.num_variables):
            if self.genes[i] < individual.genes[i]:
                a = randint(self.genes[i], individual.genes[i])
                b = randint(self.genes[i], individual.genes[i])
            else:
                a = randint(individual.genes[i],  self.genes[i])
                b = randint(individual.genes[i], self.genes[i])
            child1.genes[i] = a
            child2.genes[i] = b
            #print(child1.genes)
        #chance = 0.3
        c = random()
        g = random()
        if c < chance:
            child1.mutation()
        if g < chance:
            child2.mutation()
        return child1, child2

    def mutation(self):
        a = randint(0, self.num_variables - 1)
        b = randint(0, self.num_variables - 1)

        self.genes[a] = randint(-10, 10)
        self.genes[b] = randint(-10, 10)

        if self.num_variables >= 8:
            c = randint(0, self.num_variables - 1)
            self.genes[c] = self.genes[c]+1
