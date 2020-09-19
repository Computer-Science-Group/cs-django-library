Django Library Management App
===

# Getting Started
## Notes before getting started
This project uses
- postgresql as a database
- django as backend
- python for programming language

You are expected to have a working PostgreSQL installation
and have an already setup database for the project.  
If not, please refer to the official website for more informations

If you're on Linux, replace the `python` and `pip` commands
with `python3` and `pip3`

## Setting up the environment for development
### Cloning the repository
Clone the repository using the command:
    
    git clone https://github.com/Computer-Science-Group/cs-django-library.git
or by using the download zip in your browser and extract it

Switch to that directory you extracted/downloaded

### Downloading python
**The python version used in this project is 3.7.8**  
To get started, you need to have python 3.7
installed along with pip and venv (or virtualenv)

You can get it from [here](https://www.python.org/downloads/release/python-379/)

For Linux, you can use your package manager or use pyenv for that

### Creating a virtual environment
#### Windows steps:
First create a virtual environemnt using the command:
    
    python -m venv venv
or if you use virtualenv

    python -m virtualenv venv

next source to your virtual envirnonment

    .\venv\Scripts\activate.bat
    
#### Linux Steps
Create a virtual environment using the command:

    python3 -m venv .venv
Notice the `.` before venv, **important**  
Next source it using
    
    source ./.venv/bin/activate

### Installing the needed libraries
Now that you have a working virtual environment, 
we need to install our dependencies  
Luckily, we have a requirements.txt file
containing all we need

    pip install -r requirements.txt
### Setting up needed configurations
First, you need to run the script `generate_random_key.py`
in the root folder

you can run it using the command:
        
        python generate_random_key.py
it will print out a key, copy it  
Next, create a `.env` file next to `manage.py`  
**IMPORTANT**  
The `.` in `.env` is mandatory, you cannot remove it

Open you `.env` file and add the following line to it

    SECRET_KEY=
then paste your copied key

then add the following line under your `SECRET_KEY`

    DATABASE_NAME=YourPostgreSQLDatabaseName
    DATABASE_USER=YourPostgreSQLUsername
    DATABASE_PASSWORD=YourPostgreSQLUserPassword

### Running the project
Finally, run the following commands:
    
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

If it runs without errors, open your browser to your
[localhost](http://localhost:8000) link, it should display a page

---
### Congrats, now you can start working

