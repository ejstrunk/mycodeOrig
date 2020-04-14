#!/usr/bin/python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def get_ip_data():
    input_host = input("\nWhat is the hostname of the computer? ")
    input_user = input("What is the current username? ")
    input_ip = input("What is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    d = {"Hostname": input_host, "User": input_user, "IP": input_ip, "Driver": input_driver}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] [{"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdic, dest_file_name="ip_list.xls")


# Runtime
mylistdict = [] # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

while(True):
    addmake = input("\nWould you like to (a)ppend an existing file or (c)reate a new file?")

    if addmake.lower() == "c":
        filename = input("\nWhat is the name of the *.xls file? ")
        pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')
        print("The file " + filename + ".xls should be in your local directory")
        break

    elif addmake.lower() == "a":
        filename = input("\nWhat is the name of the file you would like to append?")
        try:
            sheet = pyexcel.get_sheet()
            sheet.row += mylistdict
            sheet.save_as("excelappendtest.xls")
        except:
            print("\nFilename was not found. Please enter an existing file within the current directory.")
            continue

    else:
        print("Not a valid choice. Please type in a for append or c for create")
        continue
