from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os
from tkinter import *
from tkinter import filedialog, messagebox

# Function to generate keys
def generate_keys():
    try:
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        with open("private_key.pem", "wb") as priv_file:
            priv_file.write(private_key)
        with open("public_key.pem", "wb") as pub_file:
            pub_file.write(public_key)
        messagebox.showinfo("Success", "Keys generated and saved as private_key.pem and public_key.pem.")
    except Exception as e:
        messagebox.showerror("Error", f"Key generation failed: {str(e)}")

# Function to sign a file
import time
import json
def sign_file():
    try:
        file_path = filedialog.askopenfilename(title="Select a file to sign")
        if not file_path:
            return
        with open(file_path, "rb") as file:
            data = file.read()
        with open("private_key.pem", "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())
        
        # Create hash of the file
        h = SHA256.new(data)
        
        # Sign the hash
        signature = pkcs1_15.new(private_key).sign(h)
        
        # Create metadata with timestamp
        timestamp = int(time.time())  # Current time as Unix timestamp
        metadata = {
            "filename": os.path.basename(file_path),
            "timestamp": timestamp,
            "human_time": time.ctime(timestamp)
        }
        
        # Save both signature and metadata
        with open("signature.bin", "wb") as sig_file:
            sig_file.write(signature)
        
        with open("signature_metadata.json", "w") as meta_file:
            json.dump(metadata, meta_file, indent=4)
            
        messagebox.showinfo("Success", f"Signature saved as signature.bin\nTimestamp: {time.ctime(timestamp)}")
    except Exception as e:
        messagebox.showerror("Error", f"Signing failed: {str(e)}")

# Function to verify a signature
def verify_signature():
    try:
        file_path = filedialog.askopenfilename(title="Select a file to verify")
        if not file_path:
            return
        # Load timestamp metadata if it exists
        try:
            with open("signature_metadata.json", "r") as meta_file:
                metadata = json.load(meta_file)
                timestamp = metadata.get("timestamp", 0)
                
                # Check if signature has expired (5 minutes)
                expiration_period = 1 * 60  # 5 minutes in seconds
                current_time = int(time.time())
                
                if current_time - timestamp > expiration_period:
                    messagebox.showwarning("Warning", 
                        f"This signature has expired!\nCreated: {metadata['human_time']}\nExpired: {time.ctime(timestamp + expiration_period)}")
                    return
        except FileNotFoundError:
            # If no metadata found, just proceed with verification
            pass
        
        with open(file_path, "rb") as file:
            data = file.read()
        with open("public_key.pem", "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())
        with open("signature.bin", "rb") as sig_file:
            signature = sig_file.read()
            
        # Verify the signature
        h = SHA256.new(data)
        pkcs1_15.new(public_key).verify(h, signature)
        messagebox.showinfo("Success", "The signature is valid.")
    except (ValueError, TypeError):
        messagebox.showerror("Error", "The signature is invalid.")
    except Exception as e:
        messagebox.showerror("Error", f"Verification failed: {str(e)}")

# Create the main window
root = Tk()
root.title("Digital Signature Scheme")
root.geometry("400x200")

# Add buttons
generate_keys_btn = Button(root, text="Generate Keys", command=generate_keys, width=20, height=2)
generate_keys_btn.pack(pady=10)

sign_file_btn = Button(root, text="Sign a File", command=sign_file, width=20, height=2)
sign_file_btn.pack(pady=10)

verify_signature_btn = Button(root, text="Verify a Signature", command=verify_signature, width=20, height=2)
verify_signature_btn.pack(pady=10)

# Run the GUI
root.mainloop()