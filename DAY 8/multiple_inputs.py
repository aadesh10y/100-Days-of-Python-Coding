# Functions with more than one inputs
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Aadesh","Kathmandu")    # This is positional argument
greet_with(location ="Kathmandu",name="Aadesh")  # This is keyword argument
