from tkinter import *
import tkinter.messagebox
import math


##################################################################################################################################
root = Tk()
root.geometry("320x475+600+100")
root.iconbitmap(True, "c.ico")
root.title("Calculator")

switch = None

##################################################################################################################################
# Button on press


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


##################################################################################################################################


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '')


def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "deg"
    else:
        switch = None
        conv_btn['text'] = "rad"


def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


##################################################################################################################################
# Label

data = StringVar()

disp = Entry(
    root,
    text = "LABEL",
    font=("Segoe UI", 28, 'bold'),
    bd=0,
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
    justify=RIGHT
)
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH, padx=5, pady=5)

###################################################################################################################################
# Row 1 Buttons

btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=sin_clicked)
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=cos_clicked)
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=tan_clicked)
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow1, text="rad", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=conv_clicked)
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow1, text="ln", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=ln_clicked)
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow1, text="log", font="SegoeUI 12 bold", relief=GROOVE, activebackground="grey", bd=0, command=logarithm_clicked)
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

##################################################################################################################################
# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow2, text="(", font="SegoeUI 14 bold", relief=GROOVE, activebackground="grey", bd=0, command=bl_clicked)
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow2, text=")", font="SegoeUI 14 bold", relief=GROOVE, activebackground="grey", bd=0, command=br_clicked)
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow2, text="C", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btnc_clicked)
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow2, text="⌫", font="SegoeUI 10 bold", relief=GROOVE, activebackground="grey", bd=0, command=del_clicked)
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

##################################################################################################################################
# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow3, text="√x", font="SegoeUI 14 bold", relief=GROOVE, activebackground="grey", bd=0, command=sqr_clicked)
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow3, text="x!", font="SegoeUI 14 bold", relief=GROOVE, activebackground="grey", bd=0, command=fact_clicked)
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow3, text="π", font="SegoeUI 14 bold", relief=GROOVE, activebackground="grey", bd=0, command=pi_clicked)
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow3, text="/", font="SegoeUI 18 bold", relief=GROOVE, activebackground="grey", bd=0, command=btnd_clicked)
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

##################################################################################################################################
# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

btn7 = Button(btnrow4, text="7", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn7_clicked)
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow4, text="8", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn8_clicked)
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow4, text="9", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn9_clicked)
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow4, text="+", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btnp_clicked)
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

##################################################################################################################################
# Row 5 Buttons

btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)

btn4 = Button(btnrow5, text="4", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn4_clicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow5, text="5", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn5_clicked)
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow5, text="6", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn6_clicked)
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow5, text="*", font="SegoeUI 19 bold", relief=GROOVE, activebackground="grey", bd=0, command=btnml_clicked)
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

###################################################################################################################################
# Row 6 Buttons

btnrow6 = Frame(root)
btnrow6.pack(expand=TRUE, fill=BOTH)

btn1 = Button(btnrow6, text="1", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn1_clicked)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow6, text="2", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0,  command=btn2_clicked)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow6, text="3", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn3_clicked)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow6, text="-", font="SegoeUI 19 bold", relief=GROOVE, activebackground="grey", bd=0, command=btnm_clicked)
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)


###################################################################################################################################
# Row 7 Buttons

btnrow7 = Frame(root)
btnrow7.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow7, text="%", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=mod_clicked)
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow7, text="0", font="SegoeUI 16 bold", relief=GROOVE, activebackground="grey", bd=0, command=btn0_clicked)
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow7, text="•", font="SegoeUI 18", relief=GROOVE, activebackground="grey", bd=0, command=dot_clicked)
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow7, text="=", font="SegoeUI 17 bold", relief=GROOVE, activebackground="grey", bd=0, command=btneq_clicked, bg="#20bebe")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
