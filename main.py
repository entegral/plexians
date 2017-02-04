from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
from twilio import twiml

import database, person_controller, send_sms

database.init_db()

app = Flask(__name__)

# bootstrap starter
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app.secret_key = "not so secrets"
# Setup routes - functions and routing related to the setup and configuration of the household

@app.route('/')
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != 'admin' or request.form["password"] !='admin':
            error = "Username/Password Incorrect"
        else:
            session['username'] = request.form['username']
            flash('Welcome to Plexians')
            return redirect(url_for('dashboard'))
    else:
        return render_template("login.html", error = error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard_bootstrap.html")

@app.route('/user_Page', methods=['GET'])
def user_Page():
    Persons = database.getAllPersons()
    return render_template('user_page.html', Persons=Persons)

@app.route('/user_Page/remove_Person', methods=['POST'])
def remove_Person():
    name_to_remove = request.form['removePerson']
    database.deletePerson(name_to_remove)
    return redirect(url_for('user_Page'))

@app.route('/user_Page/submit_Person', methods=['GET', 'POST'])
def submit_Person_data():
    if request.method == 'POST':
        first_name = request.form['first_name']
        email = request.form['email']
        last_name = request.form['last_name']
        phone = "+1" + request.form['phone']
        relation = request.form['relation']
        database.addPerson(first_name, email, last_name, phone, relation)
        return redirect(url_for('user_Page'))
    return render_template('user_page.html')

@app.route('/notify_users', methods=['GET'])
def notify_users():
    Persons = database.getAllPersons()
    return render_template('notify_users.html', Persons = Persons)

@app.route('/notify_users/all', methods=['POST'])
def notify_all_users():
    if request.method == 'POST':
        all_users = database.getAllPersons()
        send_sms.send_all(all_users, request.form['note'])
        return redirect(url_for('notify_users'))
    return render_template('notify_users.html')

@app.route('/notify_users/by_name', methods=['POST'])
def notify_user_by_name():
    if request.method == 'POST':
        user = database.getPersonByName(request.form['first_name'])
        send_sms.send_sms(user.phone, request.form['note'])
        return redirect(url_for('notify_users'))
    return render_template('notify_users.html')

@app.route('/sms', methods=['POST'])                                # This route will receive incoming sms POST requests
def sms():                                                          # from twilio, interpret them, and respond accordingly
    number = request.form['From']
    message_body = request.form['Body']
    send_sms.sms_reply(number, message_body)
    resp = twiml.Response()
    sender = database.getPersonByPhone(number)
    resp.message('Hey {}, your issue has been sent to the admin(s), they will send you a notification when the issue has been resolved. Thank you for your patience! '.format(sender.first_name, message_body))
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 6289, debug=True)
