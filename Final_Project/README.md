## Steganography in Linux — Final Project  

<img width="1918" height="1032" alt="Screenshot 2025-12-03 at 21 47 40" src="https://github.com/user-attachments/assets/39591b52-06a5-4709-9315-e55c80354944" />

Course: Information Security, Fall 2025  
Author: Asiyat Rakhmatova

This project demonstrates practical image steganography using the Linux tool `steghide`.  
It includes a web interface, Bash scripts, example files, and a clear workflow for hiding and extracting secret messages.

The main goal is to provide a reproducible and easy-to-understand demonstration of steganography with real Linux utilities.

---

## Project Overview

Steganography is the process of hiding information within ordinary media files.

In this project:

- A secret text file is embedded inside an image using `steghide`.
- The hidden message can be extracted later with the correct password.
- A Flask-based web interface allows users to upload files and perform the operations visually.
- Bash scripts automate the embedding and extraction commands.
- Example files are provided for immediate testing.

---

## Project Structure

```
Final_Project/
├── app.py                     # Flask web interface
├── requirements.txt           # Python dependencies
│
├── examples/
│   ├── cover.jpg              # carrier image
│   ├── secret.txt             # secret message
│   └── stego.jpg              # example output
│
├── scripts/
│   ├── embed.sh               # hide data using steghide
│   ├── extract.sh             # extract hidden message
│   └── verify.sh              # optional image comparison
│
├── templates/
│   └── index.html             # web interface template
│
└── static/
    └── style.css              # visual styling
```

---

## Tools Used

### steghide (Linux)
Main tool used for embedding and extracting hidden data.

Example commands used within the scripts:

```bash
steghide embed -cf cover.jpg -ef secret.txt -sf stego.jpg -p password
steghide extract -sf stego.jpg -xf extracted.txt -p password
```

### Flask Web Application
`app.py` provides a simple graphical interface where the user can:

- Upload a carrier image  
- Upload a secret text file  
- Enter a password  
- Generate a stego-image  
- Extract hidden data  

This helps demonstrate the process visually.

---

## Installation

### Installing steghide

#### Linux (Ubuntu / Debian)
```
sudo apt update
sudo apt install steghide
```

#### macOS (Homebrew)
```
brew update
brew install git pkg-config automake autoconf libtool gettext libjpeg zlib mhash

git clone https://github.com/607011/steghide.git
cd steghide

export LDFLAGS="-L/opt/homebrew/opt/gettext/lib"
export CPPFLAGS="-I/opt/homebrew/opt/gettext/include"

./configure
make
sudo make install
```

Verify installation:
```
steghide --version
```

#### Windows (WSL recommended)
Install Ubuntu under WSL and run:
```
sudo apt update
sudo apt install steghide
```

---

### Clone this project

```
git clone https://github.com/tayyisa/infosec.git
cd infosec/Final_Project
```

### (Optional but recommended) Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

If you prefer, you can skip the virtual environment and install the dependencies globally.

### Install Python dependencies

```
pip install -r requirements.txt
```

---

## Running the Project

### Run the web application

```
python app.py
```

Then open in your browser:

```
http://127.0.0.1:5000/
```

The interface allows hiding and extracting messages through the browser.

---

## Using the Bash Scripts

### Hide a secret message
```
./scripts/embed.sh examples/cover.jpg examples/secret.txt password
```

### Extract the hidden message
```
./scripts/extract.sh examples/stego.jpg password
```

### Optional verification
```
./scripts/verify.sh examples/cover.jpg examples/stego.jpg
```

---

## Included Examples

The project contains ready-to-use example files:

- `cover.jpg` — carrier image  
- `secret.txt` — message to hide  
- `stego.jpg` — example output  

These allow immediate testing without preparing additional files.

---

## Requirements

To run this project, the following are required:

- `steghide` installed on the system  
- Python 3.10 or higher  
- pip  

To check if `steghide` is installed:

```
steghide --version
```

---

## Summary

This project provides:

- A functioning steganography tool using Linux utilities  
- A clear and simple web interface for demonstration  
- Bash scripts for command-line use  
- Example files for immediate testing  
- A reproducible workflow suitable for evaluation  

The structure, clarity, and organization are intended to match academic project standards.

---

## Video Demonstration

Link to video: https://drive.google.com/file/d/1ATPsCnYLnHbtiReku6HB5xTQ1cwCd-Wd/view?usp=sharing

The video demonstration shows:

1. Running the web interface (`app.py`)  
2. Uploading the carrier image and secret message  
3. Entering a password and generating a stego-image  
4. Using the extraction script to recover the message  
5. A short explanation of how `steghide` works  

---
