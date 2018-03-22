import os, time
import datetime as dt

rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\'

"""
This loops through the various brand folders and the *.CSV files they contain.  In the files it counts the instances of MEM, BRD, CPU, and HDD
and saves that number to a *.CSV file along with the name of the file the numbers came from.

Format: <file name>,<mem count>,<cpu count>,<hdd count>,<total>,<file creation date>
"""
for subdir, dirs, files in os.walk(rootdir):
    print('Starting on ' + subdir)
    for file in files:
        filepath = subdir + os.sep + file

        brand = os.path.basename(filepath).split("-")
        brand = str(brand[-1][:3])

        if filepath.endswith(".csv"):
            if brand == "ACE" or brand == "GWY" or brand == "APP" or brand == "ASU" or brand == "DEL" or brand == "HEW" or brand == "LEN" or brand == "SAC" or brand == "SYC" or brand == "TSC":
                with open(filepath, "r", encoding="latin1") as f:
                    mydir = os.path.dirname(os.path.abspath(__file__))
                    try:
                        classList, classCount = [], []

                        for line in f:
                            splitLine = line.split(",", 1)
                            if splitLine[0] == "MEM" or splitLine[0] == "BRD" or splitLine[0] == "PROC" or "HDD" == splitLine[0]:
                                classList.append(splitLine[0])

                        classCount.append(str(classList.count("MEM")))
                        classCount.append(str(classList.count("BRD")))
                        classCount.append(str(classList.count("PROC")))
                        classCount.append(str(classList.count("HDD")))

                        listPath = os.path.join(mydir, "list-" + brand + ".csv")

                        creationDate = dt.datetime.fromtimestamp(os.path.getctime(filepath))

                        if not os.path.exists(listPath):
                            with open(listPath,"w") as flist:
                                flist.write("Model,MEM,BRD,CPU,HDD,TOTAL,Created,\n")
                                flist.write(os.path.basename(f.name) + ',' + ','.join(classCount) + ',' + ',' + str(creationDate) + ',\n')
                        else:
                            with open(listPath,"a") as flist:
                                flist.write(os.path.basename(f.name) + ',' + ','.join(classCount) + ',' + ',' + str(creationDate) + ',\n')
                    except Exception as e:
                        errorPath = os.path.join(mydir, "errors.csv")
                        print("Error: " + str(e))
                        with open(errorPath, "a") as flist:
                            flist.write(os.path.basename(f.name) + ',' + str(e) + ',\n')
                        pass
                continue
            else:
                continue
        else:
            continue
