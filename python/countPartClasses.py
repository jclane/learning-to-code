import os

rootdir = "S:\\BOM Squad\\BOM-Smart Parts\\"

""" 
This loops through the file, pulls the number of 
part numbers for the RAM, HDD, mobo, and CPUs and saves that 
number to a *.CSV file.
"""
def get_data(filepath, brand):
    with open(filepath, "r") as f:
        try:
            classList, classCount = [], []

            for line in f:
                splitLine = line.split(",",1)
                if splitLine[0] == "MEM" or splitLine[0] == "BRD" or splitLine[0] == "PROC" or splitLine[0] == "HDD":
                    classList.append(splitLine[0])

            classCount.append(str(classList.count("MEM")))
            classCount.append(str(classList.count("BRD")))
            classCount.append(str(classList.count("PROC")))
            classCount.append(str(classList.count("HDD")))

            if not os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop", "list-" + brand + ".csv")):
                with open(os.path.join(os.path.expanduser("~"), "Desktop", "list-" + brand + ".csv"), "w") as flist:
                    flist.write("Model,MEM,BRD,CPU,HDD,TOTAL,\n")
                    flist.write(os.path.basename(f.name) + ',' + ','.join(classCount) + ',\n')
            else:
                with open(os.path.join(os.path.expanduser("~"), "Desktop", "list-" + brand + ".csv"), "a") as flist:
                    flist.write(os.path.basename(f.name) + ',' + ','.join(classCount) + ',\n')
        except (EOFError, IndexError) as e:
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "errors.csv"), "a") as flist:
                flist.write(os.path.basename(f.name) + ',' + 'EOF Error: ' + e + ',\n')
            pass


"""
This loops through the brand directory and runs get_data() on each *.CSV
file.
"""
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        brand = os.path.basename(filepath).split("-")
        brand = str(brand[-1][:3])


        if filepath.endswith(".csv"):
            if brand == "ACE" or brand == "GWY" or brand == "APP" or brand == "ASU" or brand == "DEL" or brand == "HEW" or brand == "LEN" or brand == "SAC" or brand == "SYC" or brand == "TSC":
                get_data(filepath, brand)
                continue
            else:
                continue
        else:
            continue

