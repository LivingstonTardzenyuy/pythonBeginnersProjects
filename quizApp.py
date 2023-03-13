quiz={
    "question1": {
        "question": "What is the capital of Northwest Region: ",
        "answer": "Bamenda"
    },

    "question2": {
        "question": "What is the capital of west Region: ",
        "answer": "Bafoussam"
    },

    "question3": {
        "question": "What is the capital of SouthWest Region: ",
        "answer": "Buea"
    },

    "question4": {
        "question": "What is the capital of South Region: ",
        "answer": "Ebolowa"
    },

    "question5": {
        "question": "What is the capital of Littoral Region: ",
        "answer": "Douala"
    },

    "question6": {
        "question": "What is the capital of Center Region: ",
        "answer": "Yaounde"
    },

    "question7": {
        "question": "What is the capital of East Region: ",
        "answer": "Bertoua"
    },

    "question8": {
        "question": "What is the capital of Adamawa Region: ",
        "answer": "Ngoundere"
    },

    "question9": {
        "question": "What is the capital of North Region: ",
        "answer": "Garoua"
    },

    "question10": {
        "question": "What is the capital of Far North Region: ",
        "answer": "Maroua"
    },

}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer=input("Enter response: \n")
    
    if value['answer'].lower() == answer.lower():
        score= score+ 1
        print("Correct response")
        print("********************")


    else:
        print("the correct answer is" + value['answer'])
        print("********************")
        
print("Your total score is " + str(score))