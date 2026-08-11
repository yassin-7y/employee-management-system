from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox, ttk

emp_list = []


class Employee(ABC):
    def __init__(self, company, loc_company, base_salary):
        self.company = company
        self.location = loc_company
        self.base_salary = base_salary

    def show_info(self):
        return f"Company: {self.company}\nLocation: {self.location}\nBase Salary: {self.base_salary}"

    @abstractmethod
    def display(self):
        pass


class Engineer(Employee):
    def __init__(self, company, loc_company, base_salary, department, name, id, salary):
        super().__init__(company, loc_company, base_salary)
        self.department = department
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        info = self.show_info()
        return f"{info}\nDepartment: {self.department}\nName: {self.__name}\nID: {self.__id}\nSalary: {self.__salary}"


class ML_engineer(Engineer):
    def __init__(self, company, loc_company, base_salary, department, name, id, salary, programming_language, no_models):
        Engineer.__init__(self, company, loc_company, base_salary, department, name, id, salary)
        self.programming_language = programming_language
        self.no_models = no_models
        self.cloud_platforms = []

    def set_cloud_platforms(self, *args):
        self.cloud_platforms.extend(args)

    def display(self):
        info = Engineer.display(self)
        return f"{info}\nNo. of Models: {self.no_models}\nProg. Language: {self.programming_language}\nCloud Platforms: {', '.join(self.cloud_platforms)}"


class DL(Engineer):
    def __init__(self, company, loc_company, base_salary, department, name, id, salary, gpu_architecture):
        Engineer.__init__(self, company, loc_company, base_salary, department, name, id, salary)
        self.gpu_architecture = gpu_architecture
        self.distributed_training_tools = []
        self.experiment_trackers = []

    def set_distributed_training_tools(self, *args):
        self.distributed_training_tools.extend(args)

    def set_experiment_trackers(self, *args):
        self.experiment_trackers.extend(args)

    def display(self):
        info = Engineer.display(self)
        return f"{info}\nGPU Arch: {self.gpu_architecture}\nDist. Tools: {', '.join(self.distributed_training_tools)}\nTrackers: {', '.join(self.experiment_trackers)}"


class AI_Engineer(ML_engineer, DL):
    def __init__(self, company, loc_company, base_salary, department, name, id, salary, programming_language, no_models, gpu_architecture):
        ML_engineer.__init__(self, company, loc_company, base_salary, department, name, id, salary, programming_language, no_models)
        DL.__init__(self, company, loc_company, base_salary, department, name, id, salary, gpu_architecture)

    def display(self):
        ml_info = ML_engineer.display(self)
        dl_info = f"GPU Arch: {self.gpu_architecture}\nDist. Tools: {', '.join(self.distributed_training_tools)}\nTrackers: {', '.join(self.experiment_trackers)}"
        return f"{ml_info}\n{dl_info}"


def for_gui():
    spec = specialization_combo.get().upper()

    if spec in ["ML ENGINEER", "ML"]:
        ML = ML_engineer(
            company_input.get(), location_input.get(), base_salary_input.get(),
            department_input.get(), name_input.get(), id_input.get(),
            salary_input.get(), programming_language_input.get(), no_models_input.get()
        )
        if cloud_platform_input.get():
            ML.set_cloud_platforms(cloud_platform_input.get())
        emp_list.append(ML)
        messagebox.showinfo("Success", "ML Engineer added successfully!")
        clear_add_inputs()

    elif spec in ["DEEP LEARNING ENGINEER", "DL"]:
        dl_obj = DL(
            company_input.get(), location_input.get(), base_salary_input.get(),
            department_input.get(), name_input.get(), id_input.get(),
            salary_input.get(), gpu_architecture_input.get()
        )
        if distributed_training_tools_input.get():
            dl_obj.set_distributed_training_tools(distributed_training_tools_input.get())
        if experiment_trackers_input.get():
            dl_obj.set_experiment_trackers(experiment_trackers_input.get())
        emp_list.append(dl_obj)
        messagebox.showinfo("Success", "DL Engineer added successfully!")
        clear_add_inputs()

    elif spec in ["AI ENGINEER", "AI"]:
        Ai = AI_Engineer(
            company_input.get(), location_input.get(), base_salary_input.get(),
            department_input.get(), name_input.get(), id_input.get(),
            salary_input.get(), programming_language_input.get(),
            no_models_input.get(), gpu_architecture_input.get()
        )
        if cloud_platform_input.get():
            Ai.set_cloud_platforms(cloud_platform_input.get())
        if distributed_training_tools_input.get():
            Ai.set_distributed_training_tools(distributed_training_tools_input.get())
        if experiment_trackers_input.get():
            Ai.set_experiment_trackers(experiment_trackers_input.get())
        emp_list.append(Ai)
        messagebox.showinfo("Success", "AI Engineer added successfully!")
        clear_add_inputs()
    else:
        messagebox.showwarning("Warning", "Please select a valid specialization!")


