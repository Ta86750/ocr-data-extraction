# N-Queens Problem Solver

## Description

This project solves the **N-Queens Problem** using the **backtracking** algorithm in **C++**. The N-Queens problem is a classic problem in computer science, where the goal is to place `N` queens on an `N x N` chessboard such that no two queens can attack each other. That is, no two queens should share the same row, column, or diagonal.

The program uses **backtracking** to explore all possible configurations of placing queens on the board and returns all valid solutions for any given value of `N`.

## Problem Statement

Given an integer `N`, the objective is to place `N` queens on an `N x N` chessboard in such a way that no two queens threaten each other. A queen can attack another queen if they share the same row, column, or diagonal.

## Algorithm

- The program uses **backtracking** to solve the problem.
- It recursively places queens on the board, checking if the current placement is valid.
- If the current placement is invalid (i.e., queens threaten each other), the algorithm backtracks and tries the next placement.
- The program prints all possible valid configurations where `N` queens can be placed on the board.

## Features

- **Backtracking Algorithm**: Efficient solution using recursion and backtracking.
- **All Solutions**: Outputs all possible configurations for placing `N` queens.
- **Flexible Input**: Supports any value of `N` to find solutions for any chessboard size.

## How to Run

### Prerequisites

To run this project, you must have **C++** and **g++** installed on your machine.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/n-queens-solver.git

