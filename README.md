# elite-git-exercise

## Instructions

This is an exercise to get you through the basic steps of development with git. We will be going over this exercise together, following my screen. Reach out to me if you get stuck.

## Set Up

### Create a Github Account (if you don't have one already)
https://github.com/join

Quick tips:
* A mature github profile looks good on you, try to pick a name you'd want to keep for a while
* Use an email that you will be using in the future. **Do not use your school email**

### Installing *Git* on *Linux* (Windows Users here)

Remember that we installed Ubuntu to run inside your Windows OS. At this point, you can treat your Ubuntu terminal as an Ubuntu OS (and follow any Ubuntu instructions/tutorials).

Open up your Ubuntu terminal through the program (you can keep a shortcut, or you can just search for "Ubuntu" inside of your bottom left search bar)

**Copy & paste the following** into the terminal window and **hit `Return`**. You may be prompted to enter your password.

```shell
sudo apt update
sudo apt upgrade
sudo apt install git
```

### Installing *Git* on *Mac*

Last week you should have installed Homebrew on your Mac.

Setting up Github is as simple as this:

```shell
brew install git
```

## Github Exercises

### Part 1
* Fork this repository
* Clone this repository to your local
* Debug `math_test.py`
* Make changes to fix `math_test.py`
* Stage your changes
* Commit your changes
* Push your change directly to the remote repository
* Verify your change on https://www.github.com/

### Part 2
* Create a development branch
* Create the file [your-name].txt file with your github username inside
* Stage your changes
* Commit your changes
* Push your branch to the remote repository
* Submit a Pull Request
* Delete your remote and local development branches

### Bonus

* Pull a fresh version from master
* Create a new development branch
* Edit the file rollcall.txt by adding your name
* Perform a diff between master and your branch
* Verify your changes
* Stage your changes
* Commit your changes
* Switch to master and pull a fresh version from master
* Switch to your development branch
* Perform a merge from master to your development branch
* Commit your changes
* Push your branch to remote
* Submit a pull request
* Delete your remote and local development branches
