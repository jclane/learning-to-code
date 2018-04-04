import sys, os, fileinput

found = []
brands = {1:('ACE', 'GWY', 'EMA'), 2:'APP', 3:'ASU'}
brand = 1
edited = 0
rootdir = r'C:\Users\a803415\Desktop\Pie'

def show_results():
    if len(found) > 0:
        print('\nText found in ' + str(len(found)) + ' files and ' + str(edited) + ' files were altered.\n')
        ask = input('Save to results to file? (y/n) >> ')
        if ask.lower() == 'y' or ask.lower() == 'yes':
            savedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search results.csv")
            print(savedir)
            with open(savedir, "w") as flist:
                for el in found:
                    flist.write(el + ',\n')
        else:
            for el in found:
                print(el)
    else:
        print('No results found.')

def fix_it(file,lineToChange):
    global edited
    
    try:
        with open(file, 'r+') as f:
            old = f.readlines() # Pull the file contents to a list
            f.seek(0) # Jump to start, so we overwrite instead of appending
            for line in old:
                if lineToChange == line:
                    print('\nYou are about to edit the following line:\n' + line)
                    newstr = input('Enter new text >> ')
                    f.write(newstr + '\n')
                    edited += 1
                    found.append(os.path.basename(file) + ',[' + lineToChange + '] changed to [' + newstr + ']\n')
                else:
                    f.write(line)
                        
    except Exception as e:
        print("Error: " + str(e))
        print("@ file " + file)
        print("& line " + str(line))
                                                   
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
                                print('\nFOUND ' + searchTerm + ' in ' + file)
                                askreplace = input('Replace string? (y/n) >> ')
                                if askreplace == 'y' or askreplace == 'yes':
                                    fix_it(filepath,line)                                        
                                else:
                                    found.append(os.path.basename(filepath) + ',' + 'unchanged\n')
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
                

searchTerm = input('\nPlease enter text to search for >> ')
find_it(searchTerm)