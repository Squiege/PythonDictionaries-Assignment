# Task 1
def menu():
    print("Devin's Ticket Handler!")
    print("New Ticket")
    print("Update Ticket")
    print("Display All Tickets")
    print("Quit")


def new_ticket(tickets, ticket_number, customer_name, customer_issue):
    if ticket_number not in tickets:
        tickets[ticket_number] = {"Customer:": customer_name, "Issue": customer_issue, "Status": "open"}
        print(f"Ticket ID {ticket_number} added")
    else:
        print(f"Ticket ID {ticket_number} already exists, please choose another ticket number.")


def update_ticket(tickets, ticket_number, status):
    if ticket_number in tickets:
        tickets[ticket_number]["Status"] = status
        print(f"Ticket ID {ticket_number} updated it's status to {status}")
    else:
        print(f"Ticket ID {ticket_number} does not exist...")

def all_tickets(tickets):
    for ticket, details in tickets.items():
        print(f"Ticket Number: {ticket}")
        for section, items in details.items():
            print(f"{section}: {items}")

service_tickets = {
    "1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    menu()
    user_input = input("What would you like to do? (new, update, view all, quit)").lower()
    if user_input == "new":
        tid = input("Please enter the ticket ID: ")
        cn = input("Please enter the customers name: ")
        cis = input("Please enter the customers issue: ")
        new_ticket(service_tickets, tid, cn, cis)
    elif user_input == "update":
        tid = input("Please enter the ticket ID: ")
        status = input("What would you like to change the status to? (open/closed)")
        update_ticket(service_tickets, tid, status)
    elif user_input == "view all":
        all_tickets(service_tickets)
    elif user_input == "quit":
        quit()
    else:
        print("Sorry I dont understand.")
