from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from application.models import User, Course, Enrollment
from application.forms import Loginform, RegisterForm



courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]



@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index = True)

@app.route('/login', methods=['GET','POST'])
def login():
    form = Loginform()

    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()

        # if user and password == user.get_password(password):    iell not work because of hashed use for later
        if user and password == user.password:
            flash(f"{user.first_name}, You have successfully logged in!", "success")
            return redirect('/index')
        else:
            flash(f'Sorry, there seems to be a problem', 'danger')

    return render_template("login.html", title="Login", form=form, login = True)

@app.route('/courses/')      #added second forward slash to pattern v1.49a
@app.route('/courses/<term>')
def courses(term="Fall 2019"):
    return render_template("courses.html", courseData = courseData, courses = True, term = term)

# Registration route

@app.route('/register', methods=['GET','POST'])
def register():
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
    course = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment = True, data={"id":course, "title":title, "term":term})

# api route return response as a json v1.50 can use response to dump data to whatever needed or create api's
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):

    if (idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")



# User Route to Database

@app.route("/user")
def user():
    #User(user_id=1, first_name="Bubba", last_name="Redneck", email="bubba@imaredneck.com", password="Trumper16").save()
    #User(user_id=2, first_name="Cleatus", last_name="Dumbass", email="dumbass@imaredneck.com",password="1majorTrumper").save()
    users = User.objects.all()
    print(users)
    return render_template("user.html", users=users)

