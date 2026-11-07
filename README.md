# GLPI Decryption Tool

## Overview

This small Python script decrypts one Base64-encoded value produced by modern
GLPI installations. It reads the matching GLPI key file and prints the
decrypted value. It was created as a learning tool while working on the
**Management** machine on Hack The Box, and is not a complete GLPI integration.

## Requirements

- Python 3
- Access to the matching GLPI key file at
  `/opt/glpi/config/glpicrypt.key`
- PyNaCl, installed from `requirements.txt`

Create and activate a virtual environment, then install the dependency:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

Pass the encrypted Base64 value as the only argument:

```bash
python3 glpi_decrypt.py 'BASE64_ENCRYPTED_VALUE'
```

The script expects the key file to be readable at
`/opt/glpi/config/glpicrypt.key`. If the key is stored elsewhere, update that
path in `glpi_decrypt.py`. The key must belong to the GLPI instance that
encrypted the value. The script handles the modern Sodium-based format; it does
not handle GLPI's legacy `GLPIKEY` format.

## What Is GLPI?

GLPI (Gestionnaire Libre de Parc Informatique) is an open-source IT asset and
service management application. IT teams use it to keep track of equipment,
software, licenses, contracts, suppliers, and support requests.

## Where Is GLPI Used?

Organizations use GLPI in their IT departments and help desks to manage
technology assets and support workflows. It is a web application, so users
usually access it through a browser. It is commonly installed on a PHP web
server connected to a database such as MySQL or MariaDB.

## How Does GLPI Work?

GLPI stores its inventory, configuration, and service records in a database.
Users and IT staff manage this information through the web interface. Some
sensitive settings are encrypted so GLPI can use them without storing them as
plain text. Modern GLPI installations use an instance-specific key in
`glpicrypt.key` for this encryption.

For the values handled by this tool, the encrypted data is Base64-encoded. The
script decodes it, separates the 24-byte nonce from the encrypted data, and
uses PyNaCl with the matching GLPI key to decrypt it.

Only use this tool with systems and data you are authorized to access. Treat
the key file and decrypted output as sensitive.
