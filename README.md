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
```bash
 Run the app.py file in the code  
```

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

Still needed to add the condition checking functionality, 

## License

[MIT](https://choosealicense.com/licenses/mit/)