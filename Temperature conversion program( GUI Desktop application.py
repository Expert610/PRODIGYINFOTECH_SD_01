import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

def convert_temperature():
    try:
        input_temp = float(entry_temp.get())
        input_scale = scale_var.get()

        if input_scale == "Celsius":
            fahrenheit = (input_temp * 9/5) + 32
            kelvin = input_temp + 273.15
            output1.set(f"Fahrenheit: {fahrenheit:.2f} °F")
            output2.set(f"Kelvin: {kelvin:.2f} K")
        elif input_scale == "Fahrenheit":
            celsius = (input_temp - 32) * 5/9
            kelvin = celsius + 273.15
            output1.set(f"Celsius: {celsius:.2f} °C")
            output2.set(f"Kelvin: {kelvin:.2f} K")
        elif input_scale == "Kelvin":
            celsius = input_temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            output1.set(f"Celsius: {celsius:.2f} °C")
            output2.set(f"Fahrenheit: {fahrenheit:.2f} °F")
        else:
            output1.set("Invalid scale")
            output2.set("")
    except ValueError:
        output1.set("Enter a valid number!")
        output2.set("")

app = ttk.Window(themename="yeti")
app.title("Temperature Converter")
app.geometry("500x450")
app.resizable(False, False)
app.iconbitmap(r"D:\Prodigy InfoTech\Task 1\thermostat.ico")


ttk.Label(app, text="Select Scale:", font=("Arial", 12)).pack(pady=(10, 5))
scale_var = StringVar(value="Celsius")
scale_menu = ttk.Combobox(app, textvariable=scale_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
scale_menu.pack(pady=5)


ttk.Label(app, text="Enter Temperature:", font=("Arial", 12)).pack(pady=(10, 5))
entry_temp = ttk.Entry(app)
entry_temp.pack(pady=5)


ttk.Button(app, text="Convert", command=convert_temperature, bootstyle=PRIMARY).pack(pady=10)


output1 = StringVar()
output2 = StringVar()
ttk.Label(app, textvariable=output1, font=("Arial", 12)).pack()
ttk.Label(app, textvariable=output2, font=("Arial", 12)).pack()
ttk.Label(app,text="Developed By Muhammad Yasir With 💖").pack(side="bottom",padx=10,pady=15)


app.mainloop()
