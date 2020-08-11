# Learning Git

## Andrew's Experiences/Suggestions

---
This is meant to be a rough guide to my experience learning to use git, and upping my computer science knowledge in general to gain the necessary skills for graduate studies at UBC's department of earth and ocean sciences.

### Command Line Interface

* Extremely useful skill/shift in perspective wrt using computers in general. Also a pre-requisite to effectively using git. My biggest breakthrough was realizing that using the command line/powershell/bash is generally doing the same things that one normally does with a GUI. For example, a good place to start would be a side-by-side comparison navigating a directory using ```cd```, ```ls```, ```mkdir```, etc. then performing the same operations using finder/file explorer. Learning objectives:

  * Ease the "scariness" of the command line and learning just the basic commands that we can build on to use git, conda, pip, etc.
  * Learn to picture what is happening with each line, instead of needing to refer constantly to a GUI
  * Perform several (fairly simple) tasks both with CLI and GUI, realizing they are equivalent
  * Learn the syntax:

    ```
    $ python my_program.py arg1 arg2 --tag -t
    ```

### Git as a File Backup System

The first and most obvious use for git as a grad student is as a free backup (online repository), as explained [here](http://phdcomics.com/comics/archive.php?comicid=1531). Much superior to the  ```myproject_ver1.py```, ```myproject_ver2.py``` workflow that we all "invent" as beginners. To make this work, you need:

* Make a github account (I found this fairly intuitive)
* cd to your working directory
* this sequence, and ***explain what is happening at each step***

```
$ git init
$ git status
$ git add .
$ git commit -m 'initial commit'
<make changes>
$ git add questionable_program.py
$ git commit -m 'make mistake'
$ git status
$ git revert <hash of initial commit>
```

This is enough to defeat the ```myprogram_ver1.py``` workflow.

Now, to create an online backup,

```
$ git remote add origin <url of my git repo>
$ git push origin master
```

and we have achieved the simplest possible working structure. Leave the tutorial here and let those with extra motivation discover branching, cloning, rebasing, etc.

### Jargon Dictionary

Explicitly define the following terms:

* Repository
* Fork
* Clone
* Branch
* Remote
* Origin
* Master
* origin/master (which is distinctly *not* the same as "origin master")
* Upstream
* Index
* Add
* Commit
* Checkout
* Push
* Pull
* Fetch
* Rebase
* Reset (hard? is there another kind?)
* Merge

    All of these are named so as to hint at their usages, but their metaphorical meanings tend to trample on one another, i.e. "Make sure to rebase the local branch on your fork before pushing upstream." This causes great confusion for the uninitiated.

    Like most technology, 90\% of the value comes from 10\% of the features. Git may have an even higher ratio of features to "useful" features, especially for casual users like grad students as opposed to developers working in larger teams on more complex projects.
