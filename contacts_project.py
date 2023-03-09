import tkinter as tk
import psycopg2

class ContactBook:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",database="project",user="postgres",password="shanli2002"
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, number TEXT PRIMARY KEY, email TEXT)")

        self.window = tk.Tk()
        self.window.title("Contact Book")

        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        self.number_label = tk.Label(self.window, text="number:")

        self.number_label.grid(row=1, column=0)

        self.number_entry = tk.Entry(self.window)
        self.number_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.grid(row=2, column=0)

        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0)

        self.view_button = tk.Button(self.window, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=3, column=1)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
        self.cur.execute("INSERT INTO contacts (name,number, email) VALUES (%s ,%s, %s)",(name,number, email))
        self.conn.commit()
        # self.name_entry.delete(0, tk.END)
        # self.number_entry.delete(0,tk.END)
        # self.email_entry.delete(0, tk.END)

    def view_contacts(self):
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()

        top = tk.Toplevel(self.window)
        top.title("Contacts")

        for i, row in enumerate(rows):
            name_label = tk.Label(top, text=row[0])
            name_label.grid(row=i, column=0)

            number_label = tk.Label(top, text=row[1])
            number_label.grid(row=i, column=1)

            email_label = tk.Label(top, text=row[2])
            email_label.grid(row=i, column=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ContactBook()
    app.run()
