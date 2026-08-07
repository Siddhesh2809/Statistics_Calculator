import tkinter as tk
from tkinter import messagebox, ttk

class StatsCalculator:
    """Core mathematical algorithms implemented from scratch."""

    @staticmethod
    def calculate_mean(data):
        if not data:
            return 0
        total = 0
        for num in data:
            total += num
        return total / len(data)

    @staticmethod
    def calculate_median(data):
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

    @staticmethod
    def calculate_mode(data):
        if not data:
            return []
        
        counts = {}
        for num in data:
            counts[num] = counts.get(num, 0) + 1

        max_freq = 0
        for num, freq in counts.items():
            if freq > max_freq:
                max_freq = freq

        # If all numbers appear once, there is no mode
        if max_freq == 1:
            return "No Mode (All values unique)"

        modes = [num for num, freq in counts.items() if freq == max_freq]
        return modes

    @staticmethod
    def calculate_variance(data, is_sample=True):
        if len(data) < 2:
            return 0
        
        mean = StatsCalculator.calculate_mean(data)
        sum_squared_diff = 0
        for x in data:
            diff = x - mean
            sum_squared_diff += diff * diff

        divisor = (len(data) - 1) if is_sample else len(data)
        return sum_squared_diff / divisor

    @staticmethod
    def calculate_std_dev(data, is_sample=True):
        variance = StatsCalculator.calculate_variance(data, is_sample)
        # Power of 0.5 computes square root without math library
        return variance ** 0.5


class GUIApp:
    """Tkinter Graphical User Interface for easy running."""

    def __init__(self, root):
        self.root = root
        self.root.title("Descriptive Statistics Calculator")
        self.root.geometry("520x550")
        self.root.configure(bg="#f4f6f9")

        # Title
        title_label = tk.Label(
            root, 
            text="Descriptive Statistics Calculator", 
            font=("Helvetica", 16, "bold"),
            bg="#f4f6f9", 
            fg="#2c3e50"
        )
        title_label.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f4f6f9")
        input_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(
            input_frame, 
            text="Enter numbers (comma or space separated):", 
            font=("Helvetica", 10, "bold"),
            bg="#f4f6f9"
        ).pack(anchor="w", pady=5)

        self.entry_data = tk.Entry(input_frame, font=("Helvetica", 11), width=45)
        self.entry_data.pack(fill="x", ipady=5)

        # Calculate Button
        btn_calc = tk.Button(
            root, 
            text="Calculate Statistics", 
            font=("Helvetica", 11, "bold"),
            bg="#3498db", 
            fg="white", 
            activebackground="#2980b9",
            activeforeground="white",
            relief="flat",
            command=self.process_data
        )
        btn_calc.pack(pady=15, ipadx=10, ipady=5)

        # Results Frame
        self.result_frame = tk.LabelFrame(
            root, 
            text=" Results ", 
            font=("Helvetica", 11, "bold"),
            bg="#ffffff", 
            padx=15, 
            pady=15
        )
        self.result_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.results_labels = {}
        metrics = [
            ("Count (N)", "count"),
            ("Mean (Average)", "mean"),
            ("Median", "median"),
            ("Mode", "mode"),
            ("Sample Variance", "variance"),
            ("Sample Std Deviation", "std_dev")
        ]

        for idx, (label_text, key) in enumerate(metrics):
            lbl_title = tk.Label(
                self.result_frame, 
                text=f"{label_text}:", 
                font=("Helvetica", 10, "bold"),
                bg="#ffffff", 
                anchor="w"
            )
            lbl_title.grid(row=idx, column=0, sticky="w", pady=6)

            lbl_val = tk.Label(
                self.result_frame, 
                text="-", 
                font=("Helvetica", 10),
                bg="#ffffff", 
                fg="#27ae60",
                anchor="w"
            )
            lbl_val.grid(row=idx, column=1, sticky="w", padx=10, pady=6)
            self.results_labels[key] = lbl_val

    def process_data(self):
        raw_input = self.entry_data.get().strip()
        if not raw_input:
            messagebox.showerror("Error", "Please enter valid numerical data.")
            return

        try:
            # Parse comma or space separated numbers
            cleaned_input = raw_input.replace(",", " ")
            data = [float(x) for x in cleaned_input.split()]
            
            if not data:
                raise ValueError("No valid numbers found.")

            # Calculations
            count = len(data)
            mean = StatsCalculator.calculate_mean(data)
            median = StatsCalculator.calculate_median(data)
            mode = StatsCalculator.calculate_mode(data)
            variance = StatsCalculator.calculate_variance(data, is_sample=True)
            std_dev = StatsCalculator.calculate_std_dev(data, is_sample=True)

            # Update GUI Labels
            self.results_labels["count"].config(text=str(count))
            self.results_labels["mean"].config(text=f"{mean:.4f}")
            self.results_labels["median"].config(text=f"{median:.4f}")
            self.results_labels["mode"].config(text=str(mode))
            self.results_labels["variance"].config(text=f"{variance:.4f}")
            self.results_labels["std_dev"].config(text=f"{std_dev:.4f}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers separated by spaces or commas.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()