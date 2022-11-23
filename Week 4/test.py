




def check_word():
    if user_word[i] == wordly_word[i]:
        print(user_word[i].upper(), end="")
    elif user_word[i] in wordly_word:
        print(user_word[i].lower(), end="")
    else:
        print("_" ,end="")
    if user_word == wordly_word:
        return 1
    else:
        return 0
