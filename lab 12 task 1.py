import tkinter as tk
from tkinter import messagebox

class CGPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA CALCULATOR")

        self.subjects = ["OOP", "OOP Lab", "English", "IST"]
        self.credit_hours = [3, 1, 2, 2]

        self.create_widgets()

    def create_widgets(self):
        self.entries = {}
        for i, subject in enumerate(self.subjects):
            label = tk.Label(self.root, text=f"{subject}")
            label.grid(row=i, column=0, pady=5, padx=5, sticky=tk.W)

            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[subject] = entry

        calculate_button = tk.Button(self.root, text="Calculate CGPA", command=self.calculate_cgpa)
        calculate_button.grid(row=len(self.subjects), column=0, columnspan=2, pady=10)

    def calculate_cgpa(self):
        try:
            marks = [float(self.entries[subject].get()) for subject in self.subjects]
            credit_hours_sum = sum(self.credit_hours)

            weighted_average = sum(marks[i] * self.credit_hours[i] for i in range(len(self.subjects))) / credit_hours_sum

            cgpa = self.convert_to_cgpa(weighted_average)
            messagebox.showinfo("CGPA Result", f"Your CGPA is: {cgpa:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for percentage marks.")

    def convert_to_cgpa(self, percentage):
        if percentage >= 80:
            return 4.0
        elif 65 <= percentage < 80:
            return 3.0
        elif 50 <= percentage < 65:
            return 1.0
        else:
            return 0.0

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculatorApp(root)
    root.mainloop()
