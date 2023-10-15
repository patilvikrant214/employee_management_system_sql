import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        self.employee_list = []
        self.selected_employee_index = None

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.pack()

        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Employee", command=self.update_employee)
        self.update_button.pack()

        self.view_button = tk.Button(root, text="View Employees", command=self.view_employees)
        self.view_button.pack()

    def add_employee(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        if name and age:
            employee = Employee(name, age)
            self.employee_list.append(employee)
            self.clear_entries()
            messagebox.showinfo("Success", "Employee added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_employee(self):
        if self.selected_employee_index is not None:
            name = self.name_entry.get()
            age = self.age_entry.get()

            if name and age:
                employee = self.employee_list[self.selected_employee_index]
                employee.name = name
                employee.age = age
                self.clear_entries()
                self.selected_employee_index = None
                messagebox.showinfo("Success", "Employee updated successfully!")
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

    def view_employees(self):
        if self.employee_list:
            view_window = tk.Toplevel(self.root)
            view_window.title("Employee List")

            for i, employee in enumerate(self.employee_list):
                employee_frame = tk.Frame(view_window)
                employee_label = tk.Label(employee_frame, text=f"Name: {employee.name}, Age: {employee.age}")
                edit_button = tk.Button(employee_frame, text="Edit", command=lambda i=i: self.edit_employee(i))
                employee_label.pack(side=tk.LEFT)
                edit_button.pack(side=tk.LEFT)
                employee_frame.pack()

        else:
            messagebox.showinfo("Info", "No employees to display.")

    def edit_employee(self, index):
        self.selected_employee_index = index
        employee = self.employee_list[index]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, employee.name)
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, employee.age)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
