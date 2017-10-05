from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route('/validate_input', methods=['POST'] )
def validate_input():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = 'Not a valid username'

    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = 'Not a valid password'

    if len(verify) < 3 or len(verify) > 20 or ' ' in verify:
        verify_error = 'Not a valid password'

    if password != verify:
        verify_error = 'Passwords do not match'

    if len(email) > 0:
        if '@' not in email or '.' not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = 'Not a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome_page.html', username=username)
    else:
        return render_template('signup_form.html', username_error=username_error, password_error=password_error,
            verify_error=verify_error, email_error=email_error, username=username, password=password, verify=verify,
            email=email)            


app.run()