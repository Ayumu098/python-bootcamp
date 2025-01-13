from flask import Flask, request

app = Flask(__name__)

@app.get('/login')
def login_get():
    return """
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" name="username">
        
        <input type="submit">
    </form>
    """

@app.post('/login')
def login_post():
    username = request.form['username']
    return f'Form Submitted by {username}'

app.run()
