# Computational Mathematics

## Overview

This repository contains a collection of algorithms and methods used in computational mathematics. It aims to provide resources for solving mathematical problems using computational techniques, including numerical analysis, optimization, and simulations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure and Descriptions](#folder-structure)
- [Contributing](#contributing)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/naskeriya/computational-mathematics.git
   cd computational-mathematics
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python main.py
   ```

## Usage

After installation, you can run various scripts and modules to perform computations. Refer to the specific files in the folder structure for detailed usage instructions.

## Folder Structure and Descriptions

```plaintext
computational-mathematics/
│
├── curve_fitting/                     # Directory for curve fitting algorithms
│   ├── best_fit.py                     # Implements the best-fit line for a set of data points
│   ├── exponential_curve.py            # Fits an exponential curve to the data
│   ├── logarithmic_curve.py            # Fits a logarithmic curve to the data
│   ├── power_curve.py                  # Fits a power curve to the data
│   ├── quadratic_curve.py              # Fits a quadratic curve to the data
│   └── straight_line.py                # Fits a straight line to the data
│
├── equations/                          # Directory for solving equations using various methods
│   ├── all_methods.py                   # Contains implementations of all available methods for solving equations
│   ├── bisection_method.py              # Implements the bisection method for root finding
│   ├── false_position_method.py         # Implements the false position method for root finding
│   ├── fixed_point_method.py            # Implements the fixed-point iteration method
│   ├── graphical_method.py              # Uses graphical methods to find roots of equations
│   ├── mullers_method.py                # Implements Muller's method for finding roots
│   ├── newton_raphson_method.py         # Implements Newton-Raphson method for root finding
│   └── secant_method.py                 # Implements the secant method for root finding
│
├── finite_difference_and_interpolation/ # Directory for finite difference and interpolation methods
│   └── difference_interpolation.py       # Implements finite difference methods for interpolation
│
├── numerical_integration/               # Directory for numerical integration methods
│   └── numerical_methods.py              # Contains various numerical integration techniques (e.g., Trapezoidal, Simpson's rule)
│
├── systems/                             # Directory for solving systems of equations
│   ├── direct_method.py                  # Implements direct methods for solving systems (e.g., Gaussian elimination)
│   └── iterative_method.py               # Implements iterative methods for solving systems (e.g., Gauss-Seidel)
│
└── README.md                            # This README file, providing an overview of the project
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

