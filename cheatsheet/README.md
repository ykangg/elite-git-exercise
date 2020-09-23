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

For example: If branch1 has "hello world" on line 1 and branch2 does not, then the diff file will highlight that "hello world" on line 1 is removed. If you instead ran `git diff <branch2> <branch1>` then the diff file will highlight that "hello world" on line 1 is added. Try for yourself!

The diff command will open up an embedded text viewer inside the terminal. You can navigate through the text viewer through the arrow buttons (or you can use `j` for up and `k` for down). You can exit (quit) the view by pressing `q`.

Alternatively, if you want to save the text file somewhere, you can modify this command with:

`git diff <branch1> <branch2> > <choose a filename>`

The `>` command means to "pipe" which will write the output of the command to the file you provide afterwards. An example would be: `git diff master mydevbranch > diff.txt`


### Perform a merge

Sometimes, you will need to manually merge two branches together.

The most common case would be if there have been updates to `master` before you finish your dev branch. Before you submit a PR, you need to make sure that your dev branch has the most recent updates to master.

Run this command:

`git merge <branch1> <branch2>`

The first one is the branch with the changes that you want to merge INTO branch2. In other words, branch1 is the source branch, while branch2 is the destination branch.

In the above example, if we wanted to merge new changes from master into our dev branch, we would do this:

`git checkout master`  - Switch to master
`git pull`  - Pull the most recent changes from master
`git checkout <name of branch>`  - Switch back to your branch
`git merge master <name of branch>`  - Perform the merge

If there are no conflicts (changes that occur in the same file), then it will ask for confirmation. All you need to do is type `q`.

If there are conflicts, it will tell you that these conflicts need to be resolved, and will check you out to a tmp version of your branch. You can then manually edit the conflicting files to resolve them. Stage and commit these changes, and you are good to go!


### Perform a reset

Sometimes, you want to reset your current working branch to the state of the previous commit.

There are a lot of options for this, but for our sake, just remember this:

`git reset --hard`

This will reset everything that was not committed back to the state of the last commit. BEWARE, this will delete your changes.


### Check your commit history

To check the commit history of your current branch, use this command:

`git log`

This will put you into an embedded UI, listing all the previous commits, messages, and hash codes. You can navigate using the arrow keys or `j` and `k`. You can leave with `q`



### Perform a revert

Sometimes, you want to undo a commit. The best way to do this is to "revert" it. This is essentially making a new commit, that does the opposite of the commit you are reverting. Process looks like:

`git log`  - View the git log and copy the hash code from the commit you want to revert
`git revert <hash code>`

This will show you a confirmation screen (similar to a merge). Just type `q` and your revert will go through.

