# @TODO: Your code here
my_info = {"name": "Logan Gonzales",
           "occupation": "Billing Agent",
           "age": 28,
           "hobbies": ["painting", "drawing", "swimming", "reading", "hanging out with my family", "walking", "hiking", "singing"],
           "wake-up": {"Monday": 7, "Wednesday": 7, "Friday": 7, "Sunday":10}}

print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f'On the weekend I get up at {my_info["wake-up"]["Sunday"]}')

