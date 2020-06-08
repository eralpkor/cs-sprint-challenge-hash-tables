#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create an array with number of elements
    route = [None] * length
    destinations = {}

    # loop through tickets to store next destinations
    for ticket in tickets:
        destinations[ticket.source] = ticket.destination

    # first tickey always starts with 'NONE', it's a starting point to build a chain
    next_destination = destinations['NONE'] # first 

    # check each ticket's next destination,
    # add to the route array. Stop when it's 'NONE'
    for current in range(0, length):
        # add to next destination
        route[current] = next_destination

        # get the next destination from dict
        next_destination = destinations[next_destination]

    return route




ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3) # ["PDX", "DCA", "NONE"]

print(ticket_1.source, ticket_1.destination)

print(result)
