
def display_req(messages):
    print(messages)
    
def display_upcase(messages):
    new_messages = messages.upper()
    print(new_messages)

def display_lowcase(messages):
    new_messages = messages.lower()
    print(new_messages)
    
    
user_messages = input("what is your message? ")
    
    
display_req(user_messages)
display_lowcase(user_messages)
display_upcase(user_messages)
    