from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
 
root=Tk()
root.title("Canvas.Shapes")
root.geometry("600x600")

choose_color=Label(root, text="Choose a color :")
choose_color.place(relx=0.1, rely=0.8, anchor=CENTER)

startx=Label(root, text="start x :")
startx.place(relx=0.4, rely=0.8, anchor=CENTER)

starty=Label(root, text="start y :")
starty.place(relx=0.7, rely=0.8, anchor=CENTER)

endx=Label(root, text="end x :")
endx.place(relx=0.3, rely=0.9, anchor=CENTER)

endy=Label(root, text="end y :")
endy.place(relx=0.6, rely=0.9, anchor=CENTER)



cc_input_box=Entry(root)
cc_input_box.insert(0,"black")
fillcolor=["green","red","yellow","blue","purple","teal"]
di = ttk.Combobox(root,state="readonly", values = fillcolor, width=10)
di.place(relx=0.3, rely=0.8)
cc_input_box.place(relx=0.2, rely=0.8, anchor=CENTER)


sx_input_box=Entry(root)
sx_input_box.insert(0,"10")
d1=ttk.Combobox(root,state="readonly", values = coordinates_value, width=10)
d1.place(relx=0.6, rely=0.8)
sx_input_box.place(relx=0.5, rely=0.8, anchor=CENTER)

sy_input_box=Entry(root)
sy_input_box.insert(0,"10")
d2=ttk.Combobox(root,state="readonly", values = coordinates_value, width=10)
d2.place(relx=0.10, rely=0.8)
sy_input_box.place(relx=0.9, rely=0.8, anchor=CENTER)

ex_input_box=Entry(root)
ex_input_box.insert(0,"10")
d3=ttk.Combobox(root,state="readonly", values = coordinates_value, width=10)
d3.place(relx=0.5, rely=0.9)
ex_input_box.place(relx=0.4, rely=0.9, anchor=CENTER)

ey_input_box=Entry(root)
ey_input_box.insert(0,"10")
d4=ttk.Combobox(root,state="readonly", values = coordinates_value, width=10)
d4.place(relx=0.8, rely=0.9)
ey_input_box.place(relx=0.7, rely=0.9, anchor=CENTER)

coordinates_value=[100,200,300,400,500,600,700,800,900]

canvas=Canvas(root, width = 590, height=510, bg = "white", highlightbackground="silver")

    
canvas.pack()
root.mainloop()
