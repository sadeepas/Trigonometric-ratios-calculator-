preview

![image](https://github.com/user-attachments/assets/9daa984c-b708-42e1-895d-0f2cfc122f9c)

# Trigonometric Calculator

A simple, user-friendly Desktop GUI application built with Python and Tkinter. This tool allows users to calculate missing side lengths or angles of a right-angled triangle using standard trigonometric ratios (Sine, Cosine, and Tangent).

## 📋 Features

*   **Two Calculation Modes:**
    *   **Find Side Length:** Calculate a missing side (hypotenuse) given one leg length and an angle.
    *   **Find Angle:** Calculate a missing angle given the lengths of two sides.
*   **Trigonometric Support:** Supports Sine (sin), Cosine (cos), and Tangent (tan) functions.
*   **Error Handling:** Includes alerts for invalid inputs (non-numeric values) or missing selections.
*   **Clean Interface:** Easy-to-use grid layout.

## 🛠️ Requirements

*   Python 3.x
*   Tkinter (Included with most standard Python installations)

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/trig-calculator-gui.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd trig-calculator-gui
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```
    *(Note: Replace `main.py` with whatever you named your python file).*

## 📖 Usage Guide

1.  **Select what you want to find:**
    *   Choose "Other leg length" or "Angle" using the radio buttons at the top.
2.  **Enter Data:**
    *   **If finding a Length:** Enter the known leg length and the angle in degrees.
    *   **If finding an Angle:** Enter the lengths of Leg 1 and Leg 2.
3.  **Select Ratio:**
    *   Choose the appropriate trigonometric ratio (Sin, Cos, or Tan) based on the triangle data you have.
4.  **Calculate:**
    *   Press the **Calculate** button. The result will appear at the bottom of the window in green text.

## 🧮 Math Logic

The calculator uses the standard Python `math` library:
*   **Sin:** `Leg / sin(angle)` or `arcsin(leg1 / leg2)`
*   **Cos:** `Leg / cos(angle)` or `arccos(leg1 / leg2)`
*   **Tan:** `Leg / tan(angle)` or `arctan(leg1 / leg2)`

## 🤝 Contributing

Contributions are welcome! If you have ideas to improve the UI or add more complex math functions (like Law of Sines/Cosines), feel free to fork the repo and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
