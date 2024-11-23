import os
from termcolor import colored

def find_files_and_folders():
    
    #Get the files and folders in choosen directory
    tree = os.walk(start_directory)
    
    for roots, folders, files in tree:
        
        #Adds together the full filepath (folderpath + filename)
        for file in files:
            file_path = os.path.join(roots, file)

            #Opens file and reads its data, then searches for specified string index
            try:
                with open(file_path, 'r') as data:
                    opened_file = (data.read())
                    index = (opened_file.find(search_string))

                    #Prints out the found string + everything after it(to the specified length) at the index and file path it was found at
                    #Index gets incremented by one to ensure that multiple occurences in a single file get found
                    while index != -1:
                        print(colored("Found at index: " + str(index) + " | At path: " + file_path + " | String: " + opened_file[index:index + len(search_string) + length], 'green'))
                        index = opened_file.find(search_string, index + 1)
            
            #If a file cannot be opend it puts out an error message
            except Exception as error:
                print(colored("Error when opening file: " + file_path + " | " + str(error), 'red'))


#Input
start_directory = input("Please input your start directory: ")
search_string = input("Please input the string you want to search: ")
length = int(input("Please choose how many characters to print after the string: "))

#Function call
find_files_and_folders()
