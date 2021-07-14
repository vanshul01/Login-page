# Login-page

PREREQUISITES AND TECHNOLOGIES USED:

Visual Studio
Visual Studio Code is a source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.
Django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
Django by default provides an authentication system configuration. User objects are the core of the authentication system. Today we will implement Django’s authentication system.
 
Django: Django install

Python
Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation
Libraries:
1.Pillow
Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. It is available for Windows, Mac OS X and Linux.
 
PostgreSQL (Database System)
PostgreSQL is a powerful, open-source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
1.Psycopg2
Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection).
2.Pgadmin
Pgadmin is the most popular and feature rich Open-Source administration and development platform for PostgreSQL, the most advanced Open-Source database in the world

Html
The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.

CSS
Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
Functionality 

Register a new user using username, password and email address.
Let the user sign in using sessions. (Small function to get the sum of two numbers by taking inputs from the user) 
logout the user

Setting up:
1.Download and install Visual Studio Code, python 3.9(64bit), PostgreSQL, Pgadmin

2.Check Pip, python versions for proper installation check

Code:

python –version

pip –version

Installing necessary modules
Code:
Pip install Django
Pip install psycopg2
Pip install pillow
3.Django admin (Run Django-admin version to display the current Django version)
Code:
django-admin --version
4.Make different set or project 
5.Now setup a new environment and activate it
Code:
Pip install virtualenvwrapper-win
mkvirtualenv test
Django-admin –version
Mkdir projects
Cd projects
Django -admin startproject login
Cd login
dir
6.Run Pgadmin and start the server
Code:
Python manage.py runserver
Then click on the http://localhost:8000 

