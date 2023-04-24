# Tenx-Notebook-Server
This application is to demo a work flow that will be used for Summer 2023 internship project. Let's go over the notable technology, working our way inside out. 

## Database - SQLite

This part needs work. SQLite was just easy to get started. Not a real solution. 

## Python 3.11
This project runs on python 3.11. This is the latest version of Python. 

Why Python? 

#### Pros
* Well known (particularly to younger coders)
* Fast development
* Many plug and play packages to make life easy

#### Cons
* Slower than Java

### FastAPI and Uvicorn

Okay, so this one I hadn't heard of until recently, but it is REALLY cool. Uvicorn offers some code acceleration and acts as a nice base for serving up the REST API. 

But that isn't the magic sauce in my opinion. The cool part... It is SELF DOCUMENTING!! No more writing API guides in Google docs. It is built INTO the code. Heck yes! 

### Pydantic and SQLalchemy

Nothing really special here. They are cool packages, but nothing new. Very comparable to Java POJOs and JPA Hibernate. 

## Github

Okay. So all the above is fine.. why are we on Github? We have an internal git repo
Excellent question.... and welcome to my TED talk. 

### 1. Ease of Development - Codespaces

Ease of development? Our ec2 dev machines handle all that for us and they are great. Yup! But they can be better. How would you like to start a job and be coding with just a few clicks? Codespaces does exactly that. [DEMO]

This provides a few additional things. 
1. Zero trust
2. No devops ramp-up time / user profiles
3. Self contained and identical
4. Containers that can be IDENTICAL to production. Prod === Dev

Now, you may be thinking, "that's all great, but what about Jenkins?" I'm glad you asked!

### 2. Github Actions

This is essentially Githubs version of Jenkins. It has code linting, test runs... and fully CI/CD (More on this later). 

### 3. Dependabot

You know what sucks! 3PP. It seems like once a year at least, weeks or months have to be sunk into getting these stupid libraries to upgrade and work. It would be ideal if we did it more often, maybe every couple months or so, so that it was easier, but who has the time for that! Well, a bot. That's who. Dependabot runs WEEKLY! That's right. 3PP run WEEKLY. It doesn't just upgrade. It runs dependency checks. Nothing merges unless it is ALL green. Yeah, it is freaking cool. 

### 4. This. 
Yeah. This. Just this. I am tired of google docs. What if our effing docs existed WITH THE EFFING CODE!! There is a whole goddamn WIKI 5 tabs over! It is all freaking here! Nothing is lost. No searching for relevant docs. This repo is the end all be all of EVERYTHING. The buck stops here! 

![Barely Controlled Rage](https://media.giphy.com/media/TGUIq0O5s4XJSnefJ3/giphy.gif)

## Docker
I kinda skimmed over this with Codespaces

## 1Password
Oh yeah, and none of our secrets need leave 1Password. Muahahahaha. It all comes together. (I actually haven't implemented this part yet) TODO

![All coming together](https://media.giphy.com/media/KEYEpIngcmXlHetDqz/giphy.gif)




