# Python script to demonstrate MySQL database CRUD operations on teh GUI
# NB: Ensure you've installed the mysql python connector => pip install mysql-connector-python

# Import the required modules
import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from tkcalendar import DateEntry # For date picker

from db_conn import db_config
from student import Student

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("980x640")
        self.root.title("Student Management System")
        self.root.resizable(False, False)
        self.root.minsize(980, 640)
        #self.root.maxsize(800, 600)

        # Database connection
        self.conn = None
        self.cursor = None
        self.connect_to_db()

        # ------------------------ Form Frame -----------------------------------------------
        form_frame = tk.LabelFrame(self.root, text="Student Data",padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        # Student Number
        tk.Label(form_frame, text="Student No *").grid(row=0, sticky="e",column=0, padx=8, pady=5)
        self.entries = {}
        self.entries["student_no"] = tk.Entry(form_frame, width=32)
        self.entries["student_no"].grid(row=0, column=1, sticky="w")

        # Student Name
        tk.Label(form_frame, text='Student Name').grid(row=1,column=0,sticky="e", padx=8, pady=5)
        self.entries["name"] = tk.Entry(form_frame, width=32)
        self.entries["name"].grid(row=1, column=1, sticky="w")

        # Student Birthdate (Date Picker)
        tk.Label(form_frame, text="Birth Date *").grid(row=2,column=0,sticky="e", padx=8, pady=5)
        self.entries["birthdate"] = DateEntry(
            form_frame,
            width=28,
            date_pattern="yyyy-mm-dd",
            background="darkblue",
            foreground="white",
            borderwidth=2,
        )
        self.entries["birthdate"].grid(row=2, column=1, sticky="w")

        # Student Gender Dropdown
        tk.Label(form_frame, text="Gender *").grid(row=3,column=0,sticky="e", padx=8, pady=5)
        self.entries["gender"] = ttk.Combobox(
            form_frame,
            values=["M","F"],
            state="readonly",
            width=30,
        )
        self.entries["gender"].grid(row=3, column=1, sticky="w")
        self.entries["gender"].set("M") # Set the default gender

        # Student City
        tk.Label(form_frame,text="City *").grid(row=4,column=0,sticky="e", padx=8, pady=5)
        self.entries["city"] = tk.Entry(form_frame, width=32)
        self.entries["city"].grid(row=4, column=1, sticky="w")

        # Buttons
        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=5, column=0, columnspan=3, pady=12)

        tk.Button(btn_frame, text="Add/Update", width=14,command=self.create_or_update).pack(side="left",padx=5)
        tk.Button(btn_frame, text="Delete", width=14,command=self.delete_record).pack(side="left",padx=5)
        tk.Button(btn_frame, text="Clear", width=14,command=self.clear_form).pack(side="left",padx=5)

        # ------------------------ Search Frame -----------------------------------------------
        search_frame = tk.LabelFrame(root, text="Search/Filter",padx=10, pady=7)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame,text="Search By").pack(side="left",pady=5)

        self.search_field = ttk.Combobox(
            search_frame,
            values=["StudentNO","Name","City"],
            state="readonly",
            width=15,
        )
        self.search_field.set("Name")
        self.search_field.pack(side="left",padx=5)

        self.search_value = tk.Entry(search_frame, width=30)
        self.search_value.pack(side="left",padx=5)
        self.search_value.bind("<Return>", lambda e: self.search_record())

        tk.Button(search_frame,text="Search",width=12,command=self.search_record).pack(side="left",padx=5)
        tk.Button(search_frame, text="Show All",width=12,command=self.load_all_records).pack(side="left",padx=5)

        # ------------------------ Tree View -----------------------------------------------
        tree_frame = tk.Frame(root)
        tree_frame.pack(fill="both",expand=True, padx=10, pady=5)

        columns = ("Student Number","Student Name","Birth Date","Gender","City")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings",height=15)

        for col, width in zip(columns,(110,220,100,80,160)):
            self.tree.heading(col, text=col.replace("_"," "))
            self.tree.column(col, width=width, anchor="center" if col != "Name" else "w")

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>",self.on_row_select)

        # Initial load
        self.load_all_records

        # Database connection
    def connect_to_db(self):
        if self.conn and self.conn.is_connected():
            return
        try:
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Could not connect to database: \n{err}")
            self.conn = None
            self.cursor = None

    # ---------------------------------------------------------
    def ensure_connection(self):
        if self.conn and not self.conn.is_connected():
            self.connect_to_db()
        return self.conn is not None and self.conn.is_connected()

    # ---------------------------------------------------------
    def load_all_records(self):
        if not self.ensure_connection():
            return
        try:
            self.cursor.execute("SELECT * FROM student") # execute("SELECT StudentNo, Name, Birthdate,Gender,City FROM Student")
            rows = self.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Unable to load records: \n{err}")

    # ----------------------------------------------------------
    def get_form_data(self):
        data = {
            "student_no": self.entries["student_no"].get().strip(),
            "name": self.entries["name"].get().strip(),
            "birthdate": self.entries["birthdate"].get_date().strftime("%m-%d-%Y"),
            "gender": self.entries["gender"].get(),
            "city": self.entries["city"].get(),
        }
        missing = [k for k, v in data.items() if not v]
        if missing:
            messagebox.showerror("Missing Data",f"Please fill in all the student fields with values")
            return None
        try:
            Student(**data) # reuse validation
        except mysql.connector.Error as err:
            messagebox.showerror("Invalid Data", f"\n{err}")
            return None
        return data

    # ---------------------------------------------------------------------------------
    def create_or_update(self):
        data = self.get_form_data()
        if not data or not self.ensure_connection():
            return
        try:
            self.cursor.execute("SELECT count(*) FROM student WHERE StudentNO=%s", (data["student_no"],))
            exists = self.cursor.fetchone()[0]>0
            if exists:
                query = """
                UPDATE student 
                SET Name=%s, BirthDate=%s, Gender=%s,City=%s
                 WHERE StudentNO=%s\
                """
                params = (data["name"], data["birth_date"], data["gender"], data["city"], data["student_no"])
            else:
                query = """
                INSERT INTO student (StudentNO, Name, BirthDate, Gender, City)
                VALUES (%s, %s, %s, %s, %s)
                """
                params = (data["student_no"], data["name"], data["birth_date"], data["gender"], data["city"])

            self.cursor.execute(query, params)
            self.conn.commit()
            action = "updated" if exists else "created"
            messagebox.showinfo("Success", f"Student record {action} successfully!")
            self.load_all_records()
            self.clear_form()
        except mysql.connector.Error as err:
            messagebox.showerror("Data Error", f"Unable to save record. \n{err}")

    # ------------------------------------------------------------------------------
    def delete_record(self):
        student_no = self.entries["student_no"].get().strip()
        if not student_no:
            messagebox.showerror("Missing Data", "Please enter or select a student number to delete.")
            return
        if not self.ensure_connection():
            return

        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {student_no}?"):
            return

        try:
            self.cursor.execute("DELETE FROM student WHERE StudentNO=%s", (student_no,))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Student record {student_no} successfully deleted.")
                self.load_all_records()
                self.clear_form()
            else:
                messagebox.showwarning("Record Not Found", f"No record with {student_no} found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Unable to delete record.\n{err}")

    # -------------------------------------------------------------------------------
    def search_record(self):
        if not self.ensure_connection():
            return

        field = self.search_field.get()
        value = self.search_value.get().strip()

        if not value:
            self.load_all_records()
            return

        try:
            query = f"SELECT StudentNO, Name, Birthdate, Gender, City FROM student WHERE {field} LIKE %s"
            self.cursor.execute(query, (f"%{value}%",))
            rows = self.cursor.fetchall()

            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Unable to search record.\n{err}")

    # ----------------------------------------------------------------------------
    def on_row_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0])["values"]
        self.clear_form()

        keys = ["student_no", "name", "birthdate", "gender", "city"]
        for key, value in zip(keys, values):
            if key == "birthdate":
                self.entries[key].set_date(value)
            elif key == "gender":
                self.entries[key].set(value)
            else:
                self.entries[key].insert(0,value)

    # -----------------------------------------------------------------------------
    def clear_form(self):
        for key, widget in self.entries.items():
            if isinstance(widget, ttk.Combobox):
                widget.set("M")
            elif isinstance(widget, DateEntry):
                widget.set_date(datetime.today())
            else:
                widget.delete(0, tk.END)

    # ------------------------------------------------------------------------------
    def __del__(self):
        if self.conn and self.conn.is_connected():
            if self.cursor and self.cursor.is_connected():
                self.cursor.close()
            self.conn.close()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()