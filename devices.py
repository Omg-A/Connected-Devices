from tkinter import *
import subprocess, json

root = Tk()
root.title("Conected Devices")
root.geometry("500x500")
root.configure(background="gold")

out = subprocess.getoutput("powershell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName| ConvertTo-Json}\"")

e1 = Label(root, text="Status:", font=("Helvaticka", 10, "bold"), bg="gold")
e1.grid(row=0, column=0, padx=10, pady=10)

e1 = Label(root, text="Class:", font=("Helvaticka", 10, "bold"), bg="gold")
e1.grid(row=0, column=1, padx=10, pady=10)

e1 = Label(root, text="Friendly Name:", font=("Helvaticka", 10, "bold"), bg="gold")
e1.grid(row=0, column=2, padx=10, pady=10)

count = 1
json_data = json.loads(out)

for dev in json_data:
    if count <= 13:
        lst = [dev["Status"], dev["Class"], dev["FriendlyName"]]
        print(lst)
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(root, width=35, fg="blue", font=("Arial", 10, "bold"))
                e.grid(row=count, column=j, ipadx=10, ipady=10, columnspan=2)
                e.insert(END, lst[i][i])
        count = count + 1

root.mainloop()