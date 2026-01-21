# TOPSIS Implementation in Python

## Overview

This project provides a Python-based implementation of the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**, a well-known multi-criteria decision-making (MCDM) method. The tool helps rank multiple alternatives by comparing them against an ideal best and an ideal worst solution based on user-defined criteria, weights, and impacts.

The package is designed to be simple to use, robust against invalid inputs, and suitable for academic as well as practical decision-making scenarios.

---

## What is TOPSIS?

TOPSIS is a decision-making technique used when multiple, often conflicting, criteria must be considered simultaneously. The core idea is to choose the alternative that is **closest to the ideal solution** and **farthest from the worst solution**.

Key characteristics:

* Works with quantitative criteria
* Allows both benefit (`+`) and cost (`-`) criteria
* Produces a relative performance score for each alternative

---

## Package Features

* Supports any number of alternatives and criteria
* Handles both positive and negative impacts
* Automatic input validation with meaningful error messages
* Outputs TOPSIS scores and final rankings in CSV format
* Can be executed via command line or Python module

---

## Installation

Clone or download the project and install it locally using:

```bash
pip install .
```

Ensure that Python **3.8 or higher** is installed on your system.

---

## Input File Format

The input must be a CSV file with the following structure:

* **First column**: Names/IDs of alternatives
* **Remaining columns**: Numerical values for criteria

### Example

```csv
Alternative,C1,C2,C3,C4
A1,250,16,12,5
A2,200,20,8,3
A3,300,14,16,4
```

---

## Command-Line Usage

After installation, the package can be executed using:

```bash
topsis-pushkar-manocha-102303751 <input_file> <weights> <impacts> <output_file>
```

### Example

```bash
topsis-pushkar-manocha-102303751 input.csv "1,1,1,1,1" "+,+,-,+,+" output.csv
```

---

## Alternative Execution Method (Recommended)

If the command-line script is not detected on your system, you can run the program using the Python module interface:

```bash
python -m topsis_pushkar_manocha_102303751.cli input.csv "1,1,1,1,1" "+,+,-,+,+" output.csv
```

This method avoids environment and PATH-related issues.

---

## Output Format

The output CSV file contains:

* Original input data
* **TOPSIS Score** for each alternative
* **Rank**, where rank 1 indicates the best alternative

### Notes

* TOPSIS scores range between **0 and 1**
* Higher scores indicate better alternatives

---

## Methodology

The algorithm follows these steps:

1. Construct the decision matrix from input data
2. Normalize the decision matrix
3. Apply weights to normalized values
4. Determine ideal best and ideal worst values
5. Compute separation measures from ideal solutions
6. Calculate TOPSIS scores
7. Rank alternatives based on scores

---

## Mathematical Formulation

Let the decision matrix be (X = [x_{ij}]):

1. **Normalization**
   r_ij = x_ij / sqrt( Σ x_ij² )

2. **Weighted Normalization**
   v_ij = w_j × r_ij

3. **Ideal Solutions**

   * Benefit criterion (`+`): best = max, worst = min
   * Cost criterion (`-`): best = min, worst = max

4. **Separation Measures**
   S_i+ = √(Σ (v_ij − v_j+)²)
   S_i− = √(Σ (v_ij − v_j−)²)

5. **TOPSIS Score**
   C_i = S_i− / (S_i+ + S_i−)

---

## Input Validation Rules

The program checks for the following conditions:

* Input file must exist and be in CSV format
* All criteria values must be numeric
* Number of weights must match number of criteria
* Number of impacts must match number of criteria
* Impacts must be either `+` or `-`

Errors are reported with clear messages for easy debugging.

---

## Build and Distribution (Optional)

For packaging or publishing purposes:

```bash
python -m build
python -m twine upload dist/*
```

---

## Applications

* Supplier or vendor selection
* Product comparison
* Academic decision-making problems
* Engineering and management analysis

---

## Author

**Pushkar Manocha**

Roll No: 102303751

Thapar Institute of Engineering and Technology

---

## License

This project is intended for **academic and educational use** as part of a university assignment. Redistribution or reuse should acknowledge the author.

