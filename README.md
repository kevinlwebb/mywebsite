# My Website

## Website
https://.herokuapp.com/

## File Layout

    .
    ├── flaskapp
    │   ├── __init__.py                      # Flask file that runs app
    │   ├── routes.py                        # Flask file that contains endpoints
    │   ├── data
    │   │   └── machines.pkl                 # Pickle file of devices dictionary 
    │   ├── templates   
    │   │   └── index.html                   # Map page of web app
    │   └── static   
    ├── Procfile                             # Specifies commands executed on startup
    ├── run.py                               # Entry point for the application
    └── requirements.txt                     # List of libraries to be installed

## To Do
- Integrate Jinja to dynamically show items
  - Blogs
  - Projects