# elite-git-exercise

## Purpose

This is a quick reference to github cli commands


### Clone a repository

Find the URL of the repository to clone.

Copy it.

Paste it into this command:

`git clone <URL here>`



### Create a new branch

To create a new branch (forking it from the current branch you are on), run this command:

`git checkout -b <name of branch>`


### View all branches

To view all the branches you have currently in your local repository, run:

`git branch`

This will list all branches in the current repo into a window. Type in `q` to exit the window.


### Switch branches

To switch to an existing branch use:

`git checkout <name of branch>`

Notice the lack of the `-b` flag. 


### Perform a git pull

Make sure that there are no local changes that will be overwritten before running the below command

`git pull`


### Perform a git push

Ensure that your working directory is clean and all changes are committed

`git push`

If you are trying to push a newly made branch, you will need to run this command:

`git push --set-upstream origin <name of branch>`

This will create a copy of your local branch to your remote repository.

FYI: Check your commit message after this. If you want to submit a PR, it will have a quick link to do so. Otherwise you can submit a PR manually on the Github website.


### Stage your changes

First, check what changes are currently in your working directory with:

`git status`

You may individually stage changed files by using:

`git add <path to file>`

You may also stage all the changed files in your working directory with:

`git add -A`


### Commit your changes

Once your changes are staged, you may choose to commit them by using:

`git commit -m "<write a commit message>"`

I highly recommend writing clear messages stated what you changed in this commit. You may have to reference them later.


### Perform a diff

Diffs are the bread and butter of how git works. They tell you what changed between two separate versions, and are very useful for previewing your commits, validating, and debugging.

To perform a diff use this command:

`git diff <branch1> <branch2>`

This will generate a text file that will show you the changes that are made to turn branch1 into branch2.

For example: If branch1 has "hello world" on line 1 and branch2 does not, then the diff file will show ""


