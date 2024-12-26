import json

with open('data.json','r') as f:
    chatbot=json.load(f) #chatbot me load karne k liye

def memory(): #function create to conversation with chatbot
    while True:
        Question=input("ASK SOMETHING (type 'exit' to quit): ")#user ask question
        if Question.lower() in chatbot:#agar question exist karta hai chatbot me tab print hoga
            print(chatbot[Question])
        elif Question.lower() =='exit':#agar user exit kerna chahe to
            print("Exiting the chat. Goodbye!")
            home()
        else:#aap ka diya hua input chatbot me exist nhi kerta hai to aap apna response dena chahate hai ..
            print("I don't understand that. Would you like to add a response? (yes/no)")
            add_response=input().strip.lower()
            if add_response=='yes':
                add_question_response(Question)#call function to add response
#new function banaya new question or uske response ke liye...
def add_question_response(question):
    respone=input(f"What should I response to '{question}'?")
    chatbot[question]=respone#add question response
    with open('data.json','w') as f:
        json.dump(chatbot,f)

        
    print(f"Added: '{question}'->'{respone}'")#  yha per conform ker rahe hai ki question ka response pair milgya hai
#main menu of the program
def home():
    while True:#infinite time tak chane ke liye while loop ka use kare
        print("\nWelcome! Choose any one option:")#koi ek number ko select ker ke option select kare
        print("1 - chatbot")#1
        print("2 - Add question")#2
        print("3 - View all questions")#3
        print("4 - Exit")#4
        option=int(input("Enter an option: "))#option dale

        if option==1:
            memory()# call memory function to interection
        elif option==2:#aapp quetion add  karna chahate hai

            print("\n once you are done enter /done in question")
            while True:
                question = input("Enter the question you want to add: ")#new question
                if question.lower()=='/done':
                    home()
                else:
                    add_question_response(question.lower())
        elif option==3:
            print("Current Question and Responses:")
            for q,r in chatbot.items():
                print(f"'{q}': '{r}'")
        elif option==4:
            print("Exiting... Goodbye!")
            break #conversion khatam karne ke liye
        else:
            print("Invalid option. please try again.")# app ne galat optin choice kiya hai


if __name__ == "__main__":
    home()#+
