![GitHub last commit](https://img.shields.io/github/last-commit/ewerttrewe/fullstack-real-estate-app?style=plastic) 


# Real Estate App
App made with: React, Django, DRF, Celery, Redis, PostgreSQL, NGNX, Docker and more...

> **Disclaimer:** This application provide backend service for Real Estate App where users are able to buy, sell, rent and auction properties. Front-end part of the app is only created to test if the NGINX used as reverse proxy would serve data on the same port as API, so it's not finished and there are not any current plans for future frontend development of this app. Also steps which you are about to read,in order to run this app on your local machine, assume that you have Visual Studio Code, Python >=3.6 and Node.js >=17.9.1, PostgreSQL >= 12.15.

In order to use app and test it on your local machine follow the steps below:

1. Open any CLI that is corresponding to your operating system and clone this repository to your local machine using git clone command <br>
  `git clone https://github.com/ewerttrewe/fullstack-real-estate-app.git`<br>
  
2. Cd to the project directory and fetch & merge the latest changes if necessary using:<br>
    2a.&nbsp;&nbsp;Let's say you cloned to `e.g. C:\Users\User\desktop`,after that cd to root directory of the project:<br>
        &nbsp;&nbsp;`cd ...desktop/fullstack-real-estate-app`<br>
    2b.&nbsp;&nbsp;Git pull to fetch and merge all the recent changes:<br>
        &nbsp;&nbsp;&nbsp;`git pull`<br>
3. If you look closely into project files, there is one folder and file you need to explicitly add to the root directory of your project:<br>
   Navigate to root directory of the project and type in your CLI:&nbsp;&nbsp;`code .` it will open the VSC with a project you cloned.<br>
   After that create empty folder called `logs` inside the root directory `...\fullstack-real-estate-app\logs` where all the logs defined in `fullstack-real-estate-app\real_estate\settings\base.py` file will be placed.<br><br>
   When logs folder is created the next step is to create file called `.env` which is for environment variables, this one also will lay down in root directory - `...\fullstack-real-estate-app\.env`, all the variables you need to define inside this file are listed in `...\fullstack-real-estate-app\.env.example`<br><br>
   In this project mailtrap was used as a fake SMTP server so you have to create account there [mailtrap](https://mailtrap.io/register/signup?ref=header) and fill the necessary variables in `.env` file specifically:<br>
   `EMAIL_HOST`<br>
   `EMAIL_HOST_USER`<br>
   `EMAIL_HOST_PASSWORD`<br>
   `EMAIL_PORT`<br><br>
also you will need your PostgreSQL credentials:<br>
`POSTGRES_ENGINE=django.db.backends.postgresql`<br>
`POSTGRES_USER`,<br>
`POSTGRES_PASSWORD`,<br>
`POSTGRES_DB=estate`, you should create database called `estate` in pgAdmin or via CLI in PostgreSQL,<br>
`PG_HOST=postgres-db`<br>
`PG_PORT=5432`<br><br>
as well as:<br>
django `SECRET_KEY`,<br>
`SIGNING_KEY`,this one you can create on your own (remember to make it as strong as possible) it is used by `SIMPLE_JWT` in `settings\base.py`, <br>
`ALLOWED_HOSTS="localhost 127.0.0.1 [::1] api"`,<br>
`CELERY_BROKER=redis://redis:6379/0`,<br>
`CELERY_BACKEND=redis://redis:6379/0`<br><br>
**remember that .env file should NOT have any whitespaces cause it will throw an error!**<br><br>

> **Disclaimer:** You can open a Python shell within the project's directory and run the following command to generate a new secret key:<br>
`python manage.py shell`<br>
`from django.core.management.utils import get_random_secret_key`<br>
`get_random_secret_key()`<br><br>

4. After that, create virtual environment for this project by navigating to the root directory and typing:<br>
&nbsp;`python -m venv env` and cd to that environment: `cd env`<br>
After that actiavte that virtual environment by typing down<br><br>
&nbsp; **Windows Users:**<br>
`.\Scripts\Activate.ps1`<br><br>
&nbsp; **Linux/macOS Users:**<br>
`source venv/bin/activate`<br><br>
5. If done with steps from 1-4,  next thing that should be done is to install all the modules and packages that are listed in `fullstack-real-estate-app\requirements.txt`<br><br>
To be able to do that cd to root directory where requirements.txt file sits and run pip command:<br>
 &nbsp;&nbsp;`pip install -r requirements.txt`<br>
You can check if all the packages are installed by typing `pip list`<br>
If on windows, in order to use `make` command you have to install choclatey, follow the instalation process on [choclatey](https://chocolatey.org/install)<br>
After that you can install make via `choco install make` command<br>
**Now you can use `make` command and also you can check your version of choclatey using `choco -?`**<br><br>
6. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).<br>
7. After installation run `make build` command in the CLI while being in root directory of the project.<br>
8. Containers should be up and running properly, you can check if indeed they are by running `docker ps` command<br>
9. Now you should create a super user with `make superuser` command.<br><br>
10. After all the steps from 1 - 9 you should be able to connect to all endpoints, particularly:<br><br>
&nbsp;&nbsp;`http://localhost:8080/supersecret/` which is for django admin page, you can log in to the page using credentials you created in previous step.<br>
&nbsp;&nbsp;`http://localhost:5557/` which is for Flower to monitor all the async request that are being made, please note that to test mail functionality as well as logging in and authentication you can use insomnia or postman and test particular endpoints which are defined in `urls.py` files.<br>
&nbsp;&nbsp;`http://localhost:8080/` which is endpoint for frontend client

