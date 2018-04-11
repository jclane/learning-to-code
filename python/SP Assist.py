import sys, os

BRANDS = {1:('ACE', 'GWY', 'EMA'), 2:'APP', 3:'ASU',4:('DEL','DRC'),5:('HEW','COM'),6:'LEN',7:'SAC',8:'SYC',9:'TSC'}
brand = 0
rootdir = ''

def clear_screen():
    os.system('cls')
    
def print_menu(MENU):
    for el in MENU:
        print(MENU[el])

def is_in_classes(partclass):
    CLASSES = ['AC', 'AD', 'ANT', 'AUBD', 'AUDIO', 'BAT', 'BLUE', 'BRA', 'BRD', 'CAB', 'CAM', 
    'CARD', 'CD', 'CMOS', 'CORD', 'COS', 'CRBD', 'DCBD', 'DCJK', 'DOCKIT', 'DVD', 'FAN', 'FDD', 
    'FLD', 'GK', 'HDD', 'HEAT SYNC', 'INV', 'IOB', 'IOP', 'KB', 'LAN', 'LCD', 'LDBD', 'LK', 'MEM', 
    'MIC', 'MOD', 'OBRD', 'OTHER', 'PEN', 'PROC', 'PWBD', 'PWR', 'REM', 'SCRD', 'TABMB', 'TUBRD', 
    'USBD', 'VBRD', 'VGBD', 'WIR'] 
               
    if partclass not in CLASSES:
        return False
    else:
        return True

def select_brand():
    global brand, rootdir
    
    MENU = {0:'\n#### STEP 2 | Which brand would you like search? ####\n', 1:'\t1. Acer/Gateway/Emachine', 2:'\t2. Apple', 3:'\t3. Asus', 4:'\t4. Dell/Dell Reclamation', 5:'\t5. HP/Compaq', 6:'\t6. Lenovo', 7:'\t7. Samsung', 8:'\t8. Sony', 9:'\t9. Toshiba\n'}
    
    clear_screen()
    print_menu(MENU)
    
    brand = int(input('Select Number (1-' + str(len(MENU) - 1) + '): '))
    
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
        rootdir = r'\\VSP021320\GSC-Pub\BOM Squad\BOM-Smart Parts\Toshiba Computer-TSC'
    else:
        print('ERROR')

def get_files(dir):
    fileslist = []
    
    for subdir, dirs, files in os.walk(rootdir):          
        for file in files:
            fileSuffix = file.split("-")
            fileSuffix = str(fileSuffix[-1][:3])
            if file.endswith(".csv") and fileSuffix in BRANDS[brand]:     
                fileslist.append(subdir + os.sep + file)
    
    return fileslist

def show_results(found):
    if len(found) > 0:
        clear_screen()
        print('\nMatches were found in ' + str(len(found)) + ' files.\n')
        ask = input('Save to results to file? (y/n) : ')
        if ask.lower() == 'y' or ask.lower() == 'yes':
            savedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search results.csv")
            print('Results saved to ' + savedir)
            with open(savedir, "a") as flist:
                for el in found:
                    flist.write(el)
        else:
            for el in found:
                print(el)
    else:
        print('No matches found.')
        response = input('Return to the Main Menu? (y/n) : ')
        if response.lower() == 'y' or response.lower() == 'yes':
            main_menu()
        else:
            raise SystemExit
    
def search_files():
    MENU = {0:'\n#### STEP 1 | How would you like to search? ####\n',1:'\t1. Part Classes', 2:'\t2. Part Numbers', 3:'\t3. Search Descriptions', 4:'\t4. Search All', 5:'\t5. Quit\n'}
    
    clear_screen()
    for el in MENU:
        print(MENU[el])
    
    selection = int(input('Select Number (1-' + str(len(MENU) - 1) + '): '))

    select_brand()
    fileslist = get_files(rootdir)
    
    searchterm = input('Search for: ')
    clear_screen()
    print('\nSearching...')
    
    found = []
    
    for filepath in fileslist:           

        with open(filepath, "r", encoding="latin1") as f:
            try:
                for line in f:
                    if ',' in line and ',,' not in line and ',,,' not in line:
                        splitline = line.split(",",2)
                    
                        if selection == 1:
                            if searchterm == splitline[0]:
                                found.append(os.path.basename(filepath) + ',' + searchterm + ' found in PN ' + splitline[1] + ',' + splitline[2])
                                continue
                            elif selection == 2:
                                if searchterm == splitline[1]:
                                    found.append(os.path.basename(filepath) + ',' + searchterm + ' matches PN ' + splitline[1]  + ',' + splitline[2])
                                    continue
                            elif selection == 3:
                                if searchterm in splitline[2]:
                                    found.append(os.path.basename(filepath) + ',' + searchterm + ' found in PN  ' + splitline[1]  + ',' + splitline[2])
                                    continue
                            elif selection == 4:
                                if searchterm in splitline:
                                    found.append(os.path.basename(filepath) + ',' + searchterm + ' found in PN ' + splitline[1] + ',' + splitline[2])
                            else:
                                continue
                        else:
                            continue                    
                    else: 
                        continue
   
            except Exception as e:
                print("Error: " + str(e))
                print("@ file " + str(os.path.basename(f)))
                print("& line " + str(line))

    show_results(found)
                    
def main_menu():
    global brand, rootdir 
       
    brand = 0
    rootdir = ''
    MENU = {0:'\n\nPlease make a selection:\n', 1:'\t1. Search files', 2:'\t2. Seach and replace', 3:'\t3. Quit\n'}
    
    clear_screen()
    print_menu(MENU)
    
    selection = int(input('Select Number (1-' + str(len(MENU) - 1) + '): '))

    def call_func(selection):
        try:
            if selection == 1:
                search_files()
            elif selection == 2:
                search_and_replace()
            elif selection == 3:
                print('\nQuitting')
                raise SystemExit
            else:
                print('\n\n!ERROR : Please make a valid selection')
                main_menu()
        except ValueError:
                print('\n\n!ERROR : Please enter a number 1-' + str(len(MENU) - 1))
                main_menu()
    
    call_func(selection)
            
# Call main_menu on run     
main_menu()