## create virtual environment
make folder to make it root directory.create virtual environment inside the root directory
python -m venv <name of your env file>

## activate environment variable
run:
env/Scripts/activate
this command will activate your virtual environment variable
## install requirement.txt file libary
pip install -r requirements.txt
The above command will download necessay library in the virtual environment

## Handel environtment variable
create .env file in the root directory. inside this file keep project's private value with the variables
like:
SECRET_KEY=<your project secret key without any quotation>
install python-dotenv to load the environment variable from the .env file.
its already in the requirements.txt file.so no need to further installation
in the settings.py file ,white:
import os
from dotenv import load_dotenv
load_dotenv()
now load the secret key value like:
SECRET_KEY=os.environ.get(<your secret key variable name in the .env file you defined earlier with quotes>)
## migrations,migrate, runserver
run :
python manage.py makemigrations <app_name>
python manage.py migrate <app_name>
python manage.py migrate

now run:
python manage.py runserver

## deploy the project at PythonAnyWhere
This project is deployed on PythonAnyWhere platform for free
see the guidelines here :https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
deployed link of the project: https://mmt37.pythonanywhere.com/
