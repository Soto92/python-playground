# Quantum-Resistant Algorithms and PoC for CRYSTALS-Kyber

This repository provides an overview of quantum-resistant cryptographic algorithms and a Proof of Concept (PoC) for encrypting and decrypting a string using the **CRYSTALS-Kyber** algorithm, a post-quantum key encapsulation mechanism (KEM).

---

## Table of Contents

1. [Overview of Quantum-Resistant Algorithms](#overview-of-quantum-resistant-algorithms)
   - [Why Quantum-Resistant Algorithms?](#why-quantum-resistant-algorithms)
   - [Types of Quantum-Resistant Algorithms](#types-of-quantum-resistant-algorithms)
2. [CRYSTALS-Kyber](#crystals-kyber)
   - [What is CRYSTALS-Kyber?](#what-is-crystals-kyber)
   - [How Does It Work?](#how-does-it-work)
3. [Proof of Concept (PoC)](#proof-of-concept-poc)
   - [What Does the PoC Do?](#what-does-the-poc-do)
   - [How to Run the PoC](#how-to-run-the-poc)
4. [Dependencies](#dependencies)
5. [References](#references)

---

## Overview of Quantum-Resistant Algorithms

### Why Quantum-Resistant Algorithms?

Quantum computers, once fully realized, will be capable of breaking many of the cryptographic algorithms currently in use (e.g., RSA, ECC) by leveraging algorithms like **Shor's algorithm**. To prepare for this, **post-quantum cryptography** (PQC) focuses on developing algorithms that are resistant to attacks by both classical and quantum computers.

### Types of Quantum-Resistant Algorithms

The **National Institute of Standards and Technology (NIST)** is leading the effort to standardize post-quantum cryptographic algorithms. These algorithms fall into several categories:

1. **Lattice-Based Cryptography**:

   - Examples: CRYSTALS-Kyber, NTRU, SABER
   - Based on the hardness of problems like Learning With Errors (LWE) and Shortest Vector Problem (SVP).

2. **Hash-Based Cryptography**:

   - Examples: SPHINCS+
   - Relies on the security of cryptographic hash functions.

3. **Code-Based Cryptography**:

   - Examples: Classic McEliece
   - Based on error-correcting codes.

4. **Multivariate Cryptography**:

   - Examples: Rainbow
   - Based on the difficulty of solving systems of multivariate equations.

5. **Isogeny-Based Cryptography**:
   - Examples: SIKE
   - Based on the mathematics of elliptic curve isogenies.

---

## CRYSTALS-Kyber

### What is CRYSTALS-Kyber?

**CRYSTALS-Kyber** is a **key encapsulation mechanism (KEM)** based on lattice cryptography. It was selected by NIST in July 2022 as one of the standardized algorithms for post-quantum cryptography. Kyber is designed to be efficient and secure against attacks by both classical and quantum computers.

### How Does It Work?

Kyber uses the **Learning With Errors (LWE)** problem to generate a shared secret between two parties. The process involves:

1. **Key Generation**: A public-private key pair is generated.
2. **Encapsulation**: The sender uses the recipient's public key to encrypt a shared secret.
3. **Decapsulation**: The recipient uses their private key to decrypt the shared secret.

---

## Proof of Concept (PoC)

### What Does the PoC Do?

This PoC demonstrates how to:

1. Generate a public-private key pair using **CRYSTALS-Kyber**.
2. Encrypt a message (string) into a shared secret.
3. Decrypt the shared secret back into the original message.
4. Verify that the encryption and decryption processes work correctly.

### How to Run the PoC

#### Prerequisites

- Python 3.7 or later
- CMake
- Visual Studio Build Tools (for Windows)
- Git

#### Steps

1. **Install Dependencies**:

   - Install `liboqs` and `liboqs-python` by following the instructions in the [Setup Guide](#setup-guide).

2. **Run the PoC Script**:
   ```bash
   python poc_kyber.py
   ```
