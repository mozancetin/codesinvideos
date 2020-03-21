from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.title("BMI Hesaplayıcı")
root.resizable(0,0)

bottom = Frame(root)
bottom.pack(side = BOTTOM)

bot = Frame(root)
bot.pack(side = BOTTOM,fill = X)

def aksiyon():
    boy = float(entry1.get())
    kilo = float(entry2.get())
    BMI = kilo / (boy * boy)
    BMI = round(BMI,1)
    messagebox.showinfo("BMI","BMI Değeriniz: {}".format(BMI))
    if 25 <= BMI <= 30:
        messagebox.showinfo("UYARI!","BMI değeriniz 25 ile 30 arasında. Kilolu segmentte yer alıyorsunuz.")
    if 30 < BMI <= 40:
        messagebox.showwarning("UYARI!","BMI değeriniz 30 ile 40 arasında. OBEZ segmentte yer alıyorsunuz.")
    if 40 < BMI:
        messagebox.showerror("UYARI!","BMI değeriniz 40'tan yüksek. MORBİD OBEZ segmentte yer alıyorsunuz.")
        
#boy
yazi1 = Label(root, text="Boyunuzu Girin (metre): ")
yazi1.pack(side = LEFT)
entry1 = Entry(root)
entry1.pack(side = RIGHT)

#kilo
yazi2 = Label(bot, text="Kilonuzu Girin (Kg): ")
yazi2.pack(side = LEFT)
entry2 = Entry(bot)
entry2.pack(side = RIGHT)

#buton
btn = Button(bottom, text="Hesapla", command = aksiyon)
btn.pack()



root.mainloop()
