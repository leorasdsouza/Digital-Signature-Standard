# Digital-Signature-Standard
This Python program provides **file integrity verification** using **RSA digital signatures**. It ensures that files remain **untampered** and supports **automatic signature expiration**.
This program implements a **secure digital signature scheme** using:
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

---

## How It Works

### 1. Key Generation
- The program **generates a new key pair** (`private_key.pem` and `public_key.pem`) **every time you click "Generate Keys"**  
```bash
key = RSA.generate(2048)  # 2048-bit keys
private_key.export_key()  # PEM format
key.publickey().export_key()
```

### 2. Signing a File
1. The script hashes the file using **SHA-256**  
2. It **signs the hash** with the private key  
3. The generated **signature** (`signature.bin`) and **timestamp metadata** (`signature_metadata.json`) are saved
```bash
signature = pkcs1_15.new(private_key).sign(SHA256.new(data))
```

### 3. Verifying a Signature
1. The script **recomputes the file hash**  
2. It verifies the signature using the **public key**  
3. It also checks whether the signature has **expired** (default: **1-minute expiration**)  
```bash
if current_time - timestamp > 60:  # 1-minute expiry
    return "Signature expired!"
pkcs1_15.new(public_key).verify(h, signature)
```
---

