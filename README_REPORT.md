Please read this document in Open Preview: Ctrl+Shift+V, or Right-click 'README_USER_MANUAL.md'  
in the vsCode Explorer and then select the first option 'Open Preview'.

## Table of contents
- [Intro](#intro)
- [3 components of the solution](#3-components-of-the-solution)
- [3 problems with solutions](#3-problems-with-solutions)
  - [problem 1:](#problem-1)
  - [problem 2:](#problem-2)
  - [problem 3:](#problem-3)

<br/>

# Intro
[Table of contents](#table-of-contents)

<br/>

Write a short, 200/300-word report in which you discuss at least the following:

Name three components of your solution, explain what they are and how they relate to each other.  
A 'component' can be anthing from GitHub Actions or Bash to Digital Ocean and SSH.  
Discuss three problems that you encountered along the way and how you solved them.  
(optional) Anything of note that you want to share about the process of solving this assignment.


<br/>
<br/>

# 3 components of the solution
[Table of contents](#table-of-contents)

GitHub Actions is a CICD platform for automating your build test and deployment pipeline.  
Key feature are the actions: like functions that do all kinds of work, e.g. move data, login to a server, etc.  

Digital Ocean Droplets are remote virtual machines, with operating system and optional software pre-installed.  

SSH is een (OSI application layer) netwerk protocol to create a safe connection between computer A, the client  
with private key, and computer B, the host with the public key, over an unsecured network.  
With SSH you sit in front of A and can work on B by remotely logging in.

When code is pushed from a local machine to github, a GitHub Actions workflow, tests the code and then sends  
it to the droplet. SSH is needed to establish a connection between the GitHub Actions workflow and the droplet. 


<br/>
<br/>

# 3 problems with solutions
[Table of contents](#table-of-contents)


## problem 1:
**How to make informed choices?**  
I have studied the various options in GitHub Actions, Gunicorn, Linux systemd, with a focus on definitions.  
Then made choices: e.g. SSH pair instead of Digital Ocean Personal Access Token, git pull instead of  
appleboy/scp-action@master, list all commands in yaml instead of creating bash.sh file, etc.  
For each choice to be made, I have tried to choose the easiest alternative. 

## problem 2:
**How to distinguish between one-time preparation (e.g. config of gunicorn and nginx) and recurrent  
activities in the yaml-workflow (e.g. systemctl restart cd.service)?**  
I have created a step-by-step plan for both, based on desk research, google foo and trying things out.  
This resulted in 3 buckets: one-time preparation, yaml-workflow, not necessary. 


## problem 3:
**How to implement ssh correcly?**  
I need 2 ssh connections: (A) to connect from GitHub Actions to the Droplet and (then being on the  
droplet) (B) vice versa, so I can do a git clone (manually in preparation phase) and subsequently let  
the GitHub Actions workflow do git pull (when triggered by a git push).  
Both ssh connections need their own implentation: e.g. for (A) I need GitHub secrets and for  
(B) I must associate a SSH public key with my GitHub account. 

<br/>
<br/>