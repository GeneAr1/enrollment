# How to set up the project 
# Using PowerShell   (make sure python in VScode set to version installed in diretoru)

# Install Python and Flask and other pre env tools

-    Download and insall latest Python from Python.org,  make sure pip installed

     cmdprompt   pip list   -- to see what you have already
                pip install virtualenv
                pip install Flask     --  install latest flask version



# Setup Python virtual env tool

-        create virtual enviorment
                py -m venv venv          creates virtual folder in project
                venv\Scripts\activate    run the activate in the venv folder

         if vevn shows on line it was successful
                pip install Flask       installs flask in virtual environment
                pip insall flask-wtf    installs wtf in venv

         in main folder create file .flaskenv  use it to set enviornment variables
                touch .flaskenv     in folder create 2 variables
                                    FLASK_ENV=develoopment   dev mode on
                                    FLASK_APP=app.py         main module name

                pip install python-dotenv     need to invoke the flaskenv file

                deativate   shuts down enviornment
                
# Run First Flask App

-                venv\Scripts\activate       Start the virt env
                pip freeze > requirements,txt   Create requirements file for reinstall

         to use requirements
                pip install -r requirements.txt




