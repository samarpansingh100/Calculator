import tkinter as tk
import math
from tkinter import font

# ============== WINDOW ==============

root = tk.Tk()
root.title("Calculator")
root.geometry("450x600")
root.configure(bg="#ffffff")
root.resizable(True, True)
root.minsize(400, 550)

# Define custom fonts
display_font = font.Font(family="Segoe UI", size=40, weight="normal")
button_font = font.Font(family="Segoe UI", size=16, weight="normal")
small_button_font = font.Font(family="Segoe UI", size=10, weight="normal")

# ============== DISPLAY ==============

display_frame = tk.Frame(root, bg="#ffffff")
display_frame.pack(fill="x", padx=20, pady=(20, 10))

display = tk.Entry(
    display_frame,
    font=display_font,
    justify="right",
    fg="#000000",
    bg="#ffffff",
    border=0,
    insertbackground="#000000"
)

display.pack(fill="x")

# ============== FUNCTIONS ==============

def press(value):
    display.insert(tk.END, str(value))

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate():
    try:
        expression = display.get()
        result = eval(
            expression,
            {"__builtins__": None},
            {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log10,
                "ln": math.log,
                "factorial": math.factorial,
                "pi": math.pi,
                "e": math.e,
                "pow": pow,
                "abs": abs
            }
        )
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error")
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# ============== BUTTON STYLES ==============

number_button = {
    "font": button_font,
    "bg": "#f5f5f5",
    "fg": "#000000",
    "border": 0,
    "activebackground": "#e8e8e8",
    "activeforeground": "#000000",
    "relief": "flat",
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 4,
    "height": 2
}

operation_button = {
    "font": button_font,
    "bg": "#ffffff",
    "fg": "#ff9500",
    "border": 0,
    "activebackground": "#f5f5f5",
    "activeforeground": "#ff9500",
    "relief": "flat",
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 4,
    "height": 2
}

scientific_button = {
    "font": small_button_font,
    "bg": "#ffffff",
    "fg": "#999999",
    "border": 0,
    "activebackground": "#f5f5f5",
    "activeforeground": "#666666",
    "relief": "flat",
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 4,
    "height": 1
}

equals_button = {
    "font": button_font,
    "bg": "#ff9500",
    "fg": "#ffffff",
    "border": 0,
    "activebackground": "#e68a00",
    "activeforeground": "#ffffff",
    "relief": "flat",
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 4,
    "height": 4
}

clear_button = {
    "font": button_font,
    "bg": "#ffffff",
    "fg": "#ff3b30",
    "border": 0,
    "activebackground": "#f5f5f5",
    "activeforeground": "#ff3b30",
    "relief": "flat",
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 4,
    "height": 2
}

# ============== MAIN GRID FRAME ==============

main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(padx=15, pady=10, fill="both", expand=True)

# ============== SCIENTIFIC FUNCTIONS ==============

sci_frame = tk.Frame(main_frame, bg="#ffffff")
sci_frame.grid(row=0, column=0, columnspan=5, sticky="ew", pady=(0, 10))

tk.Button(sci_frame, text="sin", command=lambda: press("sin("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="cos", command=lambda: press("cos("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="tan", command=lambda: press("tan("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="√", command=lambda: press("sqrt("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="log", command=lambda: press("log("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="ln", command=lambda: press("ln("), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="π", command=lambda: press("pi"), **scientific_button).pack(side="left", padx=3)
tk.Button(sci_frame, text="x²", command=lambda: press("**2"), **scientific_button).pack(side="left", padx=3)

# ============== CALCULATOR BUTTONS ==============

# Row 1: C  ←  (  )
tk.Button(main_frame, text="C", command=clear, **clear_button).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="←", command=backspace, **operation_button).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="(", command=lambda: press("("), **operation_button).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text=")", command=lambda: press(")"), **operation_button).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

# Row 2: 7  8  9  ÷
tk.Button(main_frame, text="7", command=lambda: press(7), **number_button).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="8", command=lambda: press(8), **number_button).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="9", command=lambda: press(9), **number_button).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="÷", command=lambda: press("/"), **operation_button).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

# Row 3: 4  5  6  ×
tk.Button(main_frame, text="4", command=lambda: press(4), **number_button).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="5", command=lambda: press(5), **number_button).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="6", command=lambda: press(6), **number_button).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="×", command=lambda: press("*"), **operation_button).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

# Row 4: 1  2  3  −
tk.Button(main_frame, text="1", command=lambda: press(1), **number_button).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="2", command=lambda: press(2), **number_button).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="3", command=lambda: press(3), **number_button).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="−", command=lambda: press("-"), **operation_button).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Row 5: 0  .  xʸ  +
tk.Button(main_frame, text="0", command=lambda: press(0), **number_button).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text=".", command=lambda: press("."), **number_button).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="xʸ", command=lambda: press("**"), **operation_button).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
tk.Button(main_frame, text="+", command=lambda: press("+"), **operation_button).grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

# ============== EQUALS BUTTON (RIGHT SIDE) ==============

tk.Button(main_frame, text="=", command=calculate, **equals_button).grid(row=1, column=4, rowspan=5, padx=5, pady=5, sticky="nsew")

# ============== CONFIGURE GRID ==============

for i in range(6):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(5):
    main_frame.grid_columnconfigure(i, weight=1)

# ============== MAIN LOOP ==============

root.mainloop()
