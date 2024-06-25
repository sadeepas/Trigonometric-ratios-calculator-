import tkinter as tk
from tkinter import messagebox
import math

# Function to calculate trigonometric ratios
def calculate_trig():
    try:
        if var_choice.get() == 1:  # If finding other leg length
            leg = float(entry_leg.get())
            angle = math.radians(float(entry_angle.get()))
            if var_ratio.get() == 1:  # Sin ratio
                result = leg / math.sin(angle)
            elif var_ratio.get() == 2:  # Cos ratio
                result = leg / math.cos(angle)
            elif var_ratio.get() == 3:  # Tan ratio
                result = leg / math.tan(angle)
            else:
                messagebox.showerror("Error", "Please select a valid ratio.")
                return
            lbl_result.config(text=f"Result: {result:.2f}")

        elif var_choice.get() == 2:  # If finding angle
            leg1 = float(entry_leg1.get())
            leg2 = float(entry_leg2.get())
            if var_ratio.get() == 1:  # Sin ratio
                result = math.degrees(math.asin(leg1 / leg2))
            elif var_ratio.get() == 2:  # Cos ratio
                result = math.degrees(math.acos(leg1 / leg2))
            elif var_ratio.get() == 3:  # Tan ratio
                result = math.degrees(math.atan(leg1 / leg2))
            else:
                messagebox.showerror("Error", "Please select a valid ratio.")
                return
            lbl_result.config(text=f"Result: {result:.2f} degrees")

        else:
            messagebox.showerror("Error", "Please select what you want to find.")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Trigonometric Calculator")

# Create variables to store user choices
var_choice = tk.IntVar()
var_ratio = tk.IntVar()

# Create GUI components
lbl_title = tk.Label(root, text="Trigonometric Calculator", font=("Arial", 16))
lbl_title.grid(row=0, column=0, columnspan=3, pady=10)

lbl_choice = tk.Label(root, text="What do you want to find?")
lbl_choice.grid(row=1, column=0, padx=10, pady=5, sticky="w")

rb_leg = tk.Radiobutton(root, text="Other leg length", variable=var_choice, value=1)
rb_leg.grid(row=1, column=1, padx=10, pady=5, sticky="w")

rb_angle = tk.Radiobutton(root, text="Angle", variable=var_choice, value=2)
rb_angle.grid(row=1, column=2, padx=10, pady=5, sticky="w")

lbl_leg = tk.Label(root, text="Leg length:")
lbl_leg.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_leg = tk.Entry(root)
entry_leg.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="we")

lbl_angle = tk.Label(root, text="Angle (degrees):")
lbl_angle.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_angle = tk.Entry(root)
entry_angle.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="we")

lbl_leg1 = tk.Label(root, text="Leg 1 length:")
lbl_leg1.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_leg1 = tk.Entry(root)
entry_leg1.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="we")

lbl_leg2 = tk.Label(root, text="Leg 2 length:")
lbl_leg2.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_leg2 = tk.Entry(root)
entry_leg2.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="we")

lbl_ratio = tk.Label(root, text="Trigonometric Ratio:")
lbl_ratio.grid(row=6, column=0, padx=10, pady=5, sticky="w")

rb_sin = tk.Radiobutton(root, text="Sin", variable=var_ratio, value=1)
rb_sin.grid(row=6, column=1, padx=10, pady=5, sticky="w")

rb_cos = tk.Radiobutton(root, text="Cos", variable=var_ratio, value=2)
rb_cos.grid(row=6, column=2, padx=10, pady=5, sticky="w")

rb_tan = tk.Radiobutton(root, text="Tan", variable=var_ratio, value=3)
rb_tan.grid(row=7, column=1, columnspan=2, padx=10, pady=5, sticky="w")

btn_calculate = tk.Button(root, text="Calculate", command=calculate_trig, bg="blue", fg="white")
btn_calculate.grid(row=8, column=0, columnspan=3, pady=10)

lbl_result = tk.Label(root, text="Result will appear here", fg="green")
lbl_result.grid(row=9, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()
