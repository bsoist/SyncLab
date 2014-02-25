import os, sys, csv

try:
    studentfile = open(sys.argv[1])
except:
    print "Usage: python syncme.py <studentfile>"
    sys.exit()

# change student to whatever username you use
homedir = os.path.join('/','Users','student')

# we install Dropbox in the default location
dropbox = os.path.join(homedir,'Dropbox')

# the names of our classes are all over the place
# especially for Pre-K classes, so I group all 
# together based on the first character
# This only works if all your Kindergarten classes 
# begin with K and all your Pre-K begin with P

gradenames = {
'P': 'PreK',
'K': 'Kindergarten',
'1': '1st Grade',
'2': '2nd Grade',
'3': '3rd Grade',
'4': '4th Grade',
'5': '5th Grade'
}


# creates a folder in /users/USERNAME/Dropbox
# and attempts to make a symlink to it
def createFolder(pathargs, createlink=False):
    folder = os.path.join(dropbox,*pathargs)
    print "Creating folder %s" % folder
    os.mkdir(folder)
    link = os.path.join(homedir,*pathargs)
    if createlink:
        print "Creating link to %s at %s" % (folder,link)
        try:
            os.symlink(folder,link)
        except:
            pass

# grab list of folders from students.CSV
reader = csv.reader(studentfile)
reader.next()
folders = {}
for line in reader:
    grade,student,teacherparts=gradenames[line[0][0]],line[1],line[2].split(' ')
    # grab the title and last name for the teacher
    teacher = "%s %s" % (teacherparts[0],teacherparts[-1])
    if folders.get(grade,None) is None:
        folders[grade]={teacher:[]}
    else:
        if folders[grade].get(teacher,None) is None:
            folders[grade][teacher]=[]
    folders[grade][teacher].append(student)

# build folders and links
for grade,classes in folders.items():
    createFolder([grade], True)
    for teacher, students in classes.items():
        createFolder([grade,teacher])
        for student in students:
            createFolder([grade,teacher,student])


