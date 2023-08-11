# MODULE IMPORTS
import os
import time

# CURRENT WORKING DIRECTORY
current_dir = os.getcwd()
# CURRENT WORKING DIRECTORY CONTENT
current_files = os.listdir()

print(">>> Available course list")
for i,elt in enumerate(current_files):
    print(f">> {i}) {elt}")

print(">>> Enter the course number")
course_number = eval(input(">>> "))

print(f">>> The selected course is {current_files[course_number]}")

print(">>> Would you like to continue? (y/n)")
do_continue = input(">>> ")
if (do_continue.lower() == "y"):
    os.chdir(f"{current_dir}\\{current_files[course_number]}")
elif (do_continue.lower() == "n"):
    print(">>> Program will exit...")
    time.sleep(3)
    exit()
else:
    print(">>> Invalid entry, program will exit...")
    time.sleep(3)
    exit()

current_dir = os.getcwd()
current_files = os.listdir()
# CHECK & DISPLAY PWD - CODNTINUE or EXIT
print(">>> Present working directory")
print(f">>> {current_dir}")

print(">>> Would you like to continue? (y/n)")
do_continue = input(">>> ")
if (do_continue.lower() == "y"):
    pass
elif (do_continue.lower() == "n"):
    print(">>> Program will exit...")
    time.sleep(3)
    exit()
else:
    print(">>> Invalid entry, program will exit...")
    time.sleep(3)
    exit()

# SHOW DIRECTORY CONTENT - EXIST or NEW COURSE
print(">>> Create new channel and/or website? (y/n)")
do_create = input(">>> ")
if (do_create.lower() == "y"):
    print(">>> Enter the channel name")
    channel_name_folder = input(">>> ")
    print(">>> Enter the website name")
    website_name_folder = input(">>> ")

    full_name = f"{channel_name_folder}_{website_name_folder}"
    os.mkdir(full_name)
    
elif (do_create.lower() == "n"):
    print(">>> Present directory contents")
    for i,elt in enumerate(current_files):
        print(f">> {i}) {elt}")
    
    print(">>> Enter the channel number")
    channel_number = eval(input(">>> "))
    full_name = current_files[channel_number]

    print(f">>> The selected channel is {full_name}")

    channel_name_folder = full_name.split("_")[0]

    print(">>> Would you like to continue? (y/n)")
    do_continue = input(">>> ")
    if (do_continue.lower() == "y"):
        pass
    elif (do_continue.lower() == "n"):
        print(">>> Program will exit...")
        time.sleep(3)
        exit()
    else:
        print(">>> Invalid entry, program will exit...")
        time.sleep(3)
        exit()
else:
    print(">>> Invalid entry, program will exit...")
    time.sleep(3)
    exit()

# user input about the folder structure and file details
# folder name

print(">>> Enter the short course title")
course_title_folder = input(">>> ")

# file info
print(">>> Enter the complete course title")
course_title_info = input(">>> ")

print(">>> Enter the course publish date")
publish_date_info = input(">>> ")

print(">>> Enter the course last update date")
update_date_info = input(">>> ")

print(">>> Enter the course link")
course_link_info = input(">>> ")

print(">>> Enter the comment about the course")
comment_info = input(">>> ")

# default folder names
DEFAULT_REF_DIRNAME = "Reference"
DEFAULT_SESSIONS_DIRNAME = "Sessions"
# child folder of Sessions folder
DEFAULT_SESSION_DIRNAME = "Ses_1"

# default file names
DEFAULT_METADATA_FILENAME = "metadata.txt"
DEFAULT_STATUS_FILENAME = "Status_NotCompleted"
# children files of Sessions folder
DEFAULT_NOTES_FILENAME = "notes.docx"
DEFAULT_CONTENT_FILENAME = "courseContent.txt"

os.chdir(f"{current_dir}\\{full_name}")
os.mkdir(course_title_folder)
os.chdir(f"{current_dir}\\{full_name}\\{course_title_folder}")
os.mkdir(DEFAULT_REF_DIRNAME)
os.mkdir(DEFAULT_SESSIONS_DIRNAME)

metadata_file_template = f'''
Course Name: {course_title_info}
Channel Name: {channel_name_folder}
Course Publish Date: {publish_date_info}
Course Last Update: {update_date_info}
Course Link: {course_link_info}

Comment: {comment_info}
'''

f1 = open(DEFAULT_METADATA_FILENAME,"w")
f1.write(metadata_file_template)
f1.close()

f2 = open(DEFAULT_STATUS_FILENAME,"x")
f2.close()
os.chdir(f"{current_dir}\\{full_name}\\{course_title_folder}\\{DEFAULT_SESSIONS_DIRNAME}")
os.mkdir(DEFAULT_SESSION_DIRNAME)

f3 = open(DEFAULT_CONTENT_FILENAME,"x")
f3.close()

f4 = open(DEFAULT_NOTES_FILENAME,"x")
f4.close()

print(">>> Structure created successfully...")
print(">>> Program will exit...")
time.sleep(3)