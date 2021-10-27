from flask import Flask

'''
Instance of Flask class will be our WSGI application. 
Python sets the __name__ variable to the module name, so the value of this variable will vary depending on the Python source file in which you use it.
'''

app = Flask(__name__) 

'''
@app.route("/") is a decorator which adds  extra functionalities to the existing function.
'''
@app.route("/")
@app.route("/home")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
