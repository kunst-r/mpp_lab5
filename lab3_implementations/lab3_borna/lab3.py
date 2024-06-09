import numpy as np
import matplotlib.pyplot as plt
import random


class MarkovChain:
    def __init__(self, states, lambdas, transitionMatrix) -> None:
        self.states = states
        self.lambdas = lambdas
        self.transitionMatrix = transitionMatrix
        self.densityMatrix = []
        for i in range(len(states)):
            self.densityMatrix.append([])
        self.calculateDensityMatrix()

    # Calculates and assigns the density matrix
    def calculateDensityMatrix(self) -> None:
        for i in range(len(self.states)):
            for j in range(len(self.states)):
                if i == j:
                    self.densityMatrix[i].append(-self.lambdas[i])
                else:
                    self.densityMatrix[i].append(self.transitionMatrix[i][j] * self.lambdas[i])
        # Code for printing the density matrix
        print("Density matrix Q:")
        for i in range(len(self.states)):
            for j in range(len(self.states)):
                print(self.densityMatrix[i][j], end=", ")
            print("")

        return
    
    # Simulates a random walk of the specified Markov chain
    # Stores the durations of the walk in a dictionary and returns it
    def simulateRandomWalk(self, steps) -> dict:
        startingState = random.randint(0, 2)
        previousState = startingState

        durations = {}
        for state in self.states:
            durations[state] = []

        tempMat = self.transitionMatrix

        for i in range(steps):
            currentState = np.random.choice([0, 1, 2], p=transitionMatrix[previousState])
            durations[currentState].append(random.expovariate(self.lambdas[currentState]))
            previousState = currentState
            tempMat = np.matmul(tempMat, self.transitionMatrix)
        print("\nProbability matrix raised to the power of n:")
        print(tempMat)
    
        return durations
    
    

# Categories
states = {0 : "Social media",
          1 : "Music streaming", 
          2 : "Video streaming"}

# Average durations of sessions:
#     Social media: 53 minutes
#     Music streaming: 14 minutes
#     Video streaming: 87.6 minutes
lambdas = np.array([1/53, 1/14, 1/87.6])      

# Transition matrices between categories
transitionMatrix = np.array([[0.0, 0.25, 0.75], 
                             [0.4, 0.0 , 0.6 ], 
                             [0.8, 0.2 , 0.0 ]])

# Initialize the Markov chain
mChain = MarkovChain(states, lambdas, transitionMatrix)

# Simulate a random walk with 100 000 steps
durations = mChain.simulateRandomWalk(100000)

# Write the durations in three separate csv files, one for each category
with (open("social_media_readings.csv", "w") as sm_readings,
      open("music_streaming_readings.csv", "w") as ms_readings,
      open("video_streaming_readings.csv", "w") as vs_readings):
    
    sm_readings.write("Duration\n")
    for duration in durations[0]:
        sm_readings.write(f"{duration}\n")

    ms_readings.write("Duration\n")
    for duration in durations[1]:
        ms_readings.write(f"{duration}\n")

    vs_readings.write("Duration\n")
    for duration in durations[2]:
        vs_readings.write(f"{duration}\n")

# Calculate probabilities of occurrence for every category
# using its total time in simulation (task 5)
print("\nProbability of user being in a specific state:")
print(f"Social media: {sum(durations[0]/(sum(durations[0]) + sum(durations[1]) + sum(durations[2])))}")
print(f"Music streaming platforms: {sum(durations[1]/(sum(durations[0]) + sum(durations[1]) + sum(durations[2])))}")
print(f"Video streaming platforms: {sum(durations[2]/(sum(durations[0]) + sum(durations[1]) + sum(durations[2])))}")
