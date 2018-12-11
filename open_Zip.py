#https://www.geeksforgeeks.org/working-zip-files-python/
# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "pakk.zip"
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    #  zip.printdir() 
    print(zip.namelist())
    zip.extract('2016-10-02_13-31-39_0.txt')
    # extracting all the files 
    #print('Extracting all the files now...') 
    #zip.extractall() 
    #print('Done!') 