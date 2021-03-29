#system modules
from datetime import datetime

#3rd party modules
from flask import make_response,abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#Data to serve with our API
PEOPLE={
    "Farrell":{
        "fname":"Doug",
        "lname":"Farrell",
        "timestamp":get_timestamp()
    },
    "Brockman":{
        "fname":"Kent",
        "lname":"Brockman",
        "timestamp":get_timestamp()
    },
    "Esther":{
        "fname":"Bunny",
        "lname":"Esther",
        "timestamp":get_timestamp()
    },
}

#create a handler for our read (GET) people
def read_all():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    #does the person exist in people
    if lname in PEOPLE:
        person=PEOPLE.get(lname)

    #otherwise,nope,not found
    else:
        abort(
            404,"Person with last name {lname} not found".format(lname=lname)
        )
    
    return person

def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    #Does the person exist already
    if lname not in PEOPLE and lname is None:
        PEOPLE[lname]={
            "lname":lname,
            "fname":fname,
            "timestamp":get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname),201
        )

    #Otherwise there exist an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname)
        )


def update(lname,person):
    #Does the person exist in people
    if lname in PEOPLE:
        PEOPLE[lname]["fname"]=person.get("fname")
        PEOPLE[lname]["timestamp"]=get_timestamp()

        return PEOPLE[lname]

    #Otherwise,nope,that's an error
    else:
        abort(
            404,"Person with last name {lname} not found".format(lname=lname)
        )

def delete(lname):
    #Does the person to delete exist?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname),200
        )

    #otherwise,nope,person to delete not found
    else:
        abort(
            404,"Person with last name {lname} not found".format(lname=lname)
        )

