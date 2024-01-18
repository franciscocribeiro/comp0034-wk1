from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}! Welcome to the Paralympics app!'
    return '''
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/user/<name>')
def personalized_home(name):
    return f'Hello {name}! Welcome to the Paralympics app!'

if __name__ == '__main__':
    app.run(debug=True)

