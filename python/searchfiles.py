import sys, os

found = []
brands = {1:('ACE', 'GWY', 'EMA'), 2:'APP', 3:'ASU'}
brand = 0
rootdir = ''

def select_brand():
    global rootdir, brand
    
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

    brand = int(input('(Enter 1-9) >> '))
    
    if 0 <= brand >= 10:
        print('Selection is not valid!')
        select_brand()
    else:
        if brand == 1:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Acer_Gateway_Emachine'
        elif brand == 2:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Apple-APP'
        elif brand == 3:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Asus-ASU'
        elif brand == 4:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Dell_Dell Reclamation'
        elif brand == 5:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\HP_Compaq'
        elif brand == 6:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Lenovo-LEN'
        elif brand == 7:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Samsung Computer-SAC'
        elif brand == 8:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Sony Computer-SYC'
        elif brand == 9:
            rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Toshiba-TSC'

def show_results():
    if len(found) > 0:
        print('Text found in the following ' + str(len(found)) + ' files.\n')
        ask = input('Save to results to file? (y/n) >> ')
        if ask.lower() == 'y' or ask.lower() == 'yes':
            savedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search results.csv")
            print(savedir)
            with open(savedir, "w") as flist:
                for el in found:
                    flist.write(el + ',\n')
                    print(el)
        else:
            for el in found:
                print(el)
    else:
        print('No results found.')
            
def find_it(searchTerm):
    global brand, brands, rootdir
    for subdir, dirs, files in os.walk(rootdir):
                
        for file in files:

            filepath = subdir + os.sep + file
            fileSuffix = os.path.basename(filepath).split("-")
            fileSuffix = str(fileSuffix[-1][:3])
            
            if filepath.endswith(".csv") and fileSuffix in brands[brand]:
                    with open(filepath, "r", encoding="latin1") as f:
                        try:
                            for line in f:
                                partClass = []
                                partNum = []
                                partDesc = []
                                
                                if ',' in line:
                                    splitLine = line.split(",")
                                    partClass.append(splitLine[0])
                                    partNum.append(splitLine[1])
                                    partDesc.append(splitLine[2])
                                else:
                                    pass
                                if searchTerm in partClass or searchTerm in partNum or searchTerm in partDesc or searchTerm in line:
                                    found.append(os.path.basename(filepath))
                                else:
                                    continue
                        except Exception as e:
                            print("Error: " + str(e))
                            print("@ file " + file)
                            print("& line " + str(line))
                            pass
                    continue
                else:
                    continue
            else:
                continue
    show_results()
                
      
select_brand()
searchTerm = input('Please enter text to search for >> ')
find_it(searchTerm)