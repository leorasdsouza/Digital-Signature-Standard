# Digital-Signature-Standard
A secure Python GUI tool to **digitally sign and verify files** using RSA and SHA-256, with built-in **timestamp validation** to detect expired signatures.

This program implements a **secure digital signature standard** using:
- **RSA-2048** for asymmetric cryptography
- **SHA-256** for file hashing
- **Timestamp validation** for signature expiration

---
## Features
- **Digital Signatures**: Uses **RSA-2048 & SHA-256** for secure file signing  
- **Signature Expiry**: Detects expired signatures to prevent replay attacks  
- **File Integrity Check**: Verifies files haven't been modified  
- **Public-Key Cryptography**: Uses a **public/private key** system  
- **Simple GUI**: User-friendly Tkinter interface
- **Metadata Tracking** - JSON logs of signature creation times

---
## Demo Video

Watch the demo here  [Click to view demo](https://drive.google.com/drive/folders/1OTPrFFCeNv3OJxfHFUsz-NUxHEpufBRW)
---

## How It Works

### 1. Key Generation
- The program **generates a new key pair** (`private_key.pem` and `public_key.pem`) **every time you click "Generate Keys"**  
```python
key = RSA.generate(2048)  # 2048-bit keys
private_key.export_key()  # PEM format
key.publickey().export_key()
```

### 2. Signing a File
1. The file is hashed using **SHA-256**  
2. It **signs the hash** with the private key  
3. The generated **signature** (`signature.bin`) and **timestamp metadata** (`signature_metadata.json`) are saved
```python
signature = pkcs1_15.new(private_key).sign(SHA256.new(data))
```

### 3. Verifying a Signature
1. The script **recomputes the file hash**  
2. It verifies the signature using the **public key**  
3. It also checks whether the signature has **expired** (default: **1-minute expiration**)  
```python
if current_time - timestamp > 60:  # 1-minute expiry
    return "Signature expired!"
pkcs1_15.new(public_key).verify(h, signature)
```
---

## How to Run the Program

### Step 1: Set Up Virtual Environment
Create a virtual environment in your project folder:
```bash
python -m venv myenv
```
Activate the environment:
Windows:

```bash
myenv\Scripts\activate
```
macOS/Linux:

```bash
source myenv/bin/activate
```
### Step 2: Install Dependencies
Install required packages using:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Program
Once everything is set up, launch the GUI:

```bash
python digital_signature.py
```

## Project Structure
```bash
. ├── digital_signature.py # Main Python GUI app
  ├── requirements.txt # List of dependencies
  └── README.md # Project documentation (this file)
```

## Auto-Generated Files

These files are created automatically when you run the program:

- `private_key.pem` — Private key (don't share or commit)
- `public_key.pem` — Public key (safe to share if needed)
- `signature.bin` — Signature of the signed file
- `signature_metadata.json` — Timestamp info in JSON format

>  These files are not included in the GitHub repo for security and clarity.

## Customization

To change the signature expiration period (default is 1 minute), edit this line in `digital_signature.py`:

```python
expiration_period = 1 * 60  # '1' is the number of minutes
```


---

#### Sample Demo Workflow
1. Click **"Generate Keys"**
2. Click **"Sign a File"** and select your `.txt` file
3. Click **"Verify a Signature"** to check:
   -  Valid signature (within 1 minute)
   -  Expired signature (after 1 minute)
   -  Invalid signature (if file is modified)

### License
This project is for educational purposes only.
Not intended for production use without further enhancements.
