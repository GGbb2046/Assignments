# Assignment01

There are four parts to this assignment. Part 1 through 3 are worth 10 points each, Part 4 is worth 5 points (but remember that Journal entries will be marked at the end of the semester -- and count towards 100 points)

## Part01: Hello World - GitHub Tutorial
* Complete the Git Hub introductory tutorial --
* NOTE: This demonstrates the "GitHub" side of Git/GitHub, we'll also need to know how to manage a local (installed on your laptop) copy of the repo, and how to push and pull between the remote repo and local repo. 
* [Git Hub Tutorial](https://guides.github.com/activities/hello-world/)

## Part02: Create a README.md file within the root directory of you your private repo.
* make sure you have your ST?? repo (your private repo) cloned to your hardrive
* Using bash commands, create a README.md file within the root directory of your ST??? personal repo
* This file should contain three lines:
  *  Firstname Lastname (`echo "Firstname Lastname' >> README.md`)
  *  Your email address (`echo "youremail@spartans.ut.edu' >> README.md`)
  *  Your major/area of study (`echo "Area of study' >> README.md`)
* View the file to make sure it looks OK ('cat README.md`)
* Now, you will add the README.md file to you repo's staging area (`git add README.md`)
* Then commit the change, (`git commit -m "my first commit'`)
* And finally, push this change to your github repo (`git push origin master`)

## Part03: Create a public repo

NOTE: When using an unpaid GitHub account, all the repos you create are public. For this class, I've created a number of private repos - one for each student. Private repositories mean that only those that are invited/added to the repository can access it's contents (normally, you need to pay for such a service from GitHub). This private repo will give you the peace of mind to know that any of the mistakes, bad code, errors, etc. that you make will not be available to the public.

But, for this exercise, you will creat your own public repo.

* Login into your GitHub account.
* On GitHub, create a new repository called PublicRepo (DO NOT select "create initial README.md file"!).
* Copy the address of this repo.
* Clone this repo to your local project folder.
* Copy the file you created in Exercise01-Part2 into this repo (the README.md about you).
* Now stage this file, commit the change (with descriptive message), and push the update to GitHub.
* Login to your github account, find your PublicRepo and verify that the changes have been made.


## Part04 - Create a Class Journal

Add an entry to your Journal folder found in your private repo (ST???). Write a new file for each journal entry. The naming should be C1_Journal.md, C2_Journal.md, etc. Do this using the GitHub web interface. 

Each journal entry is your reflection on the material that was covered in the course. Reflection, especially so soon after you've been exposed to the material, will help in your retention and learning processes. 


### Parting notes:

Forking a repo is a way of copying code from other projects into your own repo on github. You can then clone this repo to your desktop, and work with it just like we have been working with the class repos. If you want to merge updates from the "upstream repo" the one you copied from, you can do that (see: https://help.github.com/articles/syncing-a-fork/)

For more information on forking, see other:
* https://help.github.com/articles/creating-a-pull-request-from-a-fork/
* https://guides.github.com/activities/forking/

Also, since we've only covered the basics of git and GitHub, you may wish to experiment and try other features of git (also, understand more fully how git works - and concepts such  as HEAD, branch, merge, resetting, rebasing, reviewing logs, release tagging, etc.

One of the best resources to learn Git more fully if the "Git Pro" book found here: https://git-scm.com/book/en/v2


