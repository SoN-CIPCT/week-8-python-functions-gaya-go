# Week8-Functions
# Create a function that accepts a list of sandwich ingredients.
# The function should have one parameter that can collect as many arguments as the function call provides.
# The function should print a summary of the sandwich being ordered.
def make_sandwich(*ingredients):
    print('\nSandwich Order Summary:')
    print('You ordered a sandwich with the following ingredients:')

    for ingredient in ingredients:
        print(f'- {ingredient}')

# Call the function two times with a different number of arguments. 
# First function call
make_sandwich("Turkey", "Cheese", "Lettuce")
# Second function call
make_sandwich("Salmon", "Onion", "Tomato", "Lettuce", "Cream cheese")
