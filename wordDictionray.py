#dictionary

#create a dic that has a key/value pair that represent a word and its defination
#collect input from the user, input is a word
#check if word is in dic
#print def

def main():
    myDictionary={
        'hi': 'a way of greetings',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in space'
    }
    while True:
        word=input("enter a word:")

        if word in myDictionary:
            print(word + ": ," + myDictionary[word])
main()