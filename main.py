import os

current_dir = os.getcwd()
current_files = os.listdir()

# parent1 part1
channel_name_folder = "ConceptDemystifier"
# parent1 part2
website_name_folder = "Youtube"
# parent1 child1
course_title_folder = "demo_course_title"

# metadata.txt file content
course_title_info = "demo_course_title"
publish_date_info = "17th June 2023"
update_date_info = "5th August 2023"
course_link_info = "https://www.youtube.com/@byteacademy2611/playlists"
comment_info = ""

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

full_name = f"{channel_name_folder}_{website_name_folder}"
os.mkdir(full_name)
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