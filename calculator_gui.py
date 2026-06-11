import tkinter as tk
from tkinter import font

# ============== WINDOW ==============

root = tk.Tk()
root.title("Samarpan Calculator")
root.geometry("400x600")
root.configure(bg="#1a1a1a")
root.resizable(False, False)

# Define custom fonts
display_font = font.Font(family="Segoe UI", size=32, weight="bold")
button_font = font.Font(family="Segoe UI", size=18, weight="bold")

# ============== DISPLAY ==============

display = tk.Entry(
    root,
    font=display_font,
    justify="right",
    fg="#ff9900",
    bg="#000000",
    border=0,
    insertbackground="#2b00ff"
)

display.pack(fill="x", padx=20, pady=30)

# ============== FUNCTIONS ==============

def press(value):
    display.insert(tk.END, str(value))


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        
        display.delete(0, tk.END)
        display.insert(0, str(result))
    
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by 0")
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


# ============== BUTTON FRAME ==============

frame = tk.Frame(root, bg="#1a1a1a")
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Button Styles
number_button = {
    "width": 8,
    "height": 3,
    "font": button_font,
    "bg": "#2d2d2d",
    "fg": "#ffffff",
    "border": 0,
    "activebackground": "#404040",
    "activeforeground": "#00d4ff",
    "relief": "flat",
    "cursor": "hand2"
}

operation_button = {
    "width": 8,
    "height": 3,
    "font": button_font,
    "bg": "#ff6b35",
    "fg": "#ffffff",
    "border": 0,
    "activebackground": "#ff8555",
    "activeforeground": "#ffffff",
    "relief": "flat",
    "cursor": "hand2"
}

equals_button = {
    "width": 8,
    "height": 3,
    "font": button_font,
    "bg": "#00d4ff",
    "fg": "#1a1a1a",
    "border": 0,
    "activebackground": "#00e6ff",
    "activeforeground": "#1a1a1a",
    "relief": "flat",
    "cursor": "hand2"
}

clear_button = {
    "width": 8,
    "height": 3,
    "font": button_font,
    "bg": "#d42426",
    "fg": "#ffffff",
    "border": 0,
    "activebackground": "#e54449",
    "activeforeground": "#ffffff",
    "relief": "flat",
    "cursor": "hand2"
}

# ============== ROW 1 ==============

tk.Button(frame, text="7", command=lambda: press(7), **number_button).grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="8", command=lambda: press(8), **number_button).grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="9", command=lambda: press(9), **number_button).grid(row=0, column=2, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="÷", command=lambda: press("/"), **operation_button).grid(row=0, column=3, padx=8, pady=8, sticky="nsew")

# ============== ROW 2 ==============

tk.Button(frame, text="4", command=lambda: press(4), **number_button).grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="5", command=lambda: press(5), **number_button).grid(row=1, column=1, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="6", command=lambda: press(6), **number_button).grid(row=1, column=2, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="×", command=lambda: press("*"), **operation_button).grid(row=1, column=3, padx=8, pady=8, sticky="nsew")

# ============== ROW 3 ==============

tk.Button(frame, text="1", command=lambda: press(1), **number_button).grid(row=2, column=0, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="2", command=lambda: press(2), **number_button).grid(row=2, column=1, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="3", command=lambda: press(3), **number_button).grid(row=2, column=2, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="−", command=lambda: press("-"), **operation_button).grid(row=2, column=3, padx=8, pady=8, sticky="nsew")

# ============== ROW 4 ==============

tk.Button(frame, text="0", command=lambda: press(0), **number_button).grid(row=3, column=0, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text=".", command=lambda: press("."), **number_button).grid(row=3, column=1, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="←", command=backspace, **number_button).grid(row=3, column=2, padx=8, pady=8, sticky="nsew")
tk.Button(frame, text="+", command=lambda: press("+"), **operation_button).grid(row=3, column=3, padx=8, pady=8, sticky="nsew")

# ============== ROW 5 ==============

tk.Button(frame, text="C", command=clear, width=8, height=3, font=button_font, bg="#d42426", fg="#ffffff", border=0, activebackground="#e54449", activeforeground="#ffffff", relief="flat", cursor="hand2").grid(row=4, column=0, columnspan=2, padx=8, pady=8, sticky="nsew")

tk.Button(frame, text="=", command=calculate, width=8, height=3, font=button_font, bg="#00d4ff", fg="#1a1a1a", border=0, activebackground="#00e6ff", activeforeground="#1a1a1a", relief="flat", cursor="hand2").grid(row=4, column=2, columnspan=2, padx=8, pady=8, sticky="nsew")

# Configure grid weights for responsive sizing
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i if i < 4 else 3, weight=1)

# ============== MAIN LOOP ==============

root.mainloop()