from flask import Flask, render_template, redirect, url_for, request

# Dummy user data for validation
user_data = {"username": "Mahesh", "password": "Mahesh@12"}
app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == user_data['username'] and password == user_data['password']:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/exit",methods=['POST'])
def exit():
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
