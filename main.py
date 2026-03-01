import tkinter as tk
from controllereng import OSINTController
from frontend import OSINTUI

def main():
    # Dependency Injection: Controller gets the Engine logic
    controller = OSINTController()
    
    # UI gets the Controller
    root = tk.Tk()
    app = OSINTUI(root, controller)
    
    root.mainloop()

if __name__ == "__main__":
    main()