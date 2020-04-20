from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User, Course, Enrollment
from application.forms import Loginform, RegisterForm


 
""" courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}] """



@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index = True)

@app.route('/login', methods=['GET','POST'])
def login():

    #if user already loged in jsut check for username
    if session.get('username'):
        return redirect(url_for('index'))

    form = Loginform()

    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()

        if user and password == user.get_password(password):    #will not work because of hashed use for later
        #if user and password == user.password:
            flash(f"{user.first_name}, You have successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name

            return redirect('/index')
        else:
            flash(f'Sorry, there seems to be a problem', 'danger')

    return render_template("login.html", title="Login", form=form, login = True)

# Logout route

@app.route('/logout')
def logout():
        session['user_id'] = False
        session.pop('username', None)
        return redirect(url_for('index'))


# Courses Route

@app.route('/courses/')      #added second forward slash to pattern v1.49a
@app.route('/courses/<term>')
def courses(term = None):

    if term is None:
        term = "Spring 2019"

    # classes = Course.objects.all()
    classes = Course.objects.order_by("+courseID")     #change + to - for revers sort

    return render_template("courses.html", courseData = classes, courses = True, term = term)

# Registration route

@app.route('/register', methods=['GET','POST'])
def register():

    #if user already loged in jsut check for username
    if session.get('username'):
        return redirect(url_for('index'))

    rform = RegisterForm()

    if rform.validate_on_submit():

        user_id     =   User.objects.count()      #get number of objects in database table
        user_id     +=  1                        #add 1 to user_id to get next available id in table

        #get the user data populate the data fields from rform

        email       =   rform.email.data
        password    =   rform.password.data
        first_name  =   rform.first_name.data
        last_name   =   rform.last_name.data

        #save the data remember to hash password before saing
        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are now successfully registered", "success")
        return redirect(url_for('index'))

    else:
        pass

    return render_template("register.html", title="New User Registration", rform = rform, register = True)



    # Added data request and enrollment link V1.40a added GET, POST methods in 1.40b also need to change
    # to form from args so POST will recieve data
@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():

    #if user already loged in jsut check for username
    if not session.get('username'):
        return redirect(url_for('index'))

    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    # user_id = 1      #for testing in future will be session varialbe v3.4
    user_id = session.get('user_id')

    if courseID:        #check if coming from enrollment page ID will be present in form 
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"Error, you are already registered for this course {courseID}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()               # SAVE data to data base
            flash(f"You are succesffully enrolled in course {courseTitle} {courseID}!", "success")

    
    #classes = None
    classes = list( User.objects.aggregate(*[
           {
                '$lookup': {
                    'from': 'enrollment', 
                    'localField': 'user_id', 
                    'foreignField': 'user_id', 
                    'as': 'r1'
                }
            }, {
                '$unwind': {
                    'path': '$r1', 
                    'includeArrayIndex': 'r1_id', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'course', 
                    'localField': 'r1.courseID', 
                    'foreignField': 'courseID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'user_id': user_id
                }
            }, {
                '$sort': {
                    'courseID': 1
                }
            }
        ]))


    #term = request.form.get('term')                        removed in version not needed anymore.
    #return render_template("enrollment.html", enrollment = True, data={"id":course, "title":title, "term":term})
    return render_template("enrollment.html", enrollment = True, title="Enrollment", classes=classes)


    

# api route return response as a json v1.50 can use response to dump data to whatever needed or create api's
""" @app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):

    if (idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json") """



# User Route to Database

@app.route("/user")
def user():
    users = User.objects.all()
    print(users)
    return render_template("user.html", users=users)

