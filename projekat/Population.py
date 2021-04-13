from individual import Individual

class Population(object):

    def __init__(self):
        self.individuals=[None]*20


    def set_individuals(self, list_ind):
        self.individuals=list_ind

    def createPopulation(self, dim):

        for i in range(0,20): #populacija ima 200 jedinki
            self.individuals[i]=Individual(dim)
            self.individuals[i].create_genes()