__author__ = "Brewski"


import models, database


import os, platform, time

def createNewPerson(name, email, user_pin, phone, relation,):
	role = "person"
	newPerson = models.Person(name, email, user_pin, phone, relation)
	database.addPerson(newPerson)

def setupPersons():
	numberofpersons = input('How many persons would you like to add to the home?\n The first person will be made the administrator.\n')
	current_person = 0
	createNewAdmin()
	current_person + 1
	while current_person <= int(numberofpersons) - 1:
	    createNewPerson()
	    current_person = current_person + 1


# person monitor functions ##############################################################################################################

def personsAtHome():

	"""
	get list of persons from the database and iterate through them checking
	for their presence on the local network, through use of static IPs and a
	ping function. Returns a list of persons who are home.
	"""

	persons = database.getAllPersons()
	persons_at_home = []
	for person in persons:						# ping person IP and set alarm state if nobody is home
		if ping(person.ip) == True:					# set alarm state to OFF
			persons_at_home.append(person.name)
			time.sleep(0.01)
		else:								# set alarm state to ON
			time.sleep(5)
			if ping(person.ip) == True:
				persons_at_home.append(person.name)		# wait 60 seconds, then ping the IP again to confirm person is gone, if so, break without adding to persons_at_home
	return persons_at_home



def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    if  platform.system().lower()=="windows":
        ping_str = "-n"
    else:
        ping_str = "-c"

    # Ping
    return os.system("ping " + ping_str + " 1 " + host) == 0
