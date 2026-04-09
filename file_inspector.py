import os
import time

# The function that list all methods excluding dunder methods
# This function is just to understand functions in os module
def listing_out_methods(module):
    list_of_methods=[]
    for item in dir(module):
        if not (item.startswith('__') and item.endswith('__')):
            list_of_methods.append(item)
    return list_of_methods

#The function checks the given folder path and is it is a folder
def check_folder(folder):
   if os.path.exists(folder) and os.path.isdir(folder):
       return True
   else:
       return False
# Function that create dictionary of all file details and return it
def list_out_files(folder):
    dict_detail_about_file={}
    
    for item in os.listdir(folder):
        file=os.path.join(folder,item)
        if os.path.isfile(file):
            dict_detail_about_file.update({os.path.basename(file):details_of_given_file(file)})
    return dict_detail_about_file
# Function that create individual dictionary for each file and return it  
def details_of_given_file(file):
    file_detail={'modified':time.ctime(os.path.getmtime(file)),
                 'accessed':time.ctime(os.path.getatime(file)),
                 'created':time.ctime(os.path.getctime(file)),
                 'size':f"{round(os.path.getsize(file)/1024,0)}KB"}
    return file_detail
    
folder="Give your folder!!"
if check_folder(folder):
    print(list_out_files(folder))
else:
    print("Either given folder doesn't exsits or it is not a folder")