def clear_add_inputs():
    for entry in [company_input, location_input, base_salary_input, department_input,
                  name_input, id_input, salary_input, programming_language_input,
                  no_models_input, cloud_platform_input, gpu_architecture_input,
                  distributed_training_tools_input, experiment_trackers_input]:
        entry.delete(0, END)


def show():
    try:
        no = int(employee_no_input.get())
        if 1 <= no <= len(emp_list):
            details = emp_list[no - 1].display()
            display_text.config(state=NORMAL)
            display_text.delete("1.0", END)
            display_text.insert(END, details)
            display_text.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Employee index out of range!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


def update():
    try:
        number = int(emp_no_input.get()) - 1
        variable = emP_var_input.get().strip().lower()
        NewValue = new_value_input.get().strip()

        if 0 <= number < len(emp_list):
            if variable == "name":
                emp_list[number].set_name(NewValue)
                messagebox.showinfo("Success", "Name updated successfully!")
            elif variable == "id":
                emp_list[number].set_id(NewValue)
                messagebox.showinfo("Success", "ID updated successfully!")
            elif variable == "salary":
                emp_list[number].set_salary(NewValue)
                messagebox.showinfo("Success", "Salary updated successfully!")
            elif hasattr(emp_list[number], variable):
                setattr(emp_list[number], variable, NewValue)
                messagebox.showinfo("Success", f"Field '{variable}' updated successfully!")
            else:
                messagebox.showerror("Error", f"Field '{variable}' does not exist on this employee!")
        else:
            messagebox.showerror("Error", "Employee index out of range!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid employee number!")


def delete():
    try:
        number_emp = int(no_emp_del_input.get()) - 1
        if 0 <= number_emp < len(emp_list):
            del emp_list[number_emp]
            messagebox.showinfo("Success", "Employee deleted successfully!")
            no_emp_del_input.delete(0, END)
        else:
            messagebox.showerror("Error", "Employee index out of range!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


root = Tk()
root.title("Employees Management System")
root.geometry("800x780")
root.configure(bg="#f4f4f9")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#f4f4f9")
style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=[12, 8])
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"))


notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both", padx=15, pady=15)


# --------------------------

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Add Employee")

add_center_frame = ttk.Frame(tab1)
add_center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

fields = [
    ("Company Name:", "company_input"),
    ("Location:", "location_input"),
    ("Base Salary:", "base_salary_input"),
    ("Department:", "department_input"),
    ("Name:", "name_input"),
    ("ID:", "id_input"),
    ("Salary:", "salary_input"),
    ("Prog. Language (ML):", "programming_language_input"),
    ("No. of Models (ML):", "no_models_input"),
    ("Cloud Platform (ML):", "cloud_platform_input"),
    ("GPU Architecture (DL):", "gpu_architecture_input"),
    ("Dist. Training Tools (DL):", "distributed_training_tools_input"),
    ("Experiment Trackers (DL):", "experiment_trackers_input"),
]

