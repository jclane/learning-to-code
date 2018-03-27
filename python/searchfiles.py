from time import sleep
import sys
import os

found = []
brand = 0
rootdir = ''

def select_brand():
    global rootdir
    print('Please select brand:\n \
    1. Acer/Gateway/Emachine\n \
    2. Apple\n \
    3. Asus\n \
    4. Dell\n \
    5. HP\n \
    6. Lenovo\n \
    7. Samsung\n \
    8. Sony\n \
    9. Toshiba\n')

    brand = input('(Enter 1-9) >> ')
    if 0 <= int(brand) >= 10:
        print('Selection is not valid!')
        select_brand()
    else:
        if brand == '1':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Acer_Gateway_Emachine'
        elif brand == '2':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Apple-APP'
        elif brand == '3':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Asus-ASU'
        elif brand == '4':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Dell_Dell Reclamation'
        elif brand == '5':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\HP_Compaq'
        elif brand == '6':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Lenovo-LEN'
        elif brand == '7':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Samsung Computer-SAC'
        elif brand == '8':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Sony Computer-SYC'
        elif brand == '9':
            rootdir = 'S:\\BOM Squad\\BOM-Smart Parts\\Toshiba-TSC'

select_brand()

searchTerm = input('Please enter text to search for >> ')

for subdir, dirs, files in os.walk(rootdir):
            
    for file in files:

        filepath = subdir + os.sep + file

        fileSuffix = os.path.basename(filepath).split("-")
        fileSuffix = str(fileSuffix[-1][:3])

        if filepath.endswith(".csv"):
            if fileSuffix == "ACE" or fileSuffix == "GWY" or fileSuffix == "APP" or fileSuffix == "ASU" or fileSuffix == "DEL" or fileSuffix == "HEW" or fileSuffix == "LEN" or fileSuffix == "SAC" or fileSuffix == "SYC" or fileSuffix == "TSC":
                with open(filepath, "r", encoding="latin1") as f:
                    try:

                        for line in f:
                            # Search lines for string here
                            if searchTerm in line:
                                found.append(os.path.basename(filepath))
                            else:
                                continue


                    except Exception as e:
                        print("Error: " + str(e))
                        pass
                continue
            else:
                continue
        else:
            continue

if len(found) > 0:
    print('Text found in the following ' + str(len(found)) + ' files.\n')
    ask = input('Save to desktop? (y/n) >> ')
    if ask.lower() == 'y' or ask.lower() == 'yes':
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        with open(desktop + "search results.csv", "w") as flist:
            for el in found:
                flist.write(el + ',\n')
                print(el)
    else:
        for el in found:
            print(el)
else:
    print('Text not found.')
