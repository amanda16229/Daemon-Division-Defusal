This is a final project for Systems Programming.
It is a simulated, terminal-based, bomb diffusal.

The whole thing is us using an image scanner to extract the password from an example briefing and diffusing the simulated bomb. 
(when the bomb is active, we'll see the timer and the light will be red, when it's diffused, it'll be green and the timer will stop! it'll also output: "DISARM SUCCESSFUL")

Dependencies:
- Pillow (image processing):
    python3 -m pip install --upgrade pip
    python3 -m pip install pillow pytesseract
- Tesseract OCR Engine:
    https://github.com/UB-Mannheim/tesseract/wiki (for Windows installation)
    "brew install tesseract" (for MAC installation)
    pytesseract.pytesseract.tesseract_cmd = "/path/to/tesseract"

To Run:
1. git clone https://github.com/amanda16229/Daemon-Division-Defusal.git
2. cd Daemon-Division-Defusal
3. python3 main.py

To Find the Correct Password:
Use "bomb defusal pass.png"! (You'll need to download it first!)
