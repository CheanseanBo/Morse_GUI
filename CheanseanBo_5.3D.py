from tkinter import*
import tkinter.font
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#Declare required variable
led = 8
dit = 1
dah = 3
intraspace = 1

GPIO.setup(led, GPIO.OUT)

#Setup GUI window
win = Tk()
win.title("CheanseanBo Morse Code")
myFont = tkinter.font.Font(family = "Calibri", size = 12)
#width x height of the window and position
win.geometry("250x130+300+300")

#Create the textbox so that the user can input data
user = Entry(win, width = 24)
user.grid(row = 0, column = 0)
    
#define a close function to exit the window
def close():
    GPIO.cleanup()
    win.destroy()
	
#Create dot function to flash LED in dot manner
def dot():
	GPIO.output(led, GPIO.HIGH)
	time.sleep(dit)
	GPIO.output(led, GPIO.LOW)
	time.sleep(intraspace)

#Create dash function to flash LED in dot manner	
def dash():
	GPIO.output(led, GPIO.HIGH)
	time.sleep(dah)
	GPIO.output(led, GPIO.LOW)
	time.sleep(intraspace)

#Create a function that shows it's the next character, or a 3 seconds delay before the next character
def interspace():
	time.sleep(intraspace + 2)

#Create a function that flash LED according to user input in Morse Code
def Morse(char):
	if(char.lower() == "a"):
		dot()
		dash()

	elif(char.lower() == "b"):		
		dash()
		dot()
		dot()
		dot()

	elif(char.lower() == "c"):
		dash()
		dot()
		dash()
		dot()

	elif(char.lower() == "d"):
		dash()
		dot()
		dot()

	elif(char.lower() == "e"):
		dot()

	elif(char.lower() == "f"):
		dot()
		dot()
		dash()
		dot()

	elif(char.lower() == "g"):
		dash()
		dash()
		dot()

	elif(char.lower() == "h"):	
		dot()
		dot()
		dot()
		dot()

	elif(char.lower() == "i"):
		dot()
		dot()

	elif(char.lower() == "j"):
		dot()
		dash()
		dash()
		dash()
		dash()

	elif(char.lower() == "k"):
		dash()
		dot()
		dash()

	elif(char.lower() == "l"):	
		dot()
		dash()
		dot()
		dot()	

	elif(char.lower() == "m"):	
		dash()
		dash()

	elif(char.lower() == "n"):
		dash()
		dot()

	elif(char.lower() == "o"):
		dash()
		dash()
		dash()

	elif(char.lower() == "p"):
		dot()
		dash()
		dash()
		dot()

	elif(char.lower() == "q"):
		dash()
		dash()
		dot()
		dash()

	elif(char.lower() == "r"):	
		dot()
		dash()
		dot()
		
	elif(char.lower() == "s"):
		dot()
		dot()
		dot()
		
	elif(char.lower() == "t"):
		dash()
		
	elif(char.lower() == "u"):
		dot()
		dot()
		dash()
		
	elif(char.lower() == "v"):	
		dot()
		dot()
		dot()
		dash()
		
	elif(char.lower() == "w"):	
		dot()
		dash()
		dash()
		
	elif(char.lower() == "x"):
		dash()
		dot()
		dot()
		dash()
		
	elif(char.lower() == "y"):
		dash()
		dot()
		dash()
		dash()
		
	elif(char.lower() == "z"):
		dash()
		dash()
		dot()
		dot()

#Create a function that react to when user click submit
def Click():
	#Store user input in a string variabel
	data = str(user.get())
	#Create a boolean variable
	Alp = True
	#Check if there's a character inside the input that is not a letter
	for check in data:
		if not check.isalpha():
			CheckAlp = Label(win, text = "Letters only please!")
			CheckAlp.grid(row = 3, column = 0)
			#If so, set the boolean to false
			Alp = False
	#Check with Boolean 
	if(Alp == True):
		#Check if user input data longer than 12 characters
		if(len(data) > 12):
			CheckLen = Label(win, text = "You can only enter 12 character")
			CheckLen.grid(row = 2, column = 0)
		#If it's all a letter and its less than or equal to 12 then
		else:
			for i in range(len(data) - 1):
				Morse(data[i])
				interspace()
			#This is for the last character
			Morse(data[len(data) - 1])
			
#create a button to submit
submitButton = Button(win, text = 'Submit', font = myFont,
                    command = Click, bg = 'white', height = 1, width = 24)
submitButton.grid(row = 1, column = 0)


#create buttons to exit on the window
closeButton = Button(win, text = 'Exit', font = myFont,
                    command = close, bg = 'red', height = 1,
                    width = 10)
closeButton.grid(row = 4, column = 0)

#exit window through the close function
win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()




