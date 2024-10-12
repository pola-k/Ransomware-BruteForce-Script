# Bruteforce Password Recovery for ZIP Files

## Overview
This project is a simple brute force password recovery script designed to extract files from a password-protected ZIP archive using a wordlist. The script utilizes the `zipfile` module in Python to attempt to extract files using passwords from a specified text file, such as the popular `rockyou.txt` list. This project is part of the **AIG Cybersecurity Program** offered by **Forage**.

## Features
- **Brute Force Extraction**: Attempts to extract files from a ZIP archive using passwords from a specified wordlist.
- **Feedback**: Provides real-time feedback on the password attempts and indicates if the correct password is found.
- **Easy to Use**: Simple command-line interface requiring minimal setup.

## Technologies Used
- Python 3.x
- `zipfile` module (included in Python standard library)

## Getting Started

### Prerequisites
- **Python 3.x**: Ensure you have Python installed on your machine.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/pola-k/Ransomware-BruteForce-Script.git
   ```

2. **Change into the project directory**:
   ```bash
   cd Ransomware-BruteForce-Script
   ```

3. **Download the `rockyou.txt` wordlist**:
   - You can download the `rockyou.txt` file from various sources online. Ensure that the file is placed in the same directory as your script.

### Usage
1. **Place the target ZIP file** (`enc.zip`) in the project directory.

2. **Run the script**:
   ```bash
   python brute_force.py
   ```

3. The script will begin to attempt extracting the ZIP file using each password from the `rockyou.txt` wordlist. 

### Example Output
```bash
[+] Beginning bruteforce 
[+] Password Found
[+] Decrypting Files
[+] Password: yourpassword123
```

### Important Notes
- Ensure that the ZIP file and `rockyou.txt` are in the same directory as the script.
- The script may take some time to run, depending on the length of the password list and the complexity of the password.

## Limitations
- **Efficiency**: The brute force method can be time-consuming, especially with long or complex passwords.
- **Wordlist Dependency**: The success of the script depends on the quality and comprehensiveness of the wordlist used.

## Disclaimer
**Use this tool responsibly and only on files you have permission to access. Unauthorized access to computer systems is illegal and unethical.**
