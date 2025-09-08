import tkinter as tk
from tkinter import ttk

class ColorButton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Button")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        # Configure the main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create the button
        self.button = tk.Button(
            main_frame,
            text="Click Me!",
            width=15,
            height=3,
            font=("Arial", 14, "bold"),
            bg="lightgray",
            relief="raised",
            borderwidth=3
        )
        self.button.grid(row=0, column=0, padx=20, pady=20)
        
        # Bind events
        self.button.bind("<Button-1>", self.on_single_click)
        self.button.bind("<Double-Button-1>", self.on_double_click)
        
        # Add instructions
        instructions = tk.Label(
            main_frame,
            text="Single click = Green\nDouble click = Red",
            font=("Arial", 10),
            justify=tk.CENTER
        )
        instructions.grid(row=1, column=0, pady=10)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
    
    def on_single_click(self, event):
        """Handle single click - change button to green"""
        self.button.config(bg="green", activebackground="darkgreen")
        self.button.config(text="Green!")
    
    def on_double_click(self, event):
        """Handle double click - change button to red"""
        self.button.config(bg="red", activebackground="darkred")
        self.button.config(text="Red!")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ColorButton()
    app.run()