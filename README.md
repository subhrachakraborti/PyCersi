# PyCersi

![Python Versions](https://img.shields.io/pypi/pyversions/pycersi?color=FF8C00&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/PyCersi?style=for-the-badge&color=FFD700)
![License](https://img.shields.io/badge/License-MIT-green.svg?color=008080&style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/subhrachakraborti/pycersi?style=for-the-badge&display_date=published_at&logoSize=auto&color=708090)
![GitHub Release](https://img.shields.io/github/v/release/subhrachakraborti/pycersi?sort=date&display_name=release&style=for-the-badge)

##### DEVELOPED BY SUBHRA CHAKRABORTI

##### LAST UPDATE: 14 DECEMBER 2024

##### VERSION: 5.5.0

## Overview

PyCersi is a simple Python library that provides essential tools for number functions (described below).
It is easy to use, lightweight, and can be integrated into various Python projects.

## Features

PyCersi offers a collection of number-related utilities that can simplify common mathematical tasks:

- **Mathematical Constants**

  - `Euler's Constant (e)`
  - `Golden Ratio (GR)`
  - `Logarithm of e (loge)`
  - `Pi (pi)`

- **Physical Constants**

  - `Astronomical Unit (AU)`
  - `Bohr Radius (a0)`
  - `Electric Permitivity (Eo)`
  - `Elementary Charge (Q)`
  - `Fine Structure Constant (fsc)`
  - `Gravitational Constant (G)`
  - `Light Year (LY)`
  - `Magnetic Permeability (Muo)`
  - `Mass of Earth (ME)`
  - `Mass of Electron (me)`
  - `Mass of Neutron (mn)`
  - `Mass of Proton (mp)`
  - `Mass of Sun (MS)`
  - `Planck's Constant (h)`
  - `Parsec (PC)`
  - `Reduced Plank Constant (hbar)`
  - `Speed of Light (c)`

- **Additional Constants**

  - `Avogadro's Number (NA)`
  - `Boltzmann Constant (BK)`
  - `Chandrashekhar Limit (CSK)`
  - `Faraday's Constant (F)`
  - `Gas Constant (R)`
  - `Hubble's Constant (H)`
  - `Stefan-Boltzmann Constant (SBK)`

- **Searchers**

  - `Fibonacci Upto Program : fiboupto`
  - `Fibonacci Range Program : fiborange`
  - `Floyd Triangle Program`
  - `Greatest Common Divisor Program`
  - `Least Common Multiple Program`

- **Number Property Checkers**

  - `Abundant Number Checker`
  - `Armstrong Number Checker`
  - `Automorphic Number Checker`
  - `Buzz Number Checker`
  - `Circular Prime Number Checker`
  - `Curzon Number Checker`
  - `Composite Number Checker`
  - `CoPrime Number Checker`
  - `Disarium Number Checker`
  - `Dudeney Number Checker`
  - `Duck Number Checker`
  - `Even Number Checker`
  - `Fibonacci Number Checker`
  - `Happy Number Checker`
  - `Harshad Number Checker`
  - `Heteromecic Number Checker`
  - `Krishnamurthy Number Checker`
  - `Magic Number Checker`
  - `Neon Number Checker`
  - `Niven Number Checker`
  - `Oblong Number Checker`
  - `Odd Number Checker`
  - `Palindrome Number Checker`
  - `Perfect Number Checker`
  - `Prime Number Checker`
  - `Pronic Number Checker`
  - `Sunny Number Checker`
  - `Special Number Checker`
  - `Spy Number Checker`
  - `Twin Prime Number Checker`
  - `Twisted Prime Checker`
  - `Unique Number Checker`
  - `Tech Number Checker`
  - `Ugly Number Checker`

- **Mathematical Functions**

  - `Area of Circle : ar_circle`
  - `Area of Rectangle : ar_rect`
  - `Area of Triangle : ar_triangle`
  - `Combination Calculator : comb`
  - `Digit to Word Converter : digiwords`
  - `Factorial Calculator : fact`
  - `Factors Calculator : factor`
  - `Permutation Calculator : perm`

- **Stack Functions**

  - `Push Into Stack : s_push`
  - `Pop Out Of Stack : s_push`
  - `Size Of Stack : s_size`
  - `Underflow Stack Checker : s_empty`
  - `Top Of Stack : s_top`
  - `Display Stack : s_display`

- **PyCersi Privator _(Tkinter Module is required)_**

  - `Data Encryptor`
  - `Data Decryptor`

These functions are designed to help you perform common number-related operations efficiently and can be easily integrated into larger projects.

## Installation

PyCersi is available on PyPI and can be installed using `pip` on various platforms including Windows, macOS, and Linux.

### Windows

1. **Install Python**: Make sure Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).
2. **Open Command Prompt**: Press `Win + R`, type `cmd`, and hit Enter.
3. **Run the pip command**:

```bash
   pip install pycersi
```

### macOS

1. **Install Python**: Ensure Python is installed. You can use Homebrew to install it:

```bash
   brew install python
```

2. **Open Terminal**: You can find Terminal in Applications > Utilities.

```bash
   pip3 install pycersi
```

### Linux (Ubuntu/Debian-based)

1. **Update Packages**:

```bash
   sudo apt update
```

2. **Install Python and pip**:

```bash
   sudo apt install python3 python3-pip
```

3. **Run the pip command**:

```bash
   pip3 install pycersi
```

## Using The Functions

1. For using any _searchers_ functions from PyCersi module, use:
   `pycersi.<name>(limit)`.

   - Example: `pycersi.fibo(limit)`

2. For using any _checker_ functions from PyCersi module, use:
   `pycersi.is<name>(value)`.

   - Example: `pycersi.issunny(value)`

3. For using any _mathematical_ function from PyCersi module, use:
   `pycersi.cal<name>(value)`.

   - Example: `pycesi.calfact(value)`

4. For using any _stack_ function from PyCersi module, use:
   `pycersi.s_<name>(stack,[element])`.

   - Example: `pycesi.s_top(book_stack)`

5. For using _Pycersi Privator_, use:
   `pycersi.privator()`.

   - Example: `pycersi.privator()`

## Contributing

I welcome contributions to the project! If you want to contribute, please follow these steps:

### Steps to Contribute:

1. **Fork the repository**:

   - Click the "Fork" button at the top right of the repository page to create a copy of the repository on your GitHub account.

2. **Create a new branch**:

   - Clone your forked repository to your local machine.
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature-branch
     ```

3. **Make your changes**:

   - Make sure your changes follow the project's coding standards.
   - Once you're satisfied with your changes, commit them:
     ```bash
     git commit -m 'Add some feature'
     ```

4. **Push your changes**:

   - Push your changes to your forked repository:
     ```bash
     git push origin feature-branch
     ```

5. **Create a pull request**:
   - Open a pull request from your feature branch in your forked repository to the main branch in the original repository.
   - Please ensure that your code includes relevant tests and follows the project's guidelines.

### Guidelines:

- **Code Style**: Ensure your code follows the project's coding style and is well-structured.
- **Testing**: Make sure that your code is tested and includes appropriate unit tests.
- **Documentation**: Update documentation if necessary for any changes or new features.
- **Pull Request Review**: Be patient as maintainers review your pull request and possibly request changes.

Thank you for contributing to PyCersi! Your help is appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/subhrachakraborti/PyCersi/blob/main/LICENSE) file for details.

## Security & Safety

This project is designed to simplify and accelerate everyday tasks, making your work life smoother and more efficient. It is crafted with the utmost care and attention to detail, ensuring that no security vulnerabilities or exceptions occur during its runtime.

I am deeply committed to making the web a better, safer place. This project is not malware, and any attempt to misuse it as such is highly condemnable and goes against its core purpose. Let’s work together to create a positive impact and enhance our digital experiences.

- [SafetyCLI Certificate](https://data.safetycli.com/packages/pypi/pycersi/)

## Contact

If you have any questions, feel free to open an issue or contact me directly at [mail@subhrachakraborti](mailto:mail@subhrachakraborti.com).

## Acknowledgments

- Math Library
- Tkinter Module
- Python Org
- Visual Studio Code
- GitHub
- Microsoft Corporation
- SafetyCLI
