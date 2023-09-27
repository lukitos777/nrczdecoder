import tkinter as tk


# _|¯|____|¯|__|¯¯¯
def function() -> str:
	nrcz = input_text.get()
	label.config(text=nrcz.replace("|¯", "1").replace("|_", "1").replace("_", "0").replace("¯", "0"))


# main widget
root = tk.Tk()
root.title("NRCZ decoder")
root.iconbitmap(default="favicon.ico")
root.geometry("150x100") 

# Create a label with no initial text
label = tk.Label(root, text="")
label.pack()

# Create an entry widget for text input
input_text = tk.Entry(root)
input_text.pack()

# Create a "Run" button
run_button = tk.Button(root, text="Run", command=function)
run_button.pack()

root.mainloop()