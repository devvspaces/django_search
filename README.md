# Django Postgres Full Text Search
> I will perform full text searches of your database in your Django apps. You'll need Postgres to do this, because you are actually using Postgres' built-in full text search functionality through Django. This is to be used on another project to use this algorithm feature to give users better search results. This is a very amazing method for searching, but only works with postgres. I don't know if other databases have this implementation yet :-).
> Used Factory boy to generate random data to populate database when starting project.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/devvspaces/readme_template/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/devvspaces/readme_template/issues)


![](https://www.logistec.com/wp-content/uploads/2017/12/placeholder.png)


## Requirements  (Prerequisites)
Tools and packages required to successfully install this project:
* Postgres Database [Documentation](https://www.postgresql.org/docs/current/textsearch.html)
* Python 3 and up [Python Install](https://www.python.org/downloads/)
* Django
* Factory Boy - For generating readable and resonable random data
All python main requirement and package versions are in the requirement.txt file in the root directory.

## Installation
A step by step list of commands / guide that informs how to install an run this project. 

#### Postgres Database setup For Linux and OS X

`$ sudo apt update`

If you don't have python and postgres

`$ sudo apt install python3-pip python3-dev postgresql postgresql-contrib`

Login to postgres shell

`sudo -u postgres psql`

Create new database with required permissions and extenstions. Remember to replace things like `<YOUR_DB_NAME>` with your own data and save somewhere. It will be used in django settings configuration.

```sh
CREATE DATABASE <YOUR_DB_NAME>;
CREATE USER <YOUR_DB_USER_NAME> WITH PASSWORD '<YOUR_DB_PASSWORD>';
ALTER ROLE <YOUR_DB_USER_NAME> SET client_encoding TO 'utf8';
ALTER ROLE <YOUR_DB_USER_NAME> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <YOUR_DB_USER_NAME> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <YOUR_DB_NAME> TO <YOUR_DB_USER_NAME>;
\c django_search_db
CREATE EXTENSION pg_trgm;
\q
```


#### Postgres Database setup For Windows

> Installing Postgres Method 1:

Install wsl on Windows to use linux on windows and then follow Linux and OS X method for installing Postgres [How to](https://adamtheautomator.com/windows-subsystem-for-linux/)

> Method 2:

Use Elephant SQL [Website](https://www.elephantsql.com/) and [How to](https://youtu.be/139a0fm0YFY?list=RDCMUC-QDfvrRIDB6F0bIO4I4HkQ&t=107)


### Project main setup

If you have your postgres database and user setup, you can do the below;

Clone the repo

`git clone https://github.com/devvspaces/django_search`

Move into repo directory

`cd django_search`

Create virutal enviroment

`python -m venv project_venv_name` or `python3 -m venv project_venv_name`

Install requirements

`pip install -r requirements.txt`

Move into project main directory

`cd searcher`

Create .env file

```sh
DEBUG=True
SECRET_KEY=<YOUR_SECRET_KEY>

DB_NAME=<YOUR_DB_NAME>
DB_USER=<YOUR_DB_USER_NAME>
DB_PASSWORD=<YOUR_DB_PASSWORD>
```

Run migrate

`python manage.py migrate`

Run server

`python manage.py runserver`

 
## Screenshots
Use this space to give a little demo of your project. Attach important screenshots if applicable. This section is optional and might not be applicable in some cases.

![Screenshots of projects](https://drive.google.com/file/d/1_H89nqPlrqg0jxqbHf9kxd-wLDmHEjB6/view?usp=sharing)

## Features
* Single Full text search
* Multiple Vectors and Query search
* Multiple Vectors and Query search with weights
* SearchHeadline for Marking search query on result in bold or as specified
* SearchRank (order results by how much they match to query with rank numbers)
* TrigramSimilarity and TrigramWordSimilarity

Will be good to check django docs on full text search [Django Documentation on Full text search](https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/search/)



## Tech Stack / Built With
1. [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
2. [Postgres](https://www.postgresql.org/)  - The World's Most Advanced Open Source Relational Database
3. [Python](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.

## How to Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

Steps to contribute:
1. Fork this repository
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

Additionally you can create another document called CONTRIBUTING.md which gives instructions about how to contribute. 

## Authors
 
Ayanwola Ayomide  – sketcherslodge@gmail.com
 
 You can find me here at:
[Github](https://github.com/devvspaces)
[LinkedIn](https://www.linkedin.com/in/netrobe-webby-878920194/)

## Credits

A heartfelt thank you to [@prettyprinted](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) for the knowledge I needed to get this idea off the ground and start writing!

Much love to the Django team for making this possible on django ❤️