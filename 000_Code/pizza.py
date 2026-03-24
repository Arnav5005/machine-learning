def make_pizza(size,*toppings): # this star is important
    """Summarize the pizza we are about to make."""
    print('\nMaking a '+str(size)+'-inch pizza with the following topics: ')
    for topping in toppings:
        print('-'+topping)