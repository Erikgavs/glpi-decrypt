import base64
import sys
from pathlib import Path
from nacl.bindings import crypto_aead_xchacha20poly1305_ietf_decrypt

if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 glpi_decrypt.py '<base64-value>'")

value = sys.argv[1]
key = Path("/opt/glpi/config/glpicrypt.key").read_bytes()
data = base64.b64decode(value, validate=True)
nonce = data[:24]
cipher = data[24:]

text = crypto_aead_xchacha20poly1305_ietf_decrypt(
    cipher, nonce, nonce, key
)

print(text.decode("utf-8"))
