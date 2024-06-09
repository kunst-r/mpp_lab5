import numpy as np
import matplotlib.pyplot as plt
import random
import math

# macros
NUM_OF_SIMULATION_STEPS = 100

class MarkovChain:
    def __init__(self, states, lambdas, transitionProbabilityMatrix) -> None:
        self.states = states
        self.lambdas = lambdas
        self.transitionProbabilityMatrix = transitionProbabilityMatrix
        self.durations = {}
        for state in self.states:
            self.durations[state] = []
 
    # Simulates a random walk of the specified Markov chain
    # Stores the durations of the walk in a dictionary and returns it
    def simulateRandomWalk(self, steps) -> dict:
        startingState = random.randint(0, 2)
        previousState = startingState

        for i in range(steps):
            # change state and generate duration of stay in that state
            currentState = np.random.choice([0, 1, 2], p=transitionProbabilityMatrix[previousState])
            currentStateDuration = math.ceil(random.expovariate(self.lambdas[currentState]))
            self.durations[currentState].append(currentStateDuration)
            previousState = currentState

            # TODO: generate packets and inter-arrival times

            print("currentState =", states[currentState], end = ", ")
            print("currentStateDuration =", currentStateDuration)
            
        return self.durations
    
##### MAIN ####

# Categories
states = {0 : "online video games",
          1 : "social networks", 
          2 : "video streaming"}

# Average durations of sessions: online video games: 16 seconds, social networks: 9 seconds, video streaming: 21 seconds
lambdas = np.array([1/16, 1/9, 1/21])     
transitionProbabilityMatrix = np.array([[0.0, 0.25, 0.75], 
                                        [0.4, 0.0 , 0.6 ], 
                                        [0.7, 0.3 , 0.0 ]])

# Initialize the Markov chain
mChain = MarkovChain(states, lambdas, transitionProbabilityMatrix)
# Simulate a random walk with 10 000 steps
durations = mChain.simulateRandomWalk(NUM_OF_SIMULATION_STEPS)
# Write the durations in a csv file
with open('lab3.csv', "w") as outFile:
    outFile.write("online_video_games,social_networks,video_streaming\n")
    for i in range(NUM_OF_SIMULATION_STEPS):
        row = ""
        if (i < len(durations[0])):
            row += f"{durations[0][i]},"
        else:
            row += "/,"
        
        if (i < len(durations[1])):
            row += f"{durations[1][i]},"
        else:
            row += "/,"

        if (i < len(durations[2])):
            row += f"{durations[2][i]}\n"
        else:
            row += "/\n"
        
        outFile.write(row)

""" leftovers from lab3, not necessary for lab5
# Calculate probabilities of occurrence for every category using its total time in simulation (task 5)
totalSimulationTime = sum(durations[0]) + sum(durations[1]) + sum(durations[2])
print("\nProbability of user being in a specific state:")
print(f"online video games: {sum(durations[0])/totalSimulationTime * 100} %")
print(f"social networks: {sum(durations[1])/totalSimulationTime * 100} %")
print(f"video streaming: {sum(durations[2])/totalSimulationTime * 100} %")
"""