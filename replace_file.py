'''
1/3/2019
This script looks for the matching file name and place onto the designated folder if matched
'''

import os, os.path,shutil#, arcpy
maps = '' #location of maps

#reads files
def readfiles(basedir):
    filenames = []
    for dirpath, dirnames, file in os.walk(basedir):
        for names in file:
            filenames.append(names)
    print("\nFound ".join(filenames))        
    return filenames

#main function to search matching files and add onto the designated folder with (1)
def copyfiles(basedir,movdir):
    match_names = readfiles(basedir)
    print("\nSearching for matched Tiff.........\n\n")
    for dirpath, dirnames, file in os.walk(movdir):
        for filename in file:        
            for each_name in match_names:
                if(each_name.lower() == filename.lower()):
                    old_name = os.path.join(dirpath, filename)  
                    base, extension = os.path.splitext(filename)     
                    new_name = os.path.join(basedir, base+" (2)"+ extension)
                    shutil.copy(old_name, new_name)
                    print ("Copied " + old_name + " to "+ new_name)
    print("\n\n......Done")

#main function
def main():
    #while True:
    dest = '' #location of replacement
    #dest = raw_input("Enter destination folder: ")
        #try:
        #    if not os.path.exists(dest):
        #        raise ValueError
        #    else:
        #        break
        #except ValueError:
        #    print ("\nFolder path: \""+ dest + "\" is invalid")
    print("\n\nRunning")
    copyfiles(dest, maps)

if __name__ == '__main__':
    main()
