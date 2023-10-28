import tkinter
from tkinter import messagebox

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.configure(bg='seashell3')
screen.minsize(width=300, height=300)

def calculate_bmi():
    global bmi
    kg = int(myEntry.get())
    cm = int(myEntry2.get())/ 100
    bmi = kg / (cm * cm)
    bmi = round(bmi, 2)
    bmi_index(bmi)
def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Result', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Result', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Result', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('Result', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('something went wrong!')
#label
myLabel = tkinter.Label(text="Enter your Weight(kg)",justify="center", bg="seashell3", font=('Arial',10,'normal'))
myLabel.pack(pady=(30, 0))

#entry
myEntry = tkinter.Entry(width=20)
myEntry.pack(pady=(10, 20))

#label2
myLabel2 = tkinter.Label(text="Enter your Height(cm)", justify="center", bg="seashell3", font=('Arial',10,'normal'))
myLabel2.pack()

#entry2
myEntry2 =tkinter.Entry(width=20)
myEntry2.pack(pady=10)

#button
myButton = tkinter.Button(text="Calculate", command=calculate_bmi)
myButton.pack(pady=10)




screen.mainloop()
