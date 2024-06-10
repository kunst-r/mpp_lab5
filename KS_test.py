import pandas as pd
from scipy.stats import ks_2samp

#### VIDEO STREAMING ####

# Load the first dataset (two separate CSV files) with no header
vs_length1 = pd.read_csv('lab2_measurements/Borna_videostreaming/length.csv', header=None)
vs_time1 = pd.read_csv('lab2_measurements/Borna_videostreaming/time.csv', header=None)

# Load the second dataset (one CSV file) with headers
video_streaming = pd.read_csv('video_streaming.csv')

# Extract the relevant columns from the second dataset
vs_length2 = video_streaming['packetSize']
vs_time2 = video_streaming['interArrivalTime']

# Perform the KS test for packet lengths
vs_ks_result_length = ks_2samp(vs_length1.iloc[:, 0], vs_length2)

# Perform the KS test for interarrival times
vs_ks_result_time = ks_2samp(vs_time1.iloc[:, 0], vs_time2)

# Print the results
print("==== VIDEO STREAMING ====")

print("KS Test for Packet Lengths:")
print(f"Statistic: {vs_ks_result_length.statistic}, P-value: {vs_ks_result_length.pvalue}")

print("KS Test for Interarrival Times:")
print(f"Statistic: {vs_ks_result_time.statistic}, P-value: {vs_ks_result_time.pvalue}\n")


#### ONLINE VIDEO GAMES ####

# Load the first dataset (two separate CSV files) with no header
vg_length1 = pd.read_csv('lab2_measurements/Anteo_videogames/length.csv', header=None)
vg_time1 = pd.read_csv('lab2_measurements/Anteo_videogames/intervals.csv', header=None)

# Load the second dataset (one CSV file) with headers
video_games = pd.read_csv('online_video_games.csv')

# Extract the relevant columns from the second dataset
vg_length2 = video_games['packetSize']
vg_time2 = video_games['interArrivalTime']

# Perform the KS test for packet lengths
vg_ks_result_length = ks_2samp(vg_length1.iloc[:, 0], vg_length2)

# Perform the KS test for interarrival times
vg_ks_result_time = ks_2samp(vg_time1.iloc[:, 0], vg_time2)

# Print the results
print("==== VIDEO GAMES ====")

print("KS Test for Packet Lengths:")
print(f"Statistic: {vg_ks_result_length.statistic}, P-value: {vg_ks_result_length.pvalue}")

print("KS Test for Interarrival Times:")
print(f"Statistic: {vg_ks_result_time.statistic}, P-value: {vg_ks_result_time.pvalue}\n")

#### SOCIAL NETWORKS ####

# Load the first dataset (two separate CSV files) with no header
sn_length1 = pd.read_csv('lab2_measurements/Jaksa_Tviter/lab2velicinacsv.csv', header=None)
sn_time1 = pd.read_csv('lab2_measurements/Jaksa_Tviter/lab2vrijemecsv.csv', header=None)

# Load the second dataset (one CSV file) with headers
social_networks = pd.read_csv('video_streaming.csv')

# Extract the relevant columns from the second dataset
sn_length2 = social_networks['packetSize']
sn_time2 = social_networks['interArrivalTime']

# Perform the KS test for packet lengths
sn_ks_result_length = ks_2samp(sn_length1.iloc[:, 0], sn_length2)

# Perform the KS test for interarrival times
sn_ks_result_time = ks_2samp(sn_time1.iloc[:, 0], sn_time2)

# Print the results
print("==== SOCIAL NETWORKS ====")

print("KS Test for Packet Lengths:")
print(f"Statistic: {sn_ks_result_length.statistic}, P-value: {sn_ks_result_length.pvalue}")

print("KS Test for Interarrival Times:")
print(f"Statistic: {sn_ks_result_time.statistic}, P-value: {sn_ks_result_time.pvalue}")
