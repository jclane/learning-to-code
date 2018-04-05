from time import sleep
import os
import sys

"""
This loops through the various brand folders and the *.CSV files they contain.  In the files it will search for unknown/incorrect
part classes and save the model number to a text file.
"""
rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\'

for subdir, dirs, files in os.walk(rootdir):
    print('Starting on ' + subdir)
    classesList = ['AC', 'AD', 'ANT', 'AUBD', 'AUDIO', 'BAT', 'BLUE', 'BRA', 'BRD', 'CAB', 'CAM', 
    'CARD', 'CD', 'CMOS', 'CORD', 'COS', 'CRBD', 'DCBD', 'DCJK', 'DOCKIT', 'DVD', 'FAN', 'FDD', 
    'FLD', 'GK', 'HDD', 'HEAT SYNC', 'INV', 'IOB', 'IOP', 'KB', 'LAN', 'LCD', 'LDBD', 'LK', 'MEM', 
    'MIC', 'MOD', 'OBRD', 'OTHER', 'PEN', 'PROC', 'PWBD', 'PWR', 'REM', 'SCRD', 'TABMB', 'TUBRD', 
    'USBD', 'VBRD', 'VGBD', 'WIR'] 
    
    """
    n = len(dirs)
    for i in range(n):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[{:{}}] {:.1f}%".format("=" * i, n - 1, (100 / (n - 1) * i)))
        sys.stdout.flush()
        sleep(0.25)
    """               
                   
    for file in files:
    
        filepath = subdir + os.sep + file

        brand = os.path.basename(filepath).split("-")
        brand = str(brand[-1][:3])

        if filepath.endswith(".csv"):
            if brand == "ACE" or brand == "GWY" or brand == "APP" or brand == "ASU" or brand == "DEL" or brand == "HEW" or brand == "LEN" or brand == "SAC" or brand == "SYC" or brand == "TSC":
                with open(filepath, "r", encoding="latin1") as f:
                    mydir = os.path.dirname(os.path.abspath(__file__))
                    try:
                        listPath = os.path.join(mydir, "BadClass.csv")
                        for line in f:
                            splitLine = line.split(",", 1)
                            if splitLine[0] not in classesList:
                                if not os.path.exists(listPath):
                                    with open(listPath,"w") as flist:
                                        flist.write("Model,Classs,\n")
                                        flist.write(os.path.basename(f.name) + ',' + splitLine[0] + ',\n')
                                else:
                                    with open(listPath,"a") as flist:
                                        flist.write(os.path.basename(f.name) + ',' + splitLine[0] + ',\n')
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
