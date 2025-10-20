Python Command-Line Calculator

A simple Command-Line Interface (CLI) calculator built using Python. It supports addition, subtraction, multiplication, and division, and runs continuously until the user decides to exit.

📋 Features

➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division (with division-by-zero handling)

🔁 Continuous operation until “Exit” is chosen

✅ Input validation for both menu choices and numeric inputs

🧰 Tools & Technologies

Language: Python

Editor: VS Code / Any Text Editor

Execution: Terminal / Command Prompt

🧾 How to Run

Clone or Download this repository:

git clone https://github.com//calculator-cli-app.git cd calculator-cli-app

Run the script in your terminal:

python calculator.py

Follow on-screen instructions to perform calculations.

🖥️ Example Output Welcome to python's Command-Line-Calculator Please select the correct operation from below 1-Addition(+) 2-Subtraction(-) 3-Multiplication(*) 4-Division(/) 5-End Enter the correct choice: 1 Enter the first value: 10 Enter the second value: 5 Result: 15.0

⚙️ Code Highlights

Uses functions (add, subtract, multiplication, division) for clarity.

Uses loops to handle continuous operations.

Includes error handling (try/except) for invalid numeric inputs.

Uses a custom validation function (correctvalue()) to ensure correct menu input (1–5).

🚀 Future Improvements

Add more operations (e.g., modulus, power, square root).

Implement input validation for non-numeric entries before calculation.

Add colorized CLI output using libraries like colorama.

🧑‍💻 Author Aditya Reddy Computer Science Engineering Student | Aspiring Software Developer GitHub: @adityareddysheri
