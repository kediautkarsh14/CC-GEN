# AYTRO GEN

**AYTRO GEN** is a Python-based terminal application for generating synthetic test data through a simple, menu-driven interface.

> ⚠️ **For testing and development only.**  
> Do not use synthetic data or this software for unauthorized transactions, fraud, payment-system abuse, identity theft, or any other illegal activity.

---

## ✨ Features

- Clean and simple terminal interface
- AYTRO GEN branded launcher
- Multiple generation options
- Separate generator scripts
- Automatic output organization
- Easy Python-based setup
- Dedicated `output` directory
- Supports multiple generation sizes

---

## 📋 Requirements

Before starting AYTRO GEN, make sure you have:

- Windows
- Python installed
- `pip` available from the terminal
- The complete AYTRO GEN project folder

You can check Python with:

```bash
py --version
```

You can check pip with:

```bash
pip --version
```

---

## 🚀 Installation

### Step 1 — Open the Project Folder

Open Command Prompt or PowerShell and navigate to the AYTRO GEN directory.

For example:

```bash
cd C:\Users\YourName\Downloads\AYTRO-GEN
```

Make sure `main.py` and `requirements.txt` are present in the directory.

---

### Step 2 — Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs the Python packages required by the project.

If the installation completes successfully, you can proceed to the next step.

---

### Step 3 — Start AYTRO GEN

Run:

```bash
py main.py
```

The AYTRO GEN interface will appear in your terminal.

---

## 🎮 Main Menu

The launcher provides generation options similar to:

```text
───────────────────────────────────────────────────────
                    AYTRO GEN
───────────────────────────────────────────────────────

[1] Generate 10
[2] Generate 20
[3] Generate 50
[4] Generate 100

[0] Exit

AYTRO GEN >
```

### Generate 10

Select:

```text
1
```

This launches the 10-item generator.

### Generate 20

Select:

```text
2
```

This launches the 20-item generator.

### Generate 50

Select:

```text
3
```

This launches the 50-item generator.

### Generate 100

Select:

```text
4
```

This launches the 100-item generator.

### Exit

Select:

```text
0
```

to close AYTRO GEN.

---

## 📁 Project Structure

The recommended structure is:

```text
AYTRO-GEN/
│
├── main.py
├── requirements.txt
│
├── gens/
│   ├── generator10.py
│   ├── generator20.py
│   ├── generator50.py
│   └── generator100.py
│
└── output/
    ├── gen10.txt
    ├── gen20.txt
    ├── gen50.txt
    └── gen100.txt
```

### `main.py`

The main launcher for AYTRO GEN.

It displays the menu and starts the selected generator.

### `requirements.txt`

Contains the Python dependencies required by the project.

Install them with:

```bash
pip install -r requirements.txt
```

### `gens/`

Contains the individual generator scripts.

Each script is responsible for a different generation size.

### `output/`

Contains the generated **synthetic test data**.

The directory can be created automatically by the application if it does not already exist.

---

## 📂 Output Files

Depending on the selected option, the application can organize output as:

```text
output/
├── gen10.txt
├── gen20.txt
├── gen50.txt
└── gen100.txt
```

This keeps generated files separate from the application source code.

---

## 🔧 Troubleshooting

### `pip` is not recognized

Try:

```bash
py -m pip install -r requirements.txt
```

### `py` is not recognized

Python may not be installed or may not have been added to your PATH.

Check:

```bash
python --version
```

If that works, start the application with:

```bash
python main.py
```

### `ModuleNotFoundError`

Run:

```bash
pip install -r requirements.txt
```

Then try:

```bash
py main.py
```

### Generator file not found

Make sure the `gens` folder is located beside `main.py`:

```text
AYTRO-GEN/
├── main.py
└── gens/
    ├── generator10.py
    ├── generator20.py
    ├── generator50.py
    └── generator100.py
```

---

## ⚡ Quick Start

For users who already have Python installed:

```bash
pip install -r requirements.txt
py main.py
```

That's it.

---

## 🛡️ Responsible Use

AYTRO GEN should only be used with synthetic data and in authorized testing or development environments.

Do not use the software to:

- Perform unauthorized transactions
- Test payment systems without permission
- Commit fraud
- Bypass payment verification
- Obtain another person's financial information
- Circumvent security controls

Use appropriate sandbox/test environments when developing payment-related software.

---

## 📜 License

AYTRO GEN is provided for development, testing, and educational purposes.

The author is not responsible for misuse of the software.

---

## 💙 AYTRO GEN

**Simple. Fast. Automated.**

```text
pip install -r requirements.txt
py main.py
```