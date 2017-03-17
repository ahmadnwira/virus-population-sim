# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

'''
Begin helper code
'''
class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
'''
End helper code
'''
#
# PROBLEM 1
#
class SimpleVirus(object):
    """ Representation of a simple virus (does not model drug effects/resistance). """
    def __init__(self, maxBirthProb, clearProb):
        """
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb, self.clearProp = maxBirthProb, clearProb

    def doesClear(self):
        """ check if virus-particle dies """
        if random.random() < self.clearProp:
            return True
        return False

    def reproduce(self, popDensity):
        """
        generate the next generation of viruses
        notes that P(produce) is function of popDensity
        """
        rand = random.random()
        if rand < self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb,self.clearProp)
        else:
            raise NoChildException



class SimplePatient(object):
    """
     simplified patient. doesn't take drugs and his virus populations have no drug resistance.
    """
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        survivalPop = []
        for virus in self.viruses:
            if not virus.doesClear():
                survivalPop.append(virus)
        # update population
        self.viruses = survivalPop
        popDensity = float(len(self.viruses)) / self.maxPop

        nextGeneration = []
        for virus in self.viruses:
            nextGeneration.append(virus)
            try:
                nextGeneration.append(virus.reproduce(popDensity))
            except:
                pass
        self.viruses = nextGeneration
        return  self.getTotalPop()

def step(maxBirthProp=.1, clearProb=.05,intialInfectionNum=100, maxPop=1000):
    """ represent a step in simulation """
    virus = SimpleVirus(maxBirthProp, clearProb)
    intialInfectionPop = []

    for i in range(intialInfectionNum):
        intialInfectionPop.append(virus)
    patient = SimplePatient(intialInfectionPop, maxPop)

    virusPopRecord = []
    for i in range(300):
        # represent 300 hour
        virusPopRecord.append(patient.update())
    return virusPopRecord


def  simulationWithoutDrug(trialsNum=500):
    """ Run the simulation and plot the graph """
    results = step()
    for i in range(trialsNum):
        newResults = step()
        for j in range(len(newResults)):
            results[j] += newResults[j]

    for i in range(len(results)):
        results[i] /= float(trialsNum)

    pylab.plot(results, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.show()

# uncomment to run sim
# trials with less than 100 reptation is not staple 
#simulationWithoutDrug(500)