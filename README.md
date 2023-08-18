## Get project
make folder to make it root directory.clone this project in the folder directory from this repository using:<bg>
git clone project_HTTPS_url
## create virtual environment
create virtual environment inside the root directory<br>
python -m venv 'name of your env file'

## activate environment variable
run:<br>
env/Scripts/activate<br>
this command will activate your virtual environment variable
## install requirement.txt file libary
pip install -r requirements.txt<br>
The above command will download necessay library in the virtual environment

## Handel environtment variable
create .env file in the root directory. inside this file keep project's private value with the variables<br>
like:<br>
SECRET_KEY=your project secret key without any quotation<br>
install python-dotenv to load the environment variable from the .env file.<br>
its already in the requirements.txt file.so no need to further installation<br>
in the settings.py file ,white:<br>
import os<br>
from dotenv import load_dotenv<br>
load_dotenv()<br>
now load the secret key value like:<br>
SECRET_KEY=os.environ.get(<your secret key variable name in the .env file you defined earlier with quotes>)<br>
## migrations,migrate, runserver
run :<br>
python manage.py makemigrations your_app_name<br>
python manage.py migrate your_app_name<br>
python manage.py migrate<br>
now run:<br>
python manage.py runserver

## deploy the project at PythonAnyWhere
This project is deployed on PythonAnyWhere platform for free<br>
see the guidelines here :https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/<br>
deployed link of the project: https://mmt37.pythonanywhere.com/

## Api  Testing
go to https://mmt37.pythonanywhere.com/ this link. and signup with credentials.<br>
https://mmt37.pythonanywhere.com/login-api<br> use this url in the api testing platform like postman<br>
give the username and password you just enter to sign up in the body of the api as json format and make a post request <br>
if user is authenticated then it will resposne back a token.you can use this token to authenticate other api<br>
https://mmt37.pythonanywhere.com/input-value/api<br>
use this url in the api testing platform and make a get request and provide the token in the header section<br>
Key=Authorization<br>
value=Token your token<br>
At last send the get request
