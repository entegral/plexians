from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

import database, Person_controller

database.init_db()

app = Flask(__name__)

# bootstrap starter
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app


# Setup routes - functions and routing related to the setup and configuration of the household

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard_bootstrap.html")

@app.route('/setup')
def setup_home():
    return render_template('setup_home.html')

@app.route('/setup_house')
def setup_house():
    house_in_db = database.getAllHouses()
    return render_template('setup_house.html', houses=house_in_db)

@app.route('/setup_Person')
def setup_Person():
    Persons = database.getAllPersons()
    return render_template('setup_Person.html', Persons=Persons)



@app.route('/setup/submit_Person', methods=['GET', 'POST'])
def submit_Person_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_pin = request.form['user_pin']
        phone = request.form['phone']
        relation = request.form['relation']
        return redirect(url_for('setup_Person'))
    return render_template('setup_Person.html')

@app.route('/remove_Person', methods=['POST'])
def remove_Person():
    name_to_remove = request.form['removePerson']
    database.deletePerson(name_to_remove)
    return redirect(url_for('setup_Person'))

@app.route('/test')
def testpage():
    return render_template('test.html')

@app.route('/animalfeeder')
def animalfeeder():
    pets_fed_today = database.getTodaysPetInfo()
    pets_fed_week = database.getThisWeeksPetInfo()
    return render_template('animalfeeder.html', today=pets_fed_today, week=pets_fed_week )

@app.route('/animals_fedam', methods=['POST'])
def animals_fedam():
    animalsam = True
    animalspm = False
    house_controller.animals_are_fed(animalsam, animalspm)
    return redirect(url_for('animalfeeder'))

@app.route('/animals_fedpm', methods=['POST'])
def animals_fedpm():
    todays_info = database.getTodaysPetInfo()
    if todays_info == None:
        animalsam = False
        animalspm = True
        house_controller.animals_are_fed(animalsam, animalspm)
    todays_info[0].fed_pm = True
    database.db_session.commit()
    return redirect(url_for('animalfeeder'))

@app.route('/chore_whore')
def chore_whore_home():
    return render_template('chore_whore.html')

@app.route('/add_chore')
def add_chore():
    return render_template('chore_whore.html')

@app.route('/delete_chore')
def delete_chore():
    return render_template('chore_whore.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 6289)
