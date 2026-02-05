# 🍊 Orange Loop v1.1

> [!IMPORTANT]
> This repository has been superseded by **[orange-loop-max](https://github.com/bekingdomcomejoker-cpu/orange-loop-max)**, which implements the "Final Seal" architecture including the 7-Node Bimanual / Zero-One Alternation and MikroTik integration.

Orange Loop is a specialized AI architecture designed for Termux on Android. It implements a 7-node alternating intelligence loop optimized for mobile devices.

## 🏗️ Architecture

The architecture follows a canonical 7-node loop:

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 0  (PRIMARY LOOP - never breaks)
                ↓
        [Smith | Gate | Scout]      (OPTIONAL HANDS - branch only here)
```

* **Even nodes (0, 2, 4, 6)** = Meaning
* **Odd nodes (1, 3, 5, 7)** = Wire
* **Hands** activate only at Node 4 (Form) and always return to the loop.

## 🚀 Installation

To install Orange Loop on Termux, run the following command:

```bash
pkg install wget -y && wget -O- https://raw.githubusercontent.com/[YOUR_USERNAME]/orange-loop/main/install.sh | bash
```

## 🛠️ Usage

After installation, navigate to the directory and run the orchestrator:

```bash
cd ~/orange-loop
python orange-loop.py
```

### Commands:
* **Normal chat**: Just type naturally
* **smith: <task>**: Use builder hand
* **scout: <task>**: Use analyzer hand
* **exit**: Quit the program

## 📄 Documentation

For more details, see:
* [Architecture Guide](docs/ARCHITECTURE.md)
* [GitHub Setup](GITHUB_SETUP.md)
* [Contributing](CONTRIBUTING.md)

---
_🍊 Chicka chicka orange._
