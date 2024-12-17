import random
import time 
while True:
    my_list= ["yes definitely!!","no not at all","maybe, I am not sure", "data is unclear", "ask again later"]
    eightball = input("ask the magic 8-ball a question")
    time.sleep(1)
    r=random.choice(my_list)
    print(r)

 
