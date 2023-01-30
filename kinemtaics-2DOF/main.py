
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

def calData():

     try:
        x = float(xEntry.get())
        y = float(yEntry.get())
        length1 = l1.get()
        length2 = l2.get()

        x = float(xEntry.get())
        y = float(yEntry.get())
        L1 = float(l1.get())
        L2 = float(l2.get())
        theta2 = (np.arccos((x ** 2 + y ** 2 - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)))
        theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))

        theta1 =np.degrees(theta1)
        theta2 = np.degrees(theta2)

        theta1Res = tk.Label(gui, text=f'{round(theta1, 2)} Degrees')
        theta1Res.config(font=("times new roman", 12), bg="white")
        theta1Res.place(x=460, y=90)


        theta2Res = tk.Label(gui, text=f'{round(theta2, 2)} Degrees')
        theta2Res.config(font=("times new roman", 12), bg="white")
        theta2Res.place(x=460, y=140)



        print(theta1, theta2)

        xPos = (float(length1)+float(length2))+50
        xNeg = ((float(length1)+float(length2))+50)*-1
        yPos = (float(length1)+float(length2))+10
        yNeg = ((float(length1)+float(length2))+10)*-1

        fig = Figure(figsize=(6,4))
        ax = fig.add_subplot()

        ax.scatter(x, y, color='black', marker='o')
        ax.plot()
        ax.set_xlim(xNeg, xPos)
        ax.set_ylim(yNeg, yPos)
        canvas = FigureCanvasTkAgg(fig, master=gui)
        canvas.draw()
        canvas.get_tk_widget().place(y=210, x=10)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)




     except:
        xEntry.delete(0, tk.END)
        yEntry.delete(0, tk.END)
        l1.delete(0, tk.END)
        l2.delete(0, tk.END)


def clearData():
    xEntry.delete(0, tk.END)
    yEntry.delete(0, tk.END)
    l1.delete(0, tk.END)
    l2.delete(0, tk.END)


    theta1Res.config(font=("times new roman", 12), bg="white" )
    theta1Res.place(x=460, y=90)


    theta2Res.config(font=("times new roman", 12), bg="white", text = "n/a")
    theta2Res.place(x=460, y=140)


    # graph section
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.plot()
    ax.set_xlim(-150, 150)
    ax.set_ylim(-100, 100)
    canvas = FigureCanvasTkAgg(fig, master=gui)
    canvas.draw()
    canvas.get_tk_widget().place(y=210, x=10)
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)




gui = tk.Tk()
gui.title("2DOF Inverse Kinematics")
gui.geometry("650x650")
gui.config(bg = "white")



#graph section
fig = Figure(figsize=(6,4))
ax = fig.add_subplot()
ax.plot()
ax.set_xlim(-150,150)
ax.set_ylim(-100,100)
canvas = FigureCanvasTkAgg(fig, master=gui)
canvas.draw()
canvas.get_tk_widget().place(y = 210,x =10)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

#title label
label = tk.Label(gui, text = "2DOF- Inverse Kinematics")
label.config(font = ("times new roman",18,"bold"), bg = "white")
label.place(x =200, y=0)


#Entrys and placement for x and y input and lavels
xLab = tk.Label(gui, text = "X Pos")
xLab.config(font = ("times new roman",12), bg = "white")
xLab.place(x =80, y =70)
xEntry = tk.Entry(gui)
xEntry.config(width =3, bg = "white")
xEntry.place(x=130, y =75)

yLab = tk.Label(gui, text = "Y Pos")
yLab.config(font = ("times new roman",12), bg = "white")
yLab.place(x =170, y =70)
yEntry = tk.Entry(gui)
yEntry.config(width =3, bg = "white")
yEntry.place(x=220, y =75)


#Arm 1
arm1 = tk.Label(gui, text = "Arm 1 Length")
arm1.config(font = ("times new roman",12), bg = "white")
arm1.place(x = 80, y =105)
l1 = tk.Entry(gui)
l1.config(bg = "white", width = 10)
l1.place(x = 180, y =110)


#arm2
arm2 = tk.Label(gui, text = "Arm 2 Length")
arm2.config(font = ("times new roman",12), bg = "white")
arm2.place(x = 80, y =150)
l2 = tk.Entry(gui)
l2.config(bg = "white", width = 10)
l2.place(x = 180, y =155)


#theta labels
theta1 = tk.Label(gui, text = "Theta 1:")
theta1.config(font = ("times new roman",12), bg = "white")
theta1.place(x =400, y =90)


theta2 = tk.Label(gui, text = "Theta 2:")
theta2.config(font = ("times new roman",12), bg = "white")
theta2.place(x =400, y =140)

theta1Res = tk.Label(gui, text= "n/a")
theta1Res.config(font=("times new roman", 12), bg="white")
theta1Res.place(x=460, y=90)

theta2Res = tk.Label(gui, text='n/a')
theta2Res.config(font=("times new roman", 12), bg="white")
theta2Res.place(x=460, y=140)




#calcualteButton
calButton = tk.Button(gui,text = "Calculate", command = calData)
calButton.place(x = 130, y = 185)

#clear Button
clearButton = tk.Button(gui,text = "Clear", command = clearData)
clearButton.place(x = 470, y = 185)

gui.mainloop()