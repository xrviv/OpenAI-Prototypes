import tkinter as tk
import csv, os

def submit():
    grant_date = grant_date_entry.get()
    grantor = grantor_entry.get()
    grantee = grantee_entry.get()
    project_information = project_information_entry.get()
    github_source_code = github_source_code_entry.get()
    contribution = contribution_entry.get()
    amount = amount_entry.get()

    row = [grant_date, grantor, grantee, project_information, github_source_code, contribution, amount]
    with open('grants_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save():
    submit() # call the submit function to write the latest data to the CSV file
    # Save the data to the CSV file
    with open('grants_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

def exit():
    root.destroy()

os.system('clear')
root = tk.Tk()
root.title("Grants Data")
root.config(bg='grey')

grant_date_label = tk.Label(root, text="Grant Date", bg='grey', fg='white')
grant_date_label.grid(row=0, column=0)

grant_date_entry = tk.Entry(root)
grant_date_entry.grid(row=0, column=1)

grantor_label = tk.Label(root, text="Grantor", bg='grey', fg='white')
grantor_label.grid(row=1, column=0)

grantor_entry = tk.Entry(root)
grantor_entry.grid(row=1, column=1)

grantee_label = tk.Label(root, text="Grantee", bg='grey', fg='white')
grantee_label.grid(row=2, column=0)

grantee_entry = tk.Entry(root)
grantee_entry.grid(row=2, column=1)

project_information_label = tk.Label(root, text="Project Information", bg='grey', fg='white')
project_information_label.grid(row=3, column=0)

project_information_entry = tk.Entry(root)
project_information_entry.grid(row=3, column=1)

github_source_code_label = tk.Label(root, text="GitHub/Source Code", bg='grey', fg='white')
github_source_code_label.grid(row=4, column=0)

github_source_code_entry = tk.Entry(root)
github_source_code_entry.grid(row=4, column=1)

contribution_label = tk.Label(root, text="Contribution", bg='grey', fg='white')
contribution_label.grid(row=5, column=0)

contribution_entry = tk.Entry(root)
contribution_entry.grid(row=5, column=1)

amount_label = tk.Label(root, text="Amount", bg='grey', fg='white')
amount_label.grid(row=6, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=6, column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=7, column=0)

save_button = tk.Button(root, text="Save", command=save)
save_button.grid(row=7, column=1)

root.mainloop()
