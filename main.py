# main.py

import simulated_bomb, image_scanner, timer_ascii_art
import tkinter as tk
import tkinter.messagebox as msgbox

class BombDefusalGUI:
    def __init__(self, root, bomb_timer, correct_code=None):
        self.root = root
        self.bomb = bomb_timer
        self.correct_code = "lowkeytiredfr"
        
        self.root.title("Operation Defusal")
        self.root.geometry("600x500")
        self.root.config(bg="#1a1a1a")
        
        self.create_widgets()
        
        # Start bomb countdown
        self.bomb.start_countdown(callback=self.handle_bomb_event)
    
    def create_widgets(self):
        mainframe = tk.Frame(self.root, bg="#1a1a1a", padx=20, pady=20)
        mainframe.pack(expand=True, fill="both")
        
        tk.Label(mainframe, text="⚠️ BOMB DEFUSAL ⚠️", font=("Courier", 20, "bold"),
                 bg="#1a1a1a", fg="#ff0000").pack(pady=10)
        
        self.timer_label = tk.Label(mainframe, text="TIME: 5 min", font=("Courier", 48, "bold"),
                                    bg="black", fg="#ffffff", padx=20, pady=20)
        self.timer_label.pack(pady=20)
        
        self.status_label = tk.Label(mainframe, text="BOMB ACTIVE", font=("Arial", 14),
                                     bg="#1a1a1a", fg="#ffff00")
        self.status_label.pack(pady=10)
        
        input_frame = tk.Frame(mainframe, bg="#1a1a1a")
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Defusal Code:", font=("Arial", 12),
                 bg="#1a1a1a", fg="white").pack(side="left", padx=5)
        
        self.code_entry = tk.Entry(input_frame, font=("Courier", 14), width=15, show="*")
        self.code_entry.pack(side="left", padx=5)
        self.code_entry.bind('<Return>', lambda e: self.check_code())
        self.code_entry.focus()
        
        self.submit_btn = tk.Button(mainframe, text="SUBMIT CODE", command=self.check_code,
                                    font=("Arial", 12, "bold"), bg="#00aa00", fg="white",
                                    width=20, height=2)
        self.submit_btn.pack(pady=10)
        
        self.result_label = tk.Label(mainframe, text="", font=("Arial", 12, "bold"),
                                     bg="#1a1a1a")
        self.result_label.pack(pady=10)

        self.scan_btn = tk.Button(mainframe, text="SCAN IMAGE", command=self.run_scanner,
                                  font=("Arial", 12, "bold"), bg="#0066cc", fg="white",
                                  width=20, height=2)
        self.scan_btn.pack(pady=10)
    
    def run_scanner(self):
        result = image_scanner.scan_for_password()
        if result:
            encoded, decrypted = result
            answer = msgbox.askyesno("Decrypt?", f"Encoded password found: {encoded}\nDecrypt it?")
            if answer:
                msgbox.showinfo("Decrypted Password", f"Decrypted password: {decrypted}")
                self.correct_code = decrypted
            else:
                msgbox.showinfo("Scanner Output", "Encrypted password found. Copy manually if needed.")
    
    def check_code(self):
        entered_code = self.code_entry.get()
        
        if self.bomb.status == "detonated":
            self.result_label.config(text="Too late! Bomb already detonated!", fg="#ff0000")
            return
        
        if self.bomb.status == "defused":
            self.result_label.config(text="Bomb already defused!", fg="#00ff00")
            return
        
        if entered_code == self.correct_code:
            self.bomb.defuse()
            self.result_label.config(text="✓ CORRECT CODE!", fg="#00ff00")
            self.code_entry.config(state="disabled", bg="#ccffcc")
            self.submit_btn.config(state="disabled", bg="#00ff00")
            self.timer_label.config(fg="#00ff00")
            self.status_label.config(text="BOMB DEFUSED!", fg="#00ff00")
            self.root.config(bg="#004400")
            print("\n✓ Bomb defused successfully in GUI!")
        else:
            self.result_label.config(text="✗ INCORRECT CODE!", fg="#ff0000")
            self.code_entry.delete(0, tk.END)
            self.code_entry.config(bg="#ffcccc")
            self.root.after(500, lambda: self.code_entry.config(bg="white"))
            print("✗ Incorrect defusal code entered.")
    
    def handle_bomb_event(self, event, *args):
        if event == "timer_update":
            time_left = args[0]
            self.root.after(0, lambda: self.timer_label.config(text=f"TIME: {time_left}s"))
            
            if time_left <= 60:
                self.root.after(0, lambda: self.timer_label.config(fg="#ff0000"))
            elif time_left <= 120:
                self.root.after(0, lambda: self.timer_label.config(fg="#ffb300"))
            elif time_left <= 180:
                self.root.after(0, lambda: self.timer_label.config(fg="#f2ff00"))
            elif time_left <= 240:
                self.root.after(0, lambda: self.timer_label.config(fg="#b3ff00"))
            elif time_left <= 300:
                self.root.after(0, lambda: self.timer_label.config(fg="#80ff00"))
        
        elif event == "detonated":
            self.root.after(0, lambda: self.timer_label.config(text="BOOM!", fg="#ff0000"))
            self.root.after(0, lambda: self.status_label.config(text="DETONATED!", fg="#ff0000"))
            self.root.after(0, lambda: self.code_entry.config(state="disabled", bg="#ffcccc"))
            self.root.after(0, lambda: self.submit_btn.config(state="disabled", bg="#ff0000"))
            self.root.after(0, lambda: self.root.config(bg="#440000"))
            self.root.after(0, lambda: self.result_label.config(text="GAME OVER!", fg="#ff0000"))

def run_gui():
    bomb = simulated_bomb.BombTimer()
    root = tk.Tk()
    app = BombDefusalGUI(root, bomb)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
    input("\nPress Enter to exit...")
