import math
from Population import Population
import random
from individual import Individual

def init_population(dim):
    new_population = Population()
    new_population.createPopulation(dim)
    return new_population

def make_fitness(population, name_function):
    for indiv in population.individuals:
        if name_function=="ackley":
            fit=ackley(indiv.genes, len(indiv.genes))

            indiv.set_fitness(fit)
            #print(indiv.fitness)
        elif name_function=="griewank":
            fit=griewank(indiv.genes, len(indiv.genes)) #proveri da li saljes dimenziju prostora ili broj promenljivih
            indiv.set_fitness(fit)
        else:
            fit = michalewiez(indiv.genes, len(indiv.genes)) #proveri da li saljes dimenziju prostora ili broj promenljivih
            indiv.set_fitness(fit)

def selection(population):
    ### imam populaciju koja ima listu individua (10),i od njih biram 2 roditelja, koje imaju loto, treba da sortiram, i pobijem pola
    for indiv in population.individuals:
        a = random.random()
        indiv.set_lotto(indiv.fitness * a)

    for i in range(0, len(population.individuals)):
        for j in range(0, len(population.individuals) - i - 1):
            if population.individuals[j].lotto > population.individuals[j + 1].lotto:
                t = population.individuals[j]
                population.individuals[j] = population.individuals[j + 1]
                population.individuals[j + 1] = t
    return population.individuals[0], population.individuals[1]  # ovo treba da su najbolji

def killing(population):
    for i in range(0,len(population.individuals)):
        for j in range(0,len(population.individuals)-i-1):
            if population.individuals[j].fitness>population.individuals[j+1].fitness:
                t = population.individuals[j]
                population.individuals[j] = population.individuals[j + 1]
                population.individuals[j + 1] = t
    new_list = population.individuals[0:int(len(population.individuals) / 2)]
    return new_list

def choosing_two_parents(population):
    for i in range(0, len(population.individuals)):
        for j in range(0, len(population.individuals) - i - 1):
            if population.individuals[j].fitness < population.individuals[j + 1].fitness:
                t = population.individuals[j]
                population.individuals[j] = population.individuals[j + 1]
                population.individuals[j + 1] = t
    return population.individuals[0], population.individuals[1]

def check_last(kids, parents):
    parent1, parent2 = choosing_two_parents(parents)
    if (kids.individuals[len(parents.individuals)-2].fitness > parent1.fitness):
        kids.individuals[len(parents.individuals)-2] = parent1

    elif (kids.individuals[len(parents.individuals)-2].fitness > parent1.fitness):
        kids.individuals[len(parents.individuals)-2] = parent1
        return

    if (kids.individuals[len(parents.individuals)-1].fitness > parent2.fitness):
        kids.individuals[len(parents.individuals)-1] = parent2

def work(name):
    chance=0.3
    if name=="griewank":
        chance=0.2
    dim = (int(input("Input dimension:")))
    first = init_population(dim)
    number_indiv=len(first.individuals)
    for j in range(0, 100):#300 generacija

        make_fitness(first, name)
        list_individuals = [None] * number_indiv*2 #jer treba da dobijem duplo vecu populaciju
        for i in range(number_indiv):
            parent1, parent2 = selection(first)
            list_individuals[i], list_individuals[number_indiv + i] = parent1.cross_over(parent2,chance)
        second = Population()
        second.set_individuals(list_individuals)
        killing(second)
        check_last(second, first)
        first = second
    make_fitness(first, name)
    first.individuals = killing(first)
    for ind in first.individuals:
        print(ind.genes)
    #the_best = first.individuals[0]
    print("the best fitnes ", first.individuals[0].fitness, first.individuals[0].genes)

def ackley(x,br_prom): #s tim da je br_promenljivih a ne dimenzija, dimenzija je za jedan veca
    sum1=0
    cosinus=0
    for i in range(0,br_prom):
        sum1+=(pow(x[i],2))
        cosinus+=(math.cos(2*math.pi*x[i]))
    #print(20-20*math.exp(-0.2*math.sqrt(sum1/(br_prom)))+math.e-math.exp(cosinus/(br_prom)))
    return(20-20*math.exp(-0.2*math.sqrt(sum1/(br_prom)))+math.e-math.exp(cosinus/(br_prom)))

def griewank(x, d):

    sumcomp = 0
    prodcomp = 1

    for i in range(0, d):
        sumcomp = sumcomp + pow(x[i],2)
        prodcomp = prodcomp*(math.cos(x[i] / math.sqrt(i+1)))
    scores = (sumcomp / 4000) - prodcomp + 1

    return scores
def michalewiez(x, d):
    sum1 = 0

    for i in range(0, d): #d-1?                  i+1                        d
        sum1 += math.sin(x[i])*math.pow(math.sin(i*pow(x[i], 2)/math.pi), 2*(d+1))
    return -sum1
def main():
    while (True):
        print("Input number of option: ")
        print("1) Ackley function")
        print("2) Griewank function")
        print("x) exit")
        option = input(">>>")
        if (option == "1"):
            work("ackley")

        elif (option == "2"):
            work("griewank")

        elif (option == "3"):
            work("michalewiez")

        elif (option == "x"):
            exit()

        else:
            print("Bad input, try again")

if __name__=="__main__":
    main()