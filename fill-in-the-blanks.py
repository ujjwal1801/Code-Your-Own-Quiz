#list containing the quiz of different difficulties
quiz=["Assassin's Creed is a franchise centered on an action-adventure video game series developed by __1__. It depicts a centuries-old struggle between the __2__, who fight for peace with free will, and the __3__, who desire peace through control. The protagonist of the franchise was __4__ Miles, who died in Assassin's Creed III.","Facebook is an online social media and social networking service based in Menlo Park, __1__. The Facebook website was launched on February 4, 2004, by __2__ Zuckerberg, along with fellow Harvard College students and roommates, __3__ Saverin, Andrew McCollum, __4__ Moskovitz, and Chris Hughes.","Python is a widely used high-level programming language for general-purpose programming, created by __1__ van Rossum and first released in 1991. An __2__ language, Python has a design philosophy which emphasizes code __3__, and a syntax which allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or __4__. The language provides constructs intended to enable writing clear programs on both a small and large scale."]

#list containing the answers to the blanks 
keys=[["ubisoft","assassins","templars","desmond"],["california","mark","eduardo","dustin"],["guido","interpreted","readability","java"]]

#function returning the chosen difficulty
def choose_difficulty():
    return int(raw_input("Now select your difficulty.\n1. Easy.\n2. Medium.\n3. Hard\n"))

#function replacing the blanks in the quiz
def replace_blank(blank,answer,current_quiz):
    temp = "__"+str(blank+1)+"__"
    new_quiz = current_quiz.replace(temp,current_key[blank])
    print new_quiz
    return new_quiz

#this function takes the answer from the user as an input, converts the string to lower case to check from the keys, prints a statement and return a value accordingly.
def answer_check(blank,current_key,current_quiz,tries):
    answer = raw_input("\n What do you think will come in place of __"+str(blank + 1)+"__\n")
    answer = answer.lower()
    if answer == current_key[blank]:
        print "Correct\n"
        
        return answer
    else:
        print "Wrong Choice. You have "+str(tries - 1)+" tries left\n"
        
        return False
    
            
            
#function starting the quiz. Calling the answer_check function and the main logic behind the quiz
def start_quiz(current_quiz,current_key):
    tries = 4
    max_blank = 4
    blank = 0
    print current_quiz
    
    while tries > 0 and blank < max_blank:
        flag = answer_check(blank,current_key,current_quiz,tries)
        if flag:
            current_quiz = replace_blank(blank,flag,current_quiz)
            blank = blank + 1
            if blank > 3:
                print "Congratulations!!! You won\n"
        else:
            tries = tries - 1
            if tries < 1:
                print "Sorry!!! You lost\n"
            

print "Welcome to the quiz.\nYou'll be given 4 tries to complete the quiz. Lose them and you lose the game. Get all correct to win.\n"

difficulty=choose_difficulty() - 1
current_quiz = quiz[difficulty]
current_key = keys[difficulty]
start_quiz(current_quiz,current_key)
















