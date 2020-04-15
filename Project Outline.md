# Create an online enrollment app for conference

#   Version 1


****************************************************************
# 1.0
-   Create the enrollment application
-   run and configure dev env
-   create home page for application
        
        * Project structure
        * create application package
        * create the __init__.py file for applicateion
        * create directories for templates and static data
        * refactor the main.py module

*****************************************************************
# 1.1

-   create the config.py module
-   create a routes.py module for all routing patterns
-   modify the __init__.py 
*****************************************************************
# 1.2

-   create template for the home page (index.html)
-   import render_template function to render pages
-   include directive to include external files
******************************************************************
# 1.3 

-       create navigation menus for application
-       use url_for
-       use the route() decorator to bind a function to one or more URL patterns
-       use Jinja delimiters {{% %}}, {{  }}, {{#  #}}
-       Jinja   if statement
********************************************************************
# 1.4  

-       create base templates in JinJa
-       use inheritance to creat child templates
-       pass data using props
-       access data using request and response
# 1.40a
-       Url variables
-       HTTP methots (Get POST) for moving data
-       global objects:  REQUEST and RESPONSE 
-       Request and response JSON API format

-               Accessng Query String (GET)
@               request.args.get(<field_name>)
@               request.args[<field_name>]
-               Accessomg Query String (POST)
@               request.form.get(<field_name>)
@               request.form[<field_name>]

-       class flask.Response( see documentation )
-       creat enrollment form using GET
@               create the template
@               create the enrollment route (URL Pattern)
# 1.40b
-       update enrollment using POST method (secure)
-       add GET and POST methonds to Route
-       access form data using form object
# 1.5
-       Response Object
-       Create API to send JSON response