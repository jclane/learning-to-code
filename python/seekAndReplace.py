import sys, os, fileinput

found = []
brands = {1:('ACE', 'GWY', 'EMA'), 2:'APP', 3:'ASU',4:('DEL','DRC'),5:('HEW','COM'),6:'LEN',7:'SAC',8:'SYC',9:'TSC'}
edited = 0
rootdir = r''

def is_in_classes(partclass):
    partClasses = ['AC', 'AD', 'ANT', 'AUBD', 'AUDIO', 'BAT', 'BLUE', 'BRA', 'BRD', 'CAB', 'CAM', 
    'CARD', 'CD', 'CMOS', 'CORD', 'COS', 'CRBD', 'DCBD', 'DCJK', 'DOCKIT', 'DVD', 'FAN', 'FDD', 
    'FLD', 'GK', 'HDD', 'HEAT SYNC', 'INV', 'IOB', 'IOP', 'KB', 'LAN', 'LCD', 'LDBD', 'LK', 'MEM', 
    'MIC', 'MOD', 'OBRD', 'OTHER', 'PEN', 'PROC', 'PWBD', 'PWR', 'REM', 'SCRD', 'TABMB', 'TUBRD', 
    'USBD', 'VBRD', 'VGBD', 'WIR'] 
               
    if partclass not in partClasses:
        return False
    else:
        return True

def show_results():
    if len(found) > 0:
        print('\nInvalid part classes were found in ' + str(len(found)) + ' files.\n Of those, ' + str(edited) + ' files were corrected.\n')
        ask = input('Save to results to file? (y/n) >> ')
        if ask.lower() == 'y' or ask.lower() == 'yes':
            savedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search results.csv")
            print(savedir)
            with open(savedir, "a") as flist:
                for el in found:
                    flist.write(el + ',\n')
        else:
            for el in found:
                print(el)
    else:
        print('All ' + str(brands[brand]) + ' part classes appear to be correct.')

def fix_it(file,splitLine):
    global edited
 
    try:
        with open(file, 'r+') as f:
            old = f.readlines() # Pull the file contents to a list
            f.seek(0) # Jump to start, so we overwrite instead of appending
            for line in old:
                if ','.join(splitLine) == line:
                    print('\n*****************************************************')
                    print('\nYou are about to edit the following line:\n\n' + line)
                    newstr = input('Enter correct part class >> ')
                    if is_in_classes(newstr):
                        splitLine[0] = newstr.upper()
                        f.write(','.join(splitLine))
                        edited += 1
                        
                        oldline = line.split(',',2)
                        
                        found.append(os.path.basename(file) + ',Class ' + oldline[0] + ' for PN ' + oldline[1] + ' changed to ' + splitLine[0])
                    else:
                        fix_it(file,line)
                else:
                    f.write(line)
                        
    except Exception as e:
        print("Error: " + str(e))
        print("@ file " + file)
        print("& line " + str(line))
                                                   
def seek_it(brand):
           
    for subdir, dirs, files in os.walk(rootdir):
                
        for file in files:

            filepath = subdir + os.sep + file
            fileSuffix = os.path.basename(filepath).split("-")
            fileSuffix = str(fileSuffix[-1][:3])
            

            if filepath.endswith(".csv") and fileSuffix in brands[brand]:
                with open(filepath, "r", encoding="latin1") as f:
                    try:
                        for line in f:
                            
                            if ',' in line and ',,' not in line and ',,,' not in line:
                                splitLine = line.split(",",1)

                                if not is_in_classes(splitLine[0]):
                                    print('\n*****************************************************')
                                    print('\nFound invalid class (' + splitLine[0] + ') in ' + file + '\n\n' + line)
                                    askfix = input('Fix class? (y/n) >> ')
                                    if askfix == 'y' or askfix == 'yes':
                                        fix_it(filepath,splitLine)                                        
                                    elif askfix == 'n' or askfix == 'no':
                                        found.append(os.path.basename(filepath) + ',' + 'unchanged')
                                    else:
                                        continue
                                else:
                                    continue
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
    show_results()
                
def set_rootdir(brand):
    global rootdir
    
    if 0 <= int(brand) >= 10:
        print('Selection is not valid!')
        brand = input('Please select brand (1-9) >> ')
        set_rootdir(brand)
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
            
print('\nPlease select brand:\n\n \
\t1. Acer/Gateway/Emachine\n \
\t2. Apple\n \
\t3. Asus\n \
\t4. Dell/Dell Reclamation\n \
\t5. HP/Compaq\n \
\t6. Lenovo\n \
\t7. Samsung\n \
\t8. Sony\n \
\t9. Toshiba\n')

brand = int(input('(Enter 1-9) >> '))
set_rootdir(brand)

if not rootdir:
    print('ERROR\nrootdir is not set')
else:
    seek_it(brand)