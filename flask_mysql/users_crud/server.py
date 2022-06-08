
from flask import Flask, redirect, render_template,request
from user import User

app = Flask(__name__)
app.secret_key = "root"

#Routes go here

@app.route ('/')
def index ():
    #needs to go to database and grab all users
    all_users = User.get_all()

    return render_template("index.html", users = all_users)

@app.route("/user/new")
def new_user():
    return render_template("new_user.html")
    

@app.route("/user/create", methods= ["POST"])
def create_user():
    #collect form data 
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form ['last_name'],
        "email": request.form ['email']
    }
    #send data to database
    User.create(data)
    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)
