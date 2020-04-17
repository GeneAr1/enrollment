# Create an online enrollment app for conference

#   Version 1


****************************************************************
# 1.0
    Create the enrollment application
    run and configure dev env
    create home page for application
        
        * Project structure
        * create application package
        * create the __init__.py file for applicateion
        * create directories for templates and static data
        * refactor the main.py module

# 1.1

        create the config.py module
        create a routes.py module for all routing patterns
        modify the __init__.py 

# 1.2

        create template for the home page (index.html)
        import render_template function to render pages
        include directive to include external files

# 1.3 

        create navigation menus for application
        use url_for
        use the route() decorator to bind a function to one or more URL patterns
        use Jinja delimiters {{% %}}, {{  }}, {{#  #}}
        Jinja   if statement

# 1.4  

        create base templates in JinJa
        use inheritance to creat child templates
        pass data using props
        access data using request and response
# 1.40a
        Url variables
        HTTP methots (Get POST) for moving data
        global objects:  REQUEST and RESPONSE 
        Request and response JSON API format

                *Accessng Query String (GET)
                *request.args.get(<field_name>)
                *request.args[<field_name>]
                *Accessomg Query String (POST)
                *request.form.get(<field_name>)
                *request.form[<field_name>]

        class flask.Response( see documentation )
        creat enrollment form using GET
                *create the template
                *create the enrollment route (URL Pattern)
# 1.40b
        update enrollment using POST method (secure)
        add GET and POST methonds to Route
        access form data using form object
# 1.5
        Response Object
        Create API to send JSON response

************************************************************************
# 2.0   DataBase Addition

        install the MondoDB database for use in this application
        Install MongoEngine extension for Flask
        Set up the Databas
        Connect to Database
                *create documents and data
                *create the DataBase Model (Schema)
# 2.01
        Set up MongoDB database
                *MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }
        Import the Mongo Engin
                *From flask_mongoengine import MongoEngine
        Initalize the database object
                *db = MongoEnging()
                *db.init_app(app)
# 2.1
        Connect to MongoDB using MongoEngine OBJ
        hooking up a user colletcion using simple user model
        insert data into collection
        display collection to the view
# 2.2
        create collections to store documents(data)
        insert documents into collections
        use MongoDB shell commands
                *see mongo documentation shell quick reference
       
        Insert JSON data usine mongoimport.exe via command line
# 2.4
        create the data models module
                * create User model
                * create Course model
                * create Enrollment model

****************************************************************************
# 3.0   Web Forms And Flask Security Issues

        Instal and configure Flask-WTF and Flask-Security extensions
        Creating the login and registration pages
        Processing the form data and updating the database
        creating the courese enrollment pages
        creating sessions and authentication for users
# 3.00
        Flask-WTF extention for WTForms library
                * WTForms provides clean way to gnerate HTML form fields
                * Maintains a seperaton of code and presentation

        Flask Security Extension provies security and authentication features
                * Session-based authentication
                * Password hashing
                * Bassic HTTP and token-based authentication
                * User registration
                * Login tracking (Flask-Login)
                * Supports data persistency for Flask-SQLAlchemy, Flask-MongoEngine, flask-peewee and PonyORM
# 3.01
        Create login and registration page
        Create the form classes and update templates using WTFforms library
        Creat alerts using flash() method
        validate forms and show error messages via form
# 3.02
        Update Login Route and Login Template
                *update login route to capture data
                *update login template using WTForms lib
# 3.03  
        Create Alert messages lusing flash() method (source)
        Retrieve flash messages using get_flashed_messages()  (view)
# 3.04  
        Validate form data login form
        Show error messages inline for form fields (using form error)
        Style and format error message
                (need to go back and redo registration form to match login using WTF forms)
# 3.04a 
        Update registration form to match model 
        minor bug fix and field name changes
# 3.04b 
        update registration form to work with WTF Forms
# 3.10
        Form data Validation
        Processing form data for data base
        Hashing passwords using Werkzeug library
                *Hashing:
                        generate_password_hash('pw")
                *Unhashing:
                        check_password_hash(password, 'pw')
        add Werkzeug to project
        add new module to models.py to check and hash passwords\
        add new module to forms.py to validate emails in register class
        corrected imports on forms and model pages
# 3.20
        Update login route to interact with database
        Validate Email Address in User
# 3.21
        Update Registration route to interact with database
                * form validation
                * insert data into DB
                * verify inserted data using MongoDB Compass 
        





