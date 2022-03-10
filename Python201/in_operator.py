my_answer = input("What is your answer? ")
options = ["rock", "paper", "scissors"]

if my_answer in options:
    print("That option is a viable option")
else:
    print("Wrong answer try again")

key = "name"
person = {
    "name": "Kalob",
    "profession": "Coding teacher",
}

if key in person:
    print("Name is a valid dictionary key in the person object")

all_set = {"Item 1", "Item 2", "Item 2", "Item 3"}
selected_set = "Item 2"
if selected_set in all_set:
    print(f"Selected set is {selected_set}, present in all_set")
else:
    print(f"Selected set is {selected_set}, this value is absent in all_set")