ttk.Label(add_center_frame, text="Specialization:").grid(row=0, column=0, sticky=W, padx=12, pady=5)
specialization_combo = ttk.Combobox(add_center_frame, values=["ML", "DL", "AI"], state="readonly", width=33, font=("Arial", 11))
specialization_combo.grid(row=0, column=1, padx=12, pady=5)
specialization_combo.current(0)

entries = {}
for idx, (label_text, var_name) in enumerate(fields, start=1):
    ttk.Label(add_center_frame, text=label_text).grid(row=idx, column=0, sticky=W, padx=12, pady=4)
    entry = ttk.Entry(add_center_frame, width=35, font=("Arial", 11))
    entry.grid(row=idx, column=1, padx=12, pady=4)
    entries[var_name] = entry

company_input = entries["company_input"]
location_input = entries["location_input"]
base_salary_input = entries["base_salary_input"]
department_input = entries["department_input"]
name_input = entries["name_input"]
id_input = entries["id_input"]
salary_input = entries["salary_input"]
programming_language_input = entries["programming_language_input"]
no_models_input = entries["no_models_input"]
cloud_platform_input = entries["cloud_platform_input"]
gpu_architecture_input = entries["gpu_architecture_input"]
distributed_training_tools_input = entries["distributed_training_tools_input"]
experiment_trackers_input = entries["experiment_trackers_input"]

btn_add = ttk.Button(add_center_frame, text="Add Employee", command=for_gui)
btn_add.grid(row=14, column=0, columnspan=2, pady=18)


# ---------------------------

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Display Info")

ttk.Label(tab2, text="Enter Employee Index (1, 2, ...):").pack(anchor=W, padx=20, pady=15)
employee_no_input = ttk.Entry(tab2, width=35, font=("Arial", 11))
employee_no_input.pack(anchor=W, padx=20, pady=5)

btn_show = ttk.Button(tab2, text="Show Details", command=show)
btn_show.pack(anchor=W, padx=20, pady=12)

display_text = Text(tab2, width=70, height=20, font=("Consolas", 11), state=DISABLED)
display_text.pack(padx=20, pady=15)


# -------------------------

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Update Employee")

update_center_frame = ttk.Frame(tab3)
update_center_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

ttk.Label(update_center_frame, text="Employee Number:").grid(row=0, column=0, sticky=W, padx=12, pady=12)
emp_no_input = ttk.Entry(update_center_frame, width=35, font=("Arial", 11))
emp_no_input.grid(row=0, column=1, padx=12, pady=12)

ttk.Label(update_center_frame, text="Field Name (e.g. name, salary, gpu_architecture):").grid(row=1, column=0, sticky=W, padx=12, pady=12)
emP_var_input = ttk.Entry(update_center_frame, width=35, font=("Arial", 11))
emP_var_input.grid(row=1, column=1, padx=12, pady=12)

ttk.Label(update_center_frame, text="New Value:").grid(row=2, column=0, sticky=W, padx=12, pady=12)
new_value_input = ttk.Entry(update_center_frame, width=35, font=("Arial", 11))
new_value_input.grid(row=2, column=1, padx=12, pady=12)

btn_update = ttk.Button(update_center_frame, text="Update Data", command=update)
btn_update.grid(row=3, column=0, columnspan=2, pady=22)


# ------------------------

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Delete Employee")

delete_center_frame = ttk.Frame(tab4)
delete_center_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

ttk.Label(delete_center_frame, text="Employee Number to Delete:").pack(padx=20, pady=15)
no_emp_del_input = ttk.Entry(delete_center_frame, width=35, font=("Arial", 11))
no_emp_del_input.pack(padx=20, pady=8)

btn_del = ttk.Button(delete_center_frame, text="Delete Employee", command=delete)
btn_del.pack(padx=20, pady=20)

root.mainloop()
