Syncing Student Work in the Lab
===============================
What?
-----
We wanted a simple way for students to save files on any of Macs in the lab and find those files on any of the other Macs in the lab. Students do not login with their own credentials. They login as a student with username student.

We also wanted to set this up so that students didn't have to think about using Dropbox.

Dropbox doesn't allow for syncing folders outside the Dropbox folder. Since we wanted to sync folders in the student/ folder, we needed to set up some links. My first approach was to create "real" folders at /Users/student/ and then create links inside the dropbox folder. This did not behave like we wanted it to. Dropbox treats the links as real folders and then creates real folders on the other Mac - and the syncing is not recursive. 

My next approach was to write a script that would sync all the files across every hour. I quickly dismissed that as more work than necessary and prone to serious issues.

Then it occurred to me to do it the other way, so this is what we have.

NOTE: Please IGNORE Dropbox as part of your routine and assume that the folders where students save work is synced (because it is). If you don't think about it, it will work.

Inside of /Users/student/Dropbox I created a folder for each grade. Then I created a link to each of those folder in /Users/student. What this does is give Johnny an easy way to find his folder. The folder really lives at /Users/student/Dropbox/5th Grade/Mrs. Bond/Johnny Smith/ but Johnny finds it at /Users/student/5th Grade/Mrs. Bond/Johnny Smith/

Why?
----
We've found this to be a nice simple solution for giving students access to their work on all of the computers in a lab. It also has the added benefit of builtin sharing. Since most of our teachers use Dropbox, it is a trivial matter to Mrs. Bond's folder with Mrs. Bond.

How?
----
To set up the lab ...

1. The tech teacher installed Dropbox on two computers and configured both for use with an account we set up for this purpose. 
2. I made sure there were no files in the Dropbox folder except for the default folders and files
3. I exported student information in a certain format (file included in this folder - students.CSV)
4. I wrote two scripts for the purpose of auto-creating folders and links.
5. I uploaded those scripts and the CSV file to the Dropbox account using the dropbox.com
6. I logged in to one of the Macs that had Dropbox installed and set up.
7. I typed the following commands into Terminal (hitting enter after each line)

    cd /Users/student/Dropbox
    python syncme.py students.CSV

8. I logged in to the other computer where Dropbox is ready to use.
9. I typed the following command into Terminal (hitting enter after)

    python /Users/student/Dropbox/linkme.py

10. Using the first computer, I added a file and a folder to a student folder.
11. I verified that folder and file synced to the other computer.
12. On the other computer, I did the same and checked number one to verify syncing.

Setting Up The Rest
--------------------
To set up the rest of the lab, visit each computer and ...

1. Install Dropbox and configure for the Dropbox account
2. Launch Terminal and type the following command and press enter

    python /Users/student/Dropbox/linkme.py

3. there is no step three

What To Do Next Year (and beyond)
---------------------------------
I highly recommend "wiping" all student work and starting over every year. Do that by doing this.

1. Create a new CSV file like the one included here. Name it students.CSV
2. Login to any of the lab computers.
3. Browse to the Dropbox folder.
4. Replace the old CSV file with the new one (drag the new one in and click "Replace" when prompted)
5. Delete all the class folders in Dropbox.
6. Launch Terminal and type the following command and press enter

    cd /Users/student/Dropbox
    python syncme.py students.CSV

7. If you have no new computers, you're done - they are all set up now. You only have to do this on one lab computer (anyone will do).

8. If you have a new computer to set up, follow the directions above under "Setting Up The Rest" (after you've done the previous seven steps ).

Notes
-----
The Python files make a lot of assumptions. They are commented throughout.

Drawbacks
---------
One major drawback in this scenario is that students have read/write permission on all files. We've found this to be an occassional problem, but not a deal-breaker so far.




