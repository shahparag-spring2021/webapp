# webapp

## Bookstore application created using Python, Flask and SQLite

## Steps to run: 

1. Install python3 on your machine
2. Clone the repository
3. Navigate to the root directory (~/webapp)
4. Create aand activate a virtual environment using the below commands
    - 	python3 -m venv venv
    -   source venv/bin/activate
5. Install all project dependencies
    -   pip install -r requirements.txt
6. Create config.py in app/ directory with the below variables
    -   SECRET_KEY = 'create a big string'
    -   SQLALCHEMY_DATABASE_URI = 'sqlite:///webapp.sqlite'
    -   # SQLALCHEMY_DATABASE_URI = 'postgresql://<postgresql_username>:<postgresql_password>@localhost/webapp'
    -   SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    -   SQLALCHEMY_TRACK_MODIFICATIONS = False
7. Navigate to ~/webapp/app and run the application
    -   python3 app.py
8. Test all endpoints using Postman

References - 
    https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
    https://www.geeksforgeeks.org/password-validation-in-python/
    https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
    <!-- Test for demo -->
