from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_one():
    return render_template('index.html', num=3, color="blue")

@app.route('/play/<int:num>')
def play_two(num):
    return render_template("index.html", num=num, color= "skyblue")

@app.route('/play/<int:num>/<string:color>')
def play_three(num, color):
    return render_template("index.html", num=num, color=color)

# I had to use the video walkthrough for this one, as well as the class/answers, but I think I understand it.  
# the /play creates a base route, and each one creates a path that adds more information and creating variables that are passed to the HTML
# in the html, we use jinja to repeat the html, which can inclued inline css.  A language in a lauanguage, neat!
# most of my issues came from not understanding the syntax, where / is neccisary (at the begining of each route), and i didn't 
# understand default routing.  I think I do now

if __name__=="__main__":
    app.run(debug=True) 
