#!/usr/bin/env python3
# File: glpi_decrypt_commented.py
# Author: 0xKaiser (GitHub: erikgavs)
# Purpose: Decrypt a value from GLPI.
# Usage: python3 glpi_decrypt.py '<base64-value>'
# Check the key file path in the script before running it.
# Needs: PyNaCl

import base64  # Convert the input from Base64.
import sys  # Read the value given in the terminal.
from pathlib import Path  # Open the key file.
from nacl.bindings import crypto_aead_xchacha20poly1305_ietf_decrypt  # Decrypt the value.

# Make sure one encrypted value was provided.
if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 glpi_decrypt.py '<base64-value>'")

# Save the encrypted value from the command line.
value = sys.argv[1]

# Read the GLPI key file as bytes.
key = Path("/opt/glpi/config/glpicrypt.key").read_bytes()

# Convert the Base64 value into bytes.
data = base64.b64decode(value, validate=True)

# The first 24 bytes are a random value needed for decryption.
nonce = data[:24]

# The remaining bytes contain the encrypted data.
cipher = data[24:]

# Decrypt the value. GLPI passes the 24-byte value twice.
text = crypto_aead_xchacha20poly1305_ietf_decrypt(
    cipher,  # The encrypted data.
    nonce,  # A value GLPI also uses to check the data.
    nonce,  # The 24-byte value needed for decryption.
    key,  # The GLPI key.
)

# Show the decrypted bytes as text.
print(text.decode("utf-8"))
