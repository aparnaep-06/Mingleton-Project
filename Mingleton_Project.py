#Personalised love letter generator
def greeting(person_name):
    print("\nA sweet greeting helps in making your chances wide. \nChoose any greeting from below:")
    greeting_lines=[f"My dearest {person_name},",
        f"To the love of my life {person_name},",
        f"My beloved {person_name},",
        f"To my one and only {person_name},",
        f"Hey {person_name},"]
    for i in range(len(greeting_lines)):
        print(i+1,greeting_lines[i],end="\n")
    y=int(input("Enter your choice (1/2/3/4/5):"))
    if y==1 or y==2 or y==3 or y==4 or y==5:
        return(greeting_lines[y-1])
    else:
        print("Please choose a valid options from the list above")

def openingPara():
    print("\nLet's start with the opening paras. \nChoose any one from the options below:")
    opening_lines = ["Words seem inadequate to express the depth of my feelings for you."
        "Every moment with you feels like a dream come true.",
        "I find myself thinking of you constantly, and it fills my heart with joy.",
        "I wanted to take a moment to tell you how much you mean to me.",
        "I'm writing this letter because I can't keep my feelings inside any longer."]
    for i in range(len(opening_lines)):
        print(i+1,opening_lines[i],end="\n")
    c=int(input("Enter your choice (1/2/3/4/5):"))
    if c==1 or c==2 or c==3 or c==4 or c==5:
        return(opening_lines[c-1])
    else:
        print("Please choose a valid options from the list above")

def bodyPara():
    print("\nNow choose any option from below as the body of your letter:")
    general_body=["You've brought so much happiness into my life, and I can't imagine a day without you.",
        "My love for you grows stronger with each passing day.",
        "Being with you feels like coming home.",
        "You are my best friend, my confidant, and my soulmate.",
        "I am so lucky to have you in my life.",]
    for i in range(len(general_body)):
        print(i+1,general_body[i],end="\n")
    c=int(input("Enter your choice (1/2/3/4/5):"))
    if c==1 or c==2 or c==3 or c==4 or c==5:
        body1=general_body[c-1]
    else:
        print("Please choose a valid options from the list above")

    ask=input("\nDo you want aditional lines in the body? (Y/N):")
    if ask in "Yy":
        additional_phrases=["In a world full of fleeting moments, you are my forever.",
            "You make my soul dance in ways I never thought possible.",
            "No matter how far we drift, my heart will always find its way back to you.",
            "You are the melody in every love song I hear, and the peace in every silent moment I cherish.",
            "Loving you feels like coming home, no matter where we are."]
        for i in range(len(additional_phrases)):
            print(i+1,additional_phrases[i],end="\n")
        x=int(input("Enter choie(1/2/3/4/5):"))
        if x==1 or x==2 or x==3 or x==4 or x==5:
            body2=additional_phrases[x-1]
        else:
            print("Please choose a valid options from the list above")
        return(body1+body2)
    else:
        return(body1 )
    
def closingPara(your_name):
    print("\nEnd your letter graefully... Choose one:")
    closing_lines = [f"With all my love, always and forever, {your_name}",
        f"Yours eternally, {your_name}",
        f"Forever and always, {your_name}",
        f"I love you more than words can say, {your_name}",
        f"Thinking of you always, {your_name}"]
    for i in range(len(closing_lines)):
        print(i+1,closing_lines[i],end="\n")
    w=int(input("Enter choie(1/2/3/4/5):"))
    if w==1 or w==2 or w==3 or w==4 or w==5:
        return(closing_lines[w-1])
    else:
        print("Please choose a valid options from the list above")

def lovelettergenerator():
    print("Welcome to personalised love letter generator!!")
    print("Choose from options given to create a concise letter thet conveys your feelings to your loved ones...\nLet's start")
    your_name=input("Enter your name:")
    person_name=input("Enter the name of your love:")
    greet=greeting(person_name)
    open=openingPara()
    body=bodyPara()
    close=closingPara(your_name)
    print("Here's your letter:\n")
    print("\n")
    print(greet)
    print(open+body)
    print(close)
    print("\n")
    print("\nHope you liked the letter. Keep visiting!!")

lovelettergenerator()