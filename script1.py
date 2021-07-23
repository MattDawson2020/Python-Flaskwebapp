from flask import Flask, render_template
#import flask class object from library

app = Flask(__name__) 
# initilize flask object, __name__ assigns the name main to the app on this page, if imported it is assigned the name script1.py

@app.route('/')
#define the root route
def home():
    return render_template("home.html")
# it seems like the function being declared immediately below the route is what links the route to the controller/action

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)