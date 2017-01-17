import pprint

"""
population = A 2D non-empty array of positive integers. Each cell represents one rabbit,
and the value of the cell represent's the rabbit's Resistance. 
x = The column of 'Patient Z' in the population array.
y = The row of 'Patient Z' in the population array.
strength = An integer value representing the strength of the virus.

Rules: The virus will attempt to infect Patient Z. Patient Z will only be infected if the
infection's Strength equals or exceed Patient Z's Resistance. Any infected rabbits will
attempt to infect any other uninfected neighbors (cells directly - not diagonally - 
adjacent in the array). They will infect any neighbor who have a Resistance less than or 
equal to the infection's strength. This will continue until no further infections are
possible. (i.e. every uninfected rabbit adjacent to an infected rabbit has a Resistance
greater than the infections strength.)

Write a function answer(population, x, y, strength), which outputs a copy of the input array
representing the state of the population at the end of the simulation, in which any infected
cells value has been replaced with -1.

Strength and Resistance values will be between 0 and 10000. The population grid will be at
least 2x2 and no larger than 50x50. The x and y values will be valid indicies in the
population arrays, with numbering beginning from 0. 
"""


# test if patient is susceptible to zombit infection
def spreadZombit(patient_z, strength):
    if patient_z > strength:
        return False
    else:
        return True

def getNeighbors(population, x, y, strength):
    neighbors = []
    current_pos = population[y][x]
    if x > 0:
        if -1 < population[y][x-1]: #<= strength:
            neighbors.append([x-1,y])
    if y > 0:
        try:
            if -1 < population[y-1][x]: #<= strength:
                neighbors.append([x, y-1])
        except:
            pass
    if x < len(population[y])-1:
        if -1 < population[y][x+1]: #<= strength:
            neighbors.append([x+1,y])
    if y < len(population)-1:
        try:
            if -1 < population[y+1][x]: #<= strength:
                neighbors.append([x,y+1])
        except:
            pass
    return neighbors

def answer(population, x, y, strength):
    # test if rabbit is susceptible to zombit infection
    isZombie = spreadZombit(population[y][x],strength)
    if isZombie:
        # if rabbit is zombie, make its value -1
        population[y][x] = -1
        # get all of rabbits neighbors
        neighbors = getNeighbors(population,x,y,strength)
        if neighbors:
            # recursively call answer to test each neighbor
            for i in neighbors:
                answer(population, i[0],i[1],strength)
    return population

test_case = [
    [6,7,2,7,6],
    [6,3,1,4,7],
    [0,2,4,1,10],
    [8,1,1,4,9],
    [8,7,4,9,9]
]
strength = 5
x = 2
y = 1
pprint.pprint(answer(test_case,x,y,strength))

test_case = [
    [0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0]
]
strength = 0
x = 0
y = 0
pprint.pprint(answer(test_case,x,y,strength))

test_case = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,3],
    [2,3,4],
    [3,2,1]
]
strength = 2
x = 0
y = 0
pprint.pprint(answer(test_case,x,y,strength))

