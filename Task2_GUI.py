
from tkinter import *
import tkinter.messagebox as messageBox

frm = Tk()
frm.title("Simple Calculator")
frm.geometry("400x500")

num1Lbl = Label(frm,text="Number 1")
num1Lbl.grid(row=1,column= 1)

txtNum1 = Entry(frm,font="segeo 20",width=20)
txtNum1.grid(row=2,column= 1,padx=30,pady=10,columnspan=4)

options = StringVar()

addition = Radiobutton(frm,text="+",variable=options,value="Addition",font="segoe 15")
subtraction = Radiobutton(frm,text="-",variable=options,value="subtraction",font="segoe 15")
mulitpliction = Radiobutton(frm,text="*",variable=options,value="mulitpliction",font="segoe 15")
division = Radiobutton(frm,text="/",variable=options,value="division",font="segoe 15")

addition.grid(row=3,column=1)
subtraction.grid(row=3,column=2)
mulitpliction.grid(row=3,column=3)
division.grid(row=3,column=4)

options.set("Addition")


num2Lbl = Label(frm,text="Number 2")
num2Lbl.grid(row=7,column= 1,ipadx=20)

txtNum2 = Entry(frm,font="segeo 20",width=20)
txtNum2.grid(row=8,column= 1,columnspan=4)

resultLbl = Label(frm,text="Result")
resultLbl.grid(row=9,column= 1,pady=10)

txtResult = Entry(frm,font="segeo 20",width=20,state="readonly")
txtResult.grid(row=12,column= 1,columnspan=4)

def SetResult(value):
    txtResult.config(state="normal")
    txtResult.delete(0,"end")
    txtResult.insert(0,value)
    txtResult.config(state="readonly")

def Calculate():

    # if(not(txtNum1.get().isdecimal() and txtNum2.get().isdecimal())):
    #     messageBox.showerror("validation error","غير مسموح بإدخال أي شيء غير الأرقام !!")
    #     SetResult("")
    #     return

    # num1 = float(txtNum1.get())
    # num2 = float(txtNum2.get())

    try:
        # محاولة تحويل المدخلات إلى float (هذا التحويل سيفشل ويرمي ValueError إذا لم يكن المدخل رقماً)
        num1 = float(txtNum1.get())
        num2 = float(txtNum2.get())

    except ValueError:
        # إذا فشل التحويل، هذا يعني أن هناك حروف أو تنسيق خاطئ
        messageBox.showerror("validation error", "الرجاء إدخال أرقام صحيحة أو عشرية فقط في كلا الحقلين.")
        SetResult("")
        return

    option = options.get()

    if(option == "Addition"):
        result = num1 + num2
    elif(option == "subtraction"):
        result = num1 - num2
    elif(option == "mulitpliction"):
        result = num1 * num2
    else:
        if(num2 == 0):
            messageBox.showerror("validation error","غير مسموح القسمة على صفر !!")
            SetResult("")
            return
        result = num1/num2

    SetResult(result)  

btnCalculate = Button(frm,text="Calculate",font="segoe 15",command=Calculate)
btnCalculate.grid(row=13,column=2,pady=20)

frm.mainloop()