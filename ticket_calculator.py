TICKET_PRICE = 10

tickets_remaining = 100


while tickets_remaining >= 1:
    print("There are {} tickets available for purchase. Order now before you miss your chance!".format(tickets_remaining))
    
    # Gather the user's name and assign it to a new variable.

    user_name = input("Please enter in a username to continue.   ")

    # Prompt the user by name and ask how many tickets they want.

    num_tickets = input(f"Welcome! {user_name}, how many tickets do you need?   ")
    num_tickets = int(num_tickets)
    
    if num_tickets > tickets_remaining:
        print(f"Sorry, there are only {tickets_remaining} ticket(s) remaining.")
        sys.exit()
    else: 
          # Calculate the price of number of tickets they want * ticket cost // Store that in variable.

        amount_due = num_tickets * TICKET_PRICE

        print(f"The total price of {num_tickets} tickets is ${amount_due}, or $10.00 per ticket.")

        # Prompt the user if they want to proceed. Y/N?

        answer = input(f"Would you like to proceed with your purchase of {num_tickets} tickets? Enter Y or N   ").lower()

        if answer == "y":
            print("Sold! Enjoy the show!")
            tickets_remaining -= num_tickets
        else:
            print(f"Thank you for considering the show {user_name}, have a nice day!")
else: 
    print("Sorry, the tickets are ALL sold out. Have a nice day.")
