import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(0, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("VIRUS Calculator")

screen = tk.Entry(root, font="lucida 20 bold", borderwidth=8, relief="sunken")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="lucida 15 bold", padx=20, pady=10)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
