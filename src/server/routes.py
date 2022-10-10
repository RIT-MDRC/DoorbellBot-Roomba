
def door():
    return (200, "Sending The Roomba To The Door")

def elevator():
    return (200, "Sending The Roomba To The Elevator")

def other():
    return(404, "Not sure where you're going bud")

REQUESTS = {
    "door" : door,
    "elevator": elevator
}
