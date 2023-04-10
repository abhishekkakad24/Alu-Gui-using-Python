from tkinter import *
from PIL import ImageTk , Image,ImageDraw,ImageFont
# Create the main window
root = Tk()
root.geometry("900x300")  #define size of GUI window
root.title("ALU by Abhishek Kakad using tkinter ")  # title of GUI
bg = ImageTk.PhotoImage(file='Paste file location of background image')
bg_label = Label(root, image=bg).place(x=360,y=1)

# Create the input/output labels and text boxes
input_label_a = Label(root, text="Enter first number: ",font=('Courier',14,'bold'),pady=10)
input_label_a.grid(row=0, column=0)
input_box_a = Entry(root)
input_box_a.grid(row=0, column=1)
input_box_a.focus()

input_label_b = Label(root, text="Enter second number: ",font=('Courier',14,'bold'),pady=10)
input_label_b.grid(row=1, column=0)
input_box_b = Entry(root)
input_box_b.insert(END,'0')
input_box_b.grid(row=1, column=1)

operation_label = Label(root, text="Operation:",font=('Courier',14,'bold'),pady=10)
operation_label.grid(row=2, column=0)
operation_var = StringVar()
operation_dropdown = OptionMenu(root,operation_var, "Add", "Subtract", "Multiply", "Divide", "Mod", "Remainder", "Power", "AND", "OR", "NAND", "NOR", "XOR", "XNOR", "NOT", "Shift left", "Shift right", "Rotate left", "Rotate right", "Decimal-binary", "Binary-decimal", "Binary-octet", "Binary-hexadecimal", "Hex-binary", "Octet-binary", "Decimal-Hex", "Decimal-octet", "Octet-decimal", "Hex-decimal", "Oct-hex", "1's complement", "2's complement", "GCD", "LCM")

operation_dropdown.grid(row=2, column=1)

result_label = Label(root, text="Result:",font=('Courier',14,'bold'),pady=10)
result_label.grid(row=4, column=0)
result_box = Label(root, text="")
result_box.grid(row=4, column=1)

# Define a function to perform the selected operation and update the result label
def perform_operation():
        a = input_box_a.get()
        b = input_box_b.get()
        operation = operation_var.get()

        if operation == "Add":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a + b
        elif operation == "Subtract":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a - b
        elif operation == "Multiply":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a * b
        elif operation == "Divide":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a / b
        elif operation == "Mod":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a % b
        elif operation == "Remainder":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a//b
        elif operation == "Power":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = pow(a, b)
        elif operation == "AND":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a & b
        elif operation == "OR":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a | b
        elif operation == "NAND":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = ~(a & b) 
        elif operation == "NOR":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = ~(a | b) 
        elif operation == "XOR":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a ^ b
        elif operation == "XNOR":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = ~(a ^ b) 
        elif operation == "NOT":
            a = int(input_box_a.get())
            result = ~a 
        elif operation == "Shift left":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a << b
        elif operation == "Shift right":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = a >> b
        elif operation == "Rotate left":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = (a << b) | (a >> (32 - b))
        elif operation == "Rotate right":
            a = int(input_box_a.get())
            b = int(input_box_b.get())
            result = (a >> b) | (a << (32 - b))
        elif operation == "Decimal-binary":
            a = input_box_a.get()
            b = input_box_b.get()
            result = bin(a)[2:]
        elif operation == "Binary-decimal":
            a = input_box_a.get()
            b = input_box_b.get()
            result = int(a, 2)
        elif operation == "Binary-octet":
            a = input_box_a.get()
            b = input_box_b.get()
            result = oct(int(a, 2))[2:]
        elif operation == "Binary-hexadecimal":
            a = input_box_a.get()
            b = input_box_b.get()
            result = hex(int(a, 2))[2:].upper()
        elif operation == "Hex-binary":
            a = input_box_a.get()
            b = input_box_b.get()
            result = bin(int(a, 16))[2:]
        elif operation == "Octet-binary":
            a = input_box_a.get()
            b = input_box_b.get()
            result = bin(int(a, 8))[2:]
        elif operation == "Decimal-Hex":
            a = input_box_a.get()
            b = input_box_b.get()
            result = hex(a)[2:].upper()
        elif operation == "Decimal-octet":
            a = input_box_a.get()
            b = input_box_b.get()
            result = oct(a)[2:]
        elif operation == "Octet-decimal":
            a = input_box_a.get()
            b = input_box_b.get()
            result = int(a, 8)
        elif operation == "Hex-decimal":
            a = input_box_a.get()
            b = input_box_b.get()
            result = int(a, 16)
        elif operation == "Oct-hex":
            a = input_box_a.get()
            b = input_box_b.get()
            result = hex(int(a, 8))[2:].upper()
        elif operation == "1's complement":
            a = input_box_a.get()
            result = ~a 
        elif operation == "2's complement":
            a = input_box_a.get()
            result = (~a + 1) 
        elif operation == "GCD":
            a = input_box_a.get()
            b = input_box_b.get()
            def gcd(self, a, b):
                if a == 0:
                    return b
                return self.gcd(b % a, a)
        elif operation == "LCM":
            a = input_box_a.get()
            b = input_box_b.get()
            def lcm(x, y):
                return (a * b) // gcd(a, b)
        else:
            result_box.config(text="Invalid input")
                
        result_box.config(text=str(result))

calculate_button = Button(root, text="Calculate", command=perform_operation,font=('Courier',14,'bold'),pady=10)
calculate_button.grid(row=3, column=0, columnspan=2)
root.mainloop()