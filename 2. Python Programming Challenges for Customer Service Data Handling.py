# Initial customer service ticket data
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(customer, issue):
    ticket_id = "Ticket" + str(len(service_tickets) + 1).zfill(3)  # Generate unique ticket ID
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
    print(f"Opened new ticket {ticket_id} for {customer}: {issue}")

# Function to update the status of a ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Updated status of ticket {ticket_id} to {new_status}")
    else:
        print(f"Ticket {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    if status:
        filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in service_tickets.items() if ticket_info["Status"] == status}
        print(f"Tickets with status '{status}':")
        for ticket_id, ticket_info in filtered_tickets.items():
            print(f"{ticket_id}: Customer {ticket_info['Customer']}, Issue: {ticket_info['Issue']}")
    else:
        print("All Tickets:")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"{ticket_id}: Customer {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

# Example usage:

# Opening new tickets
open_ticket("Eve", "Website down")
open_ticket("Charlie", "Product inquiry")

# Updating ticket status
update_ticket_status("Ticket001", "closed")

# Displaying all tickets
display_tickets()

# Displaying only open tickets
display_tickets("open")

