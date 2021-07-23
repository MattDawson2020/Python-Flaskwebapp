from flask import Flask
#import flask class object from library

app = Flask(__name__) 
# initilize flask object, __name__ assigns the name main to the app on this page, if imported it is assigned the name script1.py

@app.route('/')
#define the root route
def home():
    return "Website content goes here!"
# it seems like the function being declared immediately below the route is what links the route to the controller/action

@app.route('/about')
def about():
    return "Details go here"

if __name__ == "__main__":
    app.run(debug=True)