#string concatenation 
#suppose we want to create a string that says subscribe to 
#youtuber = "Arathi Krishna A M" #some string

#a few ways to do this 
#print("subscribe to" + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb:")
famous_person = input("Famous person: ")

madlib =f"computer programming is so{adj}! It makesvme so exicted all the time  because  \
    I love to {verb1}. Stay hydrated and {verb2} like you are a {famous_person}!"

print(madlib)
