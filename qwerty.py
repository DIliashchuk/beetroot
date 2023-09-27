import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv


class Developer:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name

    def create_report(self, project_name, time_spent, description, date):
        report = {
            "project_name": project_name,
            "time_spent": time_spent,
            "description": description,
            "date": date
        }

        try:
            with open("report.csv", 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                csv_writer.writerow([self.name, self.second_name, report["project_name"],
                                     report["time_spent"], report["description"], report["date"]])
        except Exception as e:
            print(f"Error creating report: {e}")

    def modify_report(self, project_name, new_project_name, new_time_spent, new_description, new_date):
        try:
            with open("report.csv", 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                convert_report = list(csv_reader)

            flag = False
            for index_csv in convert_report:
                if index_csv[2] == project_name:  # Change index to match the project name column
                    flag = True
                    break

            if not flag:
                print("No ID found.")
                return

            for index_csv in convert_report:
                if index_csv[2] == project_name:
                    index_csv[2] = new_project_name
                    index_csv[3] = str(new_time_spent)  # Ensure time_spent is a string
                    index_csv[4] = new_description
                    index_csv[5] = new_date

            with open("report.csv", 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                for row in convert_report:
                    csv_writer.writerow(row)
        except Exception as e:
            print(f"Error modifying report: {e}")

    def view_project(self):
        try:
            with open("report.csv", 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                for row in csv_reader:
                    print(row)
        except Exception as e:
            print(f"Error viewing project: {e}")



    def view_cost_for_job(self, second_name, project_name):
        time_spent = 0
        project_salary = 0

        # Read data from report.csv to get time spent by the developer
        try:
            with open("report.csv", 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                convert_report = list(csv_reader)

                for mysalary in convert_report:
                    if mysalary[1] == second_name:
                        time_spent = mysalary[4]
                        break
        except Exception as e:
            print(f"Error reading report.csv: {e}")

        # Read data from salary.csv to get the project's salary
        try:
            with open("salary.csv", 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                convert_report = list(csv_reader)

                for mysalary in convert_report:
                    if mysalary[0] == project_name:
                        project_salary = mysalary[2]
                        break
        except Exception as e:
            print(f"Error reading salary.csv: {e}")

        total_cost = int(time_spent) * int(project_salary)

        # Show the cost information in a messagebox
        try:
            messagebox.showinfo("Cost Information", f"The cost of work for {second_name} on project {project_name} is ${total_cost}.")
        except Exception as e:
            print(f"Error displaying messagebox: {e}")

class Manager:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name


    def create_project(self, project_name, description, budget, deadline):
        project = {
            "project_name": project_name,
            "description": description,
            "budget": budget,
            "deadline": deadline,
            "manager_who_created": self.second_name
        }

        try:
            with open("project.csv", 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',')
                csv_writer.writerow(
                    [project["project_name"], project["description"], project["budget"], project["deadline"], self.second_name])
        except Exception as e:
            print(f"Error creating report: {e}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Management System")
        self.root.geometry("800x400")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.role_label = tk.Label(self.frame, text="Choose Your Role:")
        self.role_label.grid(row=0, column=0)

        self.role = tk.StringVar()
        self.role.set("Manager")

        self.role_option_menu = tk.OptionMenu(self.frame, self.role, "Manager", "Developer")
        self.role_option_menu.grid(row=0, column=1, columnspan=2)

        self.name_label = tk.Label(self.frame, text="Employee Name:")
        self.name_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.second_name_label = tk.Label(self.frame, text="Employee Second Name:")
        self.second_name_label.grid(row=2, column=0)

        self.second_name_entry = tk.Entry(self.frame)
        self.second_name_entry.grid(row=2, column=1)

        self.role_button = tk.Button(self.frame, text="Select Role", command=self.select_role)
        self.role_button.grid(row=3, column=0, columnspan=2)

        self.project_name_entry = tk.Entry(self.frame)
        self.description_entry = tk.Entry(self.frame)
        self.budget_entry = tk.Entry(self.frame)
        self.deadline_entry = tk.Entry(self.frame)

    def select_role(self):
        role = self.role.get()
        name = self.name_entry.get()  # Get the employee's name from the entry field
        second_name = self.second_name_entry.get()  # Get the employee's second name from the entry field

        if not name or not second_name:
            messagebox.showerror("Error", "Please enter both name and second name.")
            return

        if role == "Manager":
            # Pass the name and second_name to the Manager constructor
            manager = Manager(name, second_name)
            self.show_manager_options(manager)
        elif role == "Developer":
            # Pass the name and second_name to the Developer constructor
            developer = Developer(name, second_name)
            self.show_developer_options(developer)
        else:
            messagebox.showerror("Error", "Invalid Role Selected")

    def show_manager_options(self, manager):
        for widget in self.frame.winfo_children():
            widget.destroy()

        create_report_button = tk.Button(self.frame, text="Create_new_project", command=self.create_new_project)
        create_report_button.grid(row=0, column=0, padx=10, pady=10)

        return_to_main_button = tk.Button(self.frame, text="Return to Main Menu", command=self.show_main_menu)
        return_to_main_button.grid(row=1, column=0, padx=10, pady=10)


    def show_main_menu(self):
    # Clear existing widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Re-create the role selection and entry fields
        self.role_label = tk.Label(self.frame, text="Choose Your Role:")
        self.role_label.grid(row=0, column=0)

        self.role = tk.StringVar()
        self.role.set("Manager")

        self.role_option_menu = tk.OptionMenu(self.frame, self.role, "Manager", "Developer")
        self.role_option_menu.grid(row=0, column=1, columnspan=2)

        self.name_label = tk.Label(self.frame, text="Employee Name:")
        self.name_label.grid(row=1, column=0)

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.second_name_label = tk.Label(self.frame, text="Employee Second Name:")
        self.second_name_label.grid(row=2, column=0)

        self.second_name_entry = tk.Entry(self.frame)
        self.second_name_entry.grid(row=2, column=1)

        self.role_button = tk.Button(self.frame, text="Select Role", command=self.select_role)
        self.role_button.grid(row=3, column=0, columnspan=2)

    def show_manager_options(self, manager):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create labels and Entry widgets for project details
        project_name_label = tk.Label(self.frame, text="Project Name:")
        project_name_label.grid(row=0, column=0)

        project_name_entry = tk.Entry(self.frame)
        project_name_entry.grid(row=0, column=1)

        description_label = tk.Label(self.frame, text="Description:")
        description_label.grid(row=1, column=0)

        description_entry = tk.Entry(self.frame)
        description_entry.grid(row=1, column=1)

        budget_label = tk.Label(self.frame, text="Budget:")
        budget_label.grid(row=2, column=0)

        budget_entry = tk.Entry(self.frame)
        budget_entry.grid(row=2, column=1)

        deadline_label = tk.Label(self.frame, text="Deadline:")
        deadline_label.grid(row=3, column=0)

        deadline_entry = tk.Entry(self.frame)
        deadline_entry.grid(row=3, column=1)

        # Create a button to create a new project
        create_project_button = tk.Button(self.frame, text="Create Project",
                                          command=lambda: self.create_project(manager, project_name_entry,
                                                                              description_entry,
                                                                              budget_entry,
                                                                              deadline_entry))

        create_project_button.grid(row=4, column=0, columnspan=2)

    def create_project(self, manager, project_name_entry, description_entry, budget_entry, deadline_entry):
        project_name = project_name_entry.get()
        description = description_entry.get()
        budget = budget_entry.get()
        deadline = deadline_entry.get()

        # Check if any of the fields are empty
        if not project_name or not description or not budget or not deadline:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create a report using the Developer instance
        manager.create_project(project_name, description, budget, deadline)

        # Show a success message
        messagebox.showinfo("Report Created", "Report has been created successfully.")

    def show_developer_options(self, developer):
        # Clear any existing widgets on the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create labels and Entry widgets to input report details
        project_name_label = tk.Label(self.frame, text="Project Name:")
        project_name_label.grid(row=0, column=0)

        project_name_entry = tk.Entry(self.frame)
        project_name_entry.grid(row=0, column=1)

        time_spent_label = tk.Label(self.frame, text="Time Spent:")
        time_spent_label.grid(row=1, column=0)

        time_spent_entry = tk.Entry(self.frame)
        time_spent_entry.grid(row=1, column=1)

        description_label = tk.Label(self.frame, text="Description:")
        description_label.grid(row=2, column=0)

        description_entry = tk.Entry(self.frame)
        description_entry.grid(row=2, column=1)

        date_label = tk.Label(self.frame, text="Date:")
        date_label.grid(row=3, column=0)

        date_entry = tk.Entry(self.frame)
        date_entry.grid(row=3, column=1)

        # Create a button to submit the report
        create_report_button = tk.Button(self.frame, text="Create Report",
                                         command=lambda: self.create_report(developer, project_name_entry,
                                                                            time_spent_entry, description_entry,
                                                                            date_entry))
        create_report_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        return_to_main_button = tk.Button(self.frame, text="Return to Main Menu", command=self.show_main_menu)
        return_to_main_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def create_report(self, developer, project_name_entry, time_spent_entry, description_entry, date_entry):
        # Retrieve report details from Entry widgets
        project_name = project_name_entry.get()
        time_spent = time_spent_entry.get()
        description = description_entry.get()
        date = date_entry.get()

        # Check if any of the fields are empty
        if not project_name or not time_spent or not description or not date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create a report using the Developer instance
        developer.create_report(project_name, time_spent, description, date)

        # Show a success message
        messagebox.showinfo("Report Created", "Report has been created successfully.")


    def modify_report(self):
        # Implement modify_report functionality here
        pass

    def view_project(self):
        # Implement view_project functionality here
        pass

    def view_cost_for_job(self):
        # Implement view_cost_for_job functionality here
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()