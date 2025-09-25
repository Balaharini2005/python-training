while True:
    user = input("you:")
    if user.lower() in ["hello"]:
        print("bot:hii")
    elif user.lower() in ["tell me about data analytics"]:
        print("bot:yes ofcourse")
    elif user.lower() in ["what is data analytics?"]:
        print("bot:it is used to store the datas and collecting organizing large datasets")                  
    elif user.lower() in ["explain"]:
        print("bot:ok")
    elif user.lower() in ["give me"]:
        print("bot:manipulating structure and datas")
    else:
        print("bot:i didn't understand your qwestion")
