import csv

# Setting data for separation
csvInputPath = "generated_data.csv"
csvOutputNames = ["online video games", "video streaming", "social networks"]

def separateCSVData(csvInputPath: str, csvOutputPaths: list[str]):
    for fileName in csvOutputPaths:
        with (open(csvInputPath) as csvInput,
              open(fileName, "w") as csvOutput):
            
            csvOutput.write("packetSize, interArrivalTime\n")
            csvReader = csv.reader(csvInput, delimiter='\n')

            categoryName = fileName[:-4].replace("_", " ")
            for row in csvReader:
                splitRow = row[0].split(",")
                if splitRow[0] == categoryName:
                    csvOutput.write(f"{splitRow[1].replace("[", "").replace("]", "")},{splitRow[2].replace("[", "").replace("]", "")}\n")
                
        
##### MAIN ####
csvOutputPaths = []
for csvFileName in csvOutputNames:
    csvOutputPaths.append(csvFileName.replace(" ", "_") + ".csv")
#print(csvOutputPaths)
separateCSVData(csvInputPath, csvOutputPaths)