from tkinter import *  # import the module tkinter

import math   # import the module math for the scientific calculator

root = Tk() 
root.title("Scientific Calculator") # name of the app
root.geometry("400x400")  # to give size to the apps
root.configure(background = 'brown') # background of the app
 
calc = Frame(root)
calc.grid()

egg = Entry(root, font=("arial", 18, "bold"), width=50, borderwidth=5, relief=RIDGE, fg="white", bg="black", bd=10)
egg.grid(row=0, columnspan=6)  # entry or frame creates an interface where the button will be displayed

def click(values): # performs the function that will be carried out in the app
    ex = egg.get()
    answer = ""
    # print(values)
    try: # should there be any error that will occur
        if values=="C":
            ex=ex[0:len(ex)-1]
            egg.delete(0, END)
            egg.insert(0, ex)
            
        elif values == "CE":
            egg.delete(0, END)
        
        elif values == "√":
            answer = math.sqrt(int(float(ex))) 
            # answer = math.sqrt(int(eval(ex)))
        elif values ==  "π":
            answer = math.pi
            
        elif values == "cos":
            answer = math.cos(math.radians(eval(ex)))
            
        elif values == "sin":
            answer = math.sin(math.radians(eval(ex)))
            
        elif values == "tan":
            answer = math.tan(math.radians(eval(ex)))
            
        elif values == "cosh":
            answer = math.cosh(math.radians(eval(ex)))
            
        elif values == "sinh":
            answer = math.sinh(math.radians(eval(ex)))
            
        elif values == "tanh":
            answer = math.tanh(math.radians(eval(ex))) 
            
        elif values == "^":
            answer = eval(ex) ** 2
            
        elif values == "In":
            answer= math.log2(eval(ex))
            
        elif values == "deg":
            answer = math.degrees(eval(ex))
            
        elif values == "rad":
            answer = math.radians(eval(ex))
        
        elif values == "e":
            answer = math.exp
            
        elif values == "x!":
            answer = math.factorial(eval(ex))
        
        elif values == "/":
            egg.insert(END, "/")
            return
            
        elif values == "=":
            answer=eval(ex)
        else:
            egg.insert(END, values)
            return                                   
                        
        egg.delete(0, END)
        egg.insert(0, answer)
    except ValueError:
        pass          

text_lists = ["C", "CE", "√", "+", "π", "cos", "tan", "sin", "^",
              "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
              "4", "5", "6", "+", "In", "deg", "rad", "=", "*",
              "7", "8", "9", "%", "0", ".", "/", "(", ")", "e"]

rowvalue = 1
columnvalue = 0
for i in text_lists:
    
    btn = Button(root, width=6, height=3, bd=10, text=i, bg="blue", fg="black", activebackground="purple", 
                 relief=RAISED, command=lambda btn=i: click(btn))
    btn.grid(row=rowvalue, column=columnvalue, padx=10, pady=5)
    columnvalue += 1 # it will increase by 1
    if columnvalue>5:
        rowvalue+=1
        columnvalue=0   

root.mainloop() # for the app to be able to run