# Flask
# SQlAlchemy
# Sqlite
# Bcrypt



Flask is a web framework, it’s a Python module that lets you develop web applications easily. Flask framework are: There is a built-in development server and a fast debugger provided.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL

SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.

bcrypt is a password-hashing function


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask, SqlAlchemy, flask_sqlalchemy, bcrypt

```bash
pip install Flask
pip install sqlAlchemy
pip install Flask_sqlalchemy
pip install bcrypt
```
## How to Run

Install all the required modules and then

First replace 

db_connection_string in database.py with
as db_connection_string = "mysql+pymysql://username:password@host/database?charset=utf8mb4"

you can get these from the word file attached below
for some reason if it doesn't work just create your own database with the help of planetscale.com and connect a new database with all the given values and
then create the table with following query

```bash
 create table rules(
 id int auto_increment,
 triger varchar(100),
 cond varchar(100),
 val int ,
 act varchar(100),
 primary key(id)
 );
 After this 
 Run the app.py file in the code  
```
I committed the values before but it keep disconnecting the database for some reason when pushed to git

## Usage

```python
from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from sqlalchemy import create_engine,text,insert
from database import load_rules_from_db,add_rule_to_db,delete_rule_from_db
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

Still needed to add the condition checking functionality and when the code is pushed to git with the db values the connection gets cut off(Don't know why its happening and couldn't solve it ), So use the code in a private system and replace the db_connection_string given above 


## License

[MIT](https://choosealicense.com/licenses/mit/)
