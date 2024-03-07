import tkinter as tk
from tkinter import messagebox

def email_slicer():
    email = email_entry.get()

    if '@' in email:
        # Split the email address into username and domain
        username, domain = email.split('@')

        # Show the sliced email information in a message box
        messagebox.showinfo("Email Slicer Result", f"Username: {username}\nDomain: {domain}")
    else:
        # Show an error message if the email address is invalid
        messagebox.showerror("Error", "Invalid email address")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Email Slicer")

    # Create and place widgets
    label = tk.Label(root, text="Enter your email address:")
    label.pack(pady=10)

    global email_entry
    email_entry = tk.Entry(root, width=30)
    email_entry.pack(pady=5)

    button = tk.Button(root, text="Slice Email", command=email_slicer)
    button.pack(pady=5)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
