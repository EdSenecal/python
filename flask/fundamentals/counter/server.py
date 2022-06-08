
# imports 
from flask import Flask, render_template, request,redirect,session
app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



#routes

@app.route('/')
def index():
    if 'count' not in session: 
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")

#okay, so session funcitons as a dictionary where you can hold things that is pre set up. creates a key pair, useful to know 
# variables can be created in python and accessed in the index, data stored temporarily.  
# I assume coding dojo does something likethis on the backend to see if you accessed the answers.


#active server
@app.route('/reset')
def reset():
    session.clear()	
    return redirect('/')	
    #couldn't get this to run, requires it to redirect somewhere
    #redirecting to the homepage, otherwise it returns a string.  



if __name__=="__main__":
    app.run(debug=True) 