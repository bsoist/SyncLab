import os

folders = ['PreK', 'Kindergarten','1st Grade','2nd Grade','3rd Grade','4th Grade','5th Grade','Media']

# change student to whatever username you use
homedir = os.path.join('/','Users','student')

# we install Dropbox in the default location
dropbox = os.path.join(homedir,'Dropbox')

for folder in folders:
    target = os.path.join(dropbox,folder)
    link =  os.path.join(homedir,folder)
    print "Creating Symbolic Link"
    print "%s -> %s" % (target, link)
    if os.path.exists(link):
        print "Exists. Skipping ..."
    else:
        os.symlink(target,link)


# this has nothing to do with syncing Dropbox, but
# we do want students to be able to easily find their
# TuxPaint pictures, so we create a symlink for that too

target = os.path.join('/',*['Users', 'student', 'Library', 'Application Support', 'TuxPaint', 'saved'])
link = os.path.join(homedir,'TuxPaint Pictures')
print "Creating Symbolic Link for TuxPaint Stuff"
print "%s -> %s" % (target, link)

if os.path.exists(target):
    print "Exists. Skipping ..."
else:
    os.symlink(target,link)

