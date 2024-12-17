import time
import datetime


print ("ALARM!!!")                                                                                  #"displays the message "ALARM"
current_time = datetime.datetime(2024, 10, 23, 6, 30, 0)                                            #sets the current time to 6:30 AM
print(current_time.strftime("%H:%M:%S"), end='\r')                                                   #displays the current time as hours,minutes and secs
days = ['A','B','C','D','E','F','G','H']                                                            #displays all of the days of the cycle
classes = ['seminar', 'comp sci', 'history', 'english','math', 'study hall', 'spanish', 'biology']   # displays all my classes

while True:                                                                                         #forever loop
   snooze=str.lower(input("\nSnooze? y/n: "))                                                       #choose if you want to snooze or not
   if snooze==("y"):                                                                                # snooze equals yes 
      print("go back to sleep")                                                                     # displays message "                                                              
      time.sleep(3)                                                                                  # wait 3 secs to continue the code
      current_time += datetime.timedelta(minutes=5)                                                 # if you go back sleep add 5 mins
   elif(snooze=="n"):                                                                               # snooze equals no
      print("get up")                                                                               # displays message
      current_time += datetime.timedelta (minutes=1)                                                # if you don't go back to sleep add 1 min
      break                                                                                         # terminates forever loop
   else:
      print ("invalid response")                                                                    # user response is invalid                                                                                            
print(current_time.strftime("%H:%M:%S"), end='\r')                                                  # displays current time 
print("\ngo to the bathroom")                                                                       #displays message
current_time += datetime.timedelta (minutes=2)                                                      # adds 2 mins when you go to the bathroom
print(current_time.strftime("%H:%M:%S"), end='\r')                                                  # displays current time 
print("brush your teeth")                                                                           #displays message                                                                  
print("\nturn on the shower")                                                                       # displays message
current_time += datetime.timedelta (minutes=2)                                                      # adds 2 mins when you turn on the shower
print(current_time.strftime("%H:%M:%S"), end='\r')                                                     # displays current time

while True:                                                                                         # forever loop
    showertemp=input("\nWhat temperature is the shower? hot/cold ").lower()                       # Question: Is the shower hot or cold  
    if showertemp==("hot"):                                                                        # Is the shower hot?
        print("\nget in the shower")                                                               # displays message 
        current_time += datetime.timedelta (minutes=1)                                             # adds 1 min when you get in the shower
        print(current_time.strftime("%H:%M:%S"), end='\r')      
        break                                                                                       # terminates statement
    elif showertemp==("cold"):                                                                     # is the shower hot?                                                      
        print("wait 1 more min")                                                                   # displays message
        time.sleep(5)                                                                              # delays code by 5 seconds when shower is cold
    else:
        print("invalid response")                                                                  # user response is invalid 

print(current_time.strftime("%H:%M:%S"), end='\r')                                                 # displays current time

while True:                                                                                        # forever loop
    above_or_below=input("is it above or below 60 degrees? above/below: ").lower()                 # Question: is it above or below 60 degrees
    if(above_or_below=="above"):                                                                   # temperature is above 60 degrees
        current_time += datetime.timedelta (minutes=5)                                             # adds 5 mins when you figure out temperature                                            
        print(current_time.strftime("%H:%M:%S"), end='\r')                                        # displays current time 
        print("wear T shirt and shorts")                                                           # displays message 
        break                                                                                      # ends above loop
    elif(above_or_below=="below"):                                                                 # if not above temperature equals below 60 degrees
        print("wear long pants and long sleeves")                                                  # displays message
        break                                                                                      # terminates forever loop
    else:                                                                                          # if the user does not say above or below
      print("invalid response")                                                                    # user response is invalid
print("Get Dressed")                                                                               # displays message 

while True:                                                                                        # forever loop                                                                                   
   cereal_or_baconandeggs=input("cereal or bacon and eggs? ").lower()                              # Question: Cereal or bacon and eggs for breakfast
   if cereal_or_baconandeggs==("cereal"):                                                          # cereal is choosen
      print("eat cereal")                                                                          # displays message
      break                                                                                        # ends cereal loop
   elif cereal_or_baconandeggs==("baconandeggs"):                                                  # bacon and eggs is chosen instead of cereal
      print("eat baconandeggs")                                                                    # displays message
      break                                                                                        # terminates forever loop
   else:                                                                                           # cereal or B+E is not chosen
         print("invalid response")                                                                 # user response is invalid
while True:                                                                                        # forever loop
    print("go to school")                                                                          # displays message                                                                    
   Bus_or_Car=input("take the bus or the car? ").lower()                                           # question: take the bus or the car? 
   if Bus_or_Car==("bus"):                                                                         # the bus is chosen  
      print("take the bus and leave at 7:20")                                                      # displays message
        break                                                                                      # ends bus loop                                                                                              
    elif Bus_or_Car==("car"):                                                                      # car is choosen instead
      print("take the car and leave at 7:30 ")                                                     # displays message
      break                                                                                        # terminates forever loop
   else:                                                                                           # bus or car is not chosen
         print("invalid response")                                                                 # user response is invalid
print("arrive at school")                                                                          # displays message
print("go to class")                                                                               # displays message
while True:                                                                                        # forever loop
   whatdayisit=input("what day of the cycle is it? A/B/C/D/E/F/G/H ").upper()                      # Question: What day of the cycle is it
    if whatdayisit in days:                                                                        # 
      index = days.index(whatdayisit)
      print(f"go to {classes[index]}")                                                             # displays message
      break                                                                                        # terminates forever loop
   else:                                                                               
      print ("invalid response")                                                                   # user response is invalid
print("go to next class")                                                                          # displays message




