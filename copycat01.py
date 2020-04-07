#!/usr/bin/python3

# import additional code to complete our task
import shutil    # imports the shutil method: a tool for higher-level file manipulation
import os        # imports the os method: a tool more targeted at the operating system

# move into the working directory
os.chdir("/home/student/mycode/")  # allows the user to run the program from any location on system

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")    # copies the file at path source to folder at path dest (both strings)

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")   # creates a backup
