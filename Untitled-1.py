import tkinter as tk
from tkinter import ttk

class ColorButton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Button Demo")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Create the button
        self.button = tk.Button(
            self.root,
            text="Click Me!",
            font=("Arial", 16),
            width=15,
            height=3,
            bg="lightgray",
            relief="raised",
            bd=3
        )
        
        # Bind events
        self.button.bind("<Button-1>", self.single_click)
        self.button.bind("<Double-Button-1>", self.double_click)
        
        # Pack the button
        self.button.pack(expand=True)
        
        # Add instruction label
        instruction = tk.Label(
            self.root,
            text="Single click = Green\nDouble click = Red",
            font=("Arial", 10),
            fg="gray"
        )
        instruction.pack(pady=10)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def single_click(self, event):
        """Handle single click - turn button green"""
        self.button.config(bg="green", text="Single Click!")
        print("Single click detected - Button turned green")
    
    def double_click(self, event):
        """Handle double click - turn button red"""
        self.button.config(bg="red", text="Double Click!")
        print("Double click detected - Button turned red")
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ColorButton()
    app.run()