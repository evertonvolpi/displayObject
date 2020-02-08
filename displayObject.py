# --------------------------- D I S P L A Y    O B J E C T ---------------------------

from gfxhat import backlight, lcd

# --- Main function:
def displayObject(obj,x,y):
    def aValue(obj): # returns the lenght of the main list -1. Objective: print axis Y
        a = (len(obj))-1
        return(a)
    a = aValue(obj)
    ay = y+a # update the value of y to set the correct starting point

    def bValue(a, obj): # returns the lenght of the lists inside of the main list -1. Objective: print axis X
        b = (len(obj[a]))-1
        return(b)
    
    while(a>=0):
        b = bValue(a, obj)
        bx = x+b # update the value of x to set the correct starting point
        while(b>=0):
            w = (obj[a][b])
            lcd.set_pixel(bx,ay,w)
            lcd.show()
            b-=1
            bx-=1
        a-=1
        ay-=1

#--- Objects to be printed:
f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

# --- Menu:
def mainMenu():
    choice = input("""Select the object you would like to print (enter the number of your choice)
    1 - F1 Car
    2 - PacMan
    3 - Exit
    > """)
    if(choice == '1'):
        x = int(input("Enter the point of start in axis X > "))
        y = int(input("Enter the point of start in axis Y > "))
        displayObject(f1,x,y)
        input("Press enter to clear the screen and go back to the main menu")
        clearScreen()
        mainMenu()
    elif(choice == '2'):
        x = int(input("Enter the point of start in axis X > "))
        y = int(input("Enter the point of start in axis Y > "))
        displayObject(pm,x,y)
        input("Press enter to clear the screen and go back to the main menu")
        clearScreen()
        mainMenu()
    elif(choice == '3'):
        print("Goodbye!")
        clearScreen()
        backlightOff()
    else:
        print("Invalid choice.")
        mainMenu()

# --- Side funtions:
def clearScreen():
    lcd.clear()
    lcd.show()

def backlightOff():
    backlight.set_all(0,0,0)
    backlight.show()

def backlightOn():
    backlight.set_all(255,255,255)
    backlight.show()

# --- Start test:
backlightOn()
mainMenu()