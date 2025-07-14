from flask import Flask,render_template,redirect,request


app=Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html>  
    <body> 
    <h1>Welcome to My Flask App</h1>
    <form action="/greet" method="post">
    Enter your name: <input type="text" name="name">
    <input type="submit" value="Submit">
    </form>
    </body> 
    </html>
'''

@app.route('/greet',methods=['POST'])
def greet():
    name= request.form['name']
    return f"Hello, {name}! Welcome to my Flask app."

if __name__ == '__main__':
    app.run(debug=True)
    