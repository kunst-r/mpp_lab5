import numpy as np
import matplotlib.pyplot as plt
import random
import math
import scipy
import time
import scapy.all

# macros
NUM_OF_SIMULATION_STEPS = 20
PRINT_PACKET_SIZE = True
PRINT_STATE_STATS = True
PRINT_SIMULATION_STATS = True

# general packet settings, same for each one
icmp = scapy.all.ICMP()
icmp.type = 8
icmp.code = 0
ip = scapy.all.IP()
ip.src = '10.7.229.229'
ip.dst = '4.2.2.2' # random internet server for pinging, doesn't respond to multiple back-to-back requests

# set verbosity to almost mute
scapy.config.Conf.verb = 0

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
        # init simulation
        startingState = random.randint(0, 2)
        previousState = startingState

        # simulation stats for debugging purposes
        totalSimulationTime = 0
        totalSimulationPacketCount = 0

        # start the simulation
        for i in range(steps):

            # change state and generate duration of stay in that state
            currentState = np.random.choice([0, 1, 2], p=transitionProbabilityMatrix[previousState])
            currentStateDuration = math.ceil(random.expovariate(self.lambdas[currentState]))
            self.durations[currentState].append(currentStateDuration)
            previousState = currentState
            
            # current state stats for debugging purpose
            totalTimeSpent = 0
            totalPacketSentForThisState = 0 # not necessary
            
            if (PRINT_STATE_STATS):
                print("\ncurrentState =", states[currentState])
                print("currentStateDuration =", currentStateDuration, "s")
                
            # generate packets and inter-arrival times
            while (totalTimeSpent < currentStateDuration):
                
                # generate packet and inter-arrival time
                if (currentState == 0):
                    # online video games
                    # the best distribution for packet size: dweibull(c = 0.51, loc = 115.0, scale = 41.26)
                    packetSize = scipy.stats.dweibull.rvs(c=0.51, loc=115.0, scale=41.26, size=1)
                    while (packetSize[0] < 42):
                        packetSize = scipy.stats.dweibull.rvs(c=0.51, loc=115.0, scale=41.26, size=1)
                    # the best distribution for inter-arrival times: pareto(b = 11.52, loc = -0.09, scale = 0.09)
                    interArrivalTime = scipy.stats.pareto.rvs(b=11.52, loc=-0.09, scale=0.09, size=1)
                elif (currentState == 1):
                    # social networks
                    # the best distribution for packet size: halfgennorm(beta = 0.19, loc = 54.00, scale = 0.00)
                    packetSize = scipy.stats.halfgennorm.rvs(beta=0.19, loc=54.00, scale=0.0001, size=1)
                    while (packetSize[0] < 42):
                        packetSize = scipy.stats.halfgennorm.rvs(beta=0.19, loc=54.00, scale=0.00, size=1)
                    # the best distribution for inter-arrival times: kappa3(a = 2.11, loc = -0.0, scale = 0.02)
                    interArrivalTime = scipy.stats.kappa3.rvs(a=2.11, loc=-0.0, scale=0.02, size=1)
                elif (currentState == 2):
                    # video streaming
                    # the best distribution for packet size: foldcauchy(c = 118.91, loc = 0.2, scale = 10.86)
                    packetSize = scipy.stats.foldcauchy.rvs(c=118.91, loc=0.2, scale=10.86, size=1)
                    while (packetSize[0] < 42):
                        packetSize = scipy.stats.foldcauchy.rvs(c=118.91, loc=0.2, scale=10.86, size=1)
                    # the best distribution for inter-arrival times: genhalflogistic(c = 0.0, loc = -0.04, scale = 7.0)
                    interArrivalTime = scipy.stats.genhalflogistic.rvs(c=0.0000000000001, loc=-0.04, scale=7, size=1)

                if (PRINT_PACKET_SIZE):
                    print("packetSize =", int(packetSize[0]))

                # simulating the payload (each letter in payload is 1 B, empty echo request is 42 B)
                packetPayload = ""
                for i in range(int(packetSize[0]) - 42):
                    packetPayload += "a"

                # sending the packet, we don't care about the response
                scapy.all.send(ip / icmp / packetPayload)

                # simulate inter-arrival time by sleeping
                # TODO: uncomment the next line when done with debugging
                time.sleep(interArrivalTime[0])

                # state stats 
                totalTimeSpent += interArrivalTime[0]
                totalPacketSentForThisState += 1
                
            if (PRINT_STATE_STATS):
                print("totalPacketSentForThisState =", totalPacketSentForThisState)

            # simulation stats 
            totalSimulationTime += totalTimeSpent
            totalSimulationPacketCount += totalPacketSentForThisState
            
            
        if (PRINT_SIMULATION_STATS):        
            print("\ntotalSimulationTime =", totalSimulationTime)
            print("totalSimulationPacketCount =", totalSimulationPacketCount)
        
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

# Simulate a random walk 
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