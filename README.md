# 🧮 Samarpan Calculator

A fully functional calculator application built in Python with both command-line and GUI versions. Perfect for learning Python fundamentals and GUI development with Tkinter.

---

## 📋 Features

### **calculator.py** (Basic Logic Version)
- Core calculator logic with arithmetic operations
- Continuous calculation support
- Error handling for invalid inputs
- Functions for:
  - `number_pressed(num)` - Handle digit input
  - `operation_pressed(op)` - Handle operations (+, -, *, /)
  - `equals_pressed()` - Calculate and display result
  - `clear_pressed()` - Reset calculator
  - `perform_calculation()` - Execute arithmetic operations

### **calculator_gui.py** (GUI Version - Enhanced)
- **Modern Dark Theme** - Professional appearance with cyan accents
- **Intuitive Interface** - Standard smartphone calculator layout
- **All Basic Operations** - Addition, Subtraction, Multiplication, Division
- **Additional Features**:
  - Backspace button (←) - Delete last digit
  - Clear button (C) - Reset all
  - Decimal point support
  - Error handling for division by zero
  - Responsive button design with hover effects
  - Custom fonts and styling

---

## 🛠️ Requirements

```
Python 3.7+
tkinter (built-in with Python)
```

### Install Python
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Mac**: `brew install python3`
- **Linux**: `sudo apt-get install python3`

### Verify Tkinter
```bash
python3 -m tkinter
```
If a small window appears, Tkinter is installed and ready!

---

## 🚀 How to Use

### Running the GUI Calculator (Recommended)

```bash
python3 calculator_gui.py
```

**Features:**
- Click number buttons (0-9)
- Click operation buttons (+, −, ×, ÷)
- Click "=" to calculate
- Click "C" to clear
- Click "←" to delete last digit

### Example Calculations
- `5 + 3 = 8`
- `10 × 4 = 40`
- `15 ÷ 3 = 5`
- `2.5 + 3.5 = 6.0`

---

## 📁 Project Structure

```
calculator/
├── calculator.py           # Core logic (command-line)
├── calculator_gui.py       # Enhanced GUI version
└── README.md              # This file
```

---

## 🎨 GUI Design

The calculator features:

- **Display**: Large cyan text on dark background (#0f0f0f)
- **Number Buttons**: Dark grey (#2d2d2d) with white text
- **Operations**: Orange (#ff6b35) for better visibility
- **Equals**: Bright cyan (#00d4ff) for emphasis
- **Clear**: Red (#d42426) for caution
- **Window Size**: 400x600 pixels (mobile-friendly)

---

## 💻 Code Architecture

### Variables Used
```python
current_result = 0          # Stores last calculation result
pending_operation = None    # Stores current operation
new_number_input = 0        # Current number being typed
```

### Key Functions
- `press(value)` - Add digit to display
- `clear()` - Reset calculator
- `calculate()` - Evaluate expression using `eval()`
- `backspace()` - Remove last digit
- `perform_calculation()` - Execute arithmetic operations

---

## 🐛 Error Handling

The calculator gracefully handles:
- ✅ Division by zero → "Cannot divide by 0"
- ✅ Invalid expressions → "Error"
- ✅ Invalid input types → Automatic conversion

---

## 🎓 Learning Resources

This project teaches:
- Python fundamentals (variables, functions, loops)
- Tkinter GUI programming
- Event handling with callbacks
- String manipulation and data types
- Error handling with try-except blocks
- Grid layout management

---

## 🔮 Future Enhancements

Potential features to add:
- [ ] Scientific calculator (sin, cos, tan, log, sqrt)
- [ ] Calculator history
- [ ] Keyboard input support
- [ ] Custom themes
- [ ] Memory buttons (M+, M-, MR, MC)
- [ ] Parentheses support for complex expressions

---

## 📝 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

**Samarpan**

---

## 📞 Feedback

Found a bug or have suggestions? Feel free to contribute!

---

## 🎯 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

2. **Run the calculator**
   ```bash
   python3 calculator_gui.py
   ```

3. **Start calculating!** 🧮

---

## ⚡ Quick Start

```bash
# Clone repo
git clone <your-repo-url>

# Navigate to folder
cd calculator

# Run GUI version
python3 calculator_gui.py
```

That's it! The calculator is ready to use. ✨

---

**Enjoy your calculator application!** If you found this helpful, please ⭐ star the repository!
