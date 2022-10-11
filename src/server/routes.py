rqueue = []

def door():
    if len(rqueue) < 2 and 'door' in rqueue:
        rqueue.append('door')
        return (200, "Sending The Roomba To The Door")
    else
        return roomba_status()
        

def elevator():
    if len(rqueue) < 2 and 'elevator' in rqueue:
        rqueue.append('elevator')
        return (200, "Sending The Roomba To The Elevator")
    else
        return roomba_status()

def roomba_status():
    return (200, "The Roomba is currently headed to the " + rqueue[0] + " and then headed to the " + rqueue[1])

def other():
    return(404, "Not sure where you're going bud")

REQUESTS = {
    "door" : door,
    "elevator": elevator,
    "roomba-status": roomba-status
}
