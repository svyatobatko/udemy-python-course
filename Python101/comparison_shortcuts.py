# None = False
something = None
if something:
    print("This is true")
else:
    print("This is false")

# Empty string = False
something = ""
if something:
    print("This is true")
else:
    print("This is false")

# String with something = True
something = "something"
if something:
    print("This is true")
else:
    print("This is false")

# List with something = True
something = [1, 2, 3]
print("List")
if something:
    print("This is true")
else:
    print("This is false")
# Empty list = False
something = []
if something:
    print("This is true")
else:
    print("This is false")

# Set with something = True
something = {1, 2, 3}
print("Set")
if something:
    print("This is true")
else:
    print("This is false")
# Empty set = False
something = {}
if something:
    print("This is true")
else:
    print("This is false")

# Tuple with something = True
something = (1, 2, 3,)
print("Tuple")
if something:
    print("This is true")
else:
    print("This is false")
# Empty tuple = False
something = ()
if something:
    print("This is true")
else:
    print("This is false")
