
# 🚀 ViperLang: Advanced Compiler Studio

### A Full-Stack Web-Based Compiler using ANTLR4 + Python

## 📖 Table of Contents

* [📌 Project Overview](#-project-overview)
* [💡 Motivation](#-motivation)
* [⚙️ System Architecture](#️-system-architecture)
* [✨ Core Features](#-core-features)
* [📜 Language Specification](#-language-specification)
* [📂 Project Structure](#-project-structure)
* [💻 Installation & Execution](#-installation--execution)

## 📌 Project Overview

ViperLang is a custom dynamically-typed programming language with a fully functional **web-based Compiler Studio**.

Unlike traditional academic compiler projects (which stop at parsing), this project implements a **complete end-to-end compilation pipeline**:

* Source Code Input
* Tokenization (Lexer)
* Parsing → AST Generation
* Semantic Execution (Visitor Pattern)

The entire system runs inside a **Streamlit-powered web IDE**, offering:

* Real-time execution
* AST visualization
* Memory tracking
* Debug tracing

---

## 💡 Motivation

### ❌ Problem

Most beginner compiler projects:

* Only build Lexer + Parser
* Do NOT execute code
* Provide static AST output

### ✅ Solution

ViperLang goes beyond theory by implementing:

* **Visitor Design Pattern**
* **Runtime Execution Engine**
* **Symbol Table (Memory Management)**
* **Control Flow Handling**

This bridges the gap between:

> 📚 Compiler Theory → 🧠 Real-World Implementation

## ⚙️ System Architecture

The compiler works in **3 main phases**:

### 🧩 Phase 1: Lexical Analysis (Lexer)

**What it does:**

* Converts raw input into tokens
  Example:

  ```
  score = 9;
  ```

  → `ID`, `ASSIGN`, `INT`, `SEMI`

**ANTLR Role:**

* Defined in `ViperLang.g4`
* Generates: `ViperLangLexer.py`

### 🌳 Phase 2: Syntax Analysis (Parser + AST)

**What it does:**

* Validates syntax rules
* Builds **Abstract Syntax Tree (AST)**

Example:

```
5 + 3
```

→ Tree with `+` as root and `5`, `3` as children

**ANTLR Role:**

* Generates:

  * `ViperLangParser.py`
  * AST structure

### ⚡ Phase 3: Semantic Execution (Visitor Pattern)

**What it does:**

* Executes the AST
* Manages variables using a **Symbol Table (Python Dictionary)**

**Example:**

```
score = 9;
```

→ Stored in memory

```
while (count < 4)
```

→ Loop executed dynamically

---

## ✨ Core Features

### 🖥️ Modern Web IDE (Streamlit-Ace)

* Dark theme (Monokai)
* Syntax highlighting
* Line numbers
* Live editing

---

### 🌳 Live AST Visualization (Graphviz)

* Displays program structure visually
* Helps understand parsing behavior

---

### ⚡ Real-Time Execution

* Code runs instantly after compilation
* Output shown in console UI

---

### 📊 Live Symbol Table (Memory Manager)

* Built with Pandas
* Tracks:

  * Variable values
  * Updates
  * Memory state

---

### 🚨 Robust Error Handling

* **Syntax Errors**

  * Missing semicolons
  * Invalid grammar

* **Semantic Errors**

  * Undefined variables
  * Division by zero

---

### 🧠 Compiler Trace Logger

* Shows internal working:

  * Loop iterations
  * Variable updates
  * Condition evaluations

---

## 📜 Language Specification (ViperLang)

### 🔹 Features

* Dynamically typed
* No explicit type declaration
* Uses `;` as statement terminator

---

### 🧪 Example Programs

#### ✅ Variable Initialization

```c
score = 9;
bonus = 5;
```

#### 🔁 While Loop

```c
count = 1;
while (count < 4) {
    print(count);
    count = count + 1;
}
```

#### 🔀 Conditional

```c
if (score > 5) {
    print(score + bonus);
}
```

---

## 📂 Project Structure

| File Name                   | Description                                |
| --------------------------- | ------------------------------------------ |
| `ViperLang.g4`              | Grammar file (Lexer + Parser rules)        |
| `app.py`                    | Main Streamlit app (UI + Execution Engine) |
| `ViperLangLexer.py`         | Tokenizer (auto-generated)                 |
| `ViperLangParser.py`        | Parser + AST generator (auto-generated)    |
| `ViperLangVisitor.py`       | Base visitor class (auto-generated)        |
| `antlr-4.13.2-complete.jar` | ANTLR tool for code generation             |

---

## 💻 Installation & Execution

### 🔧 Prerequisites

* Python **3.8+**
* Java **JRE 11+**

### 📦 Step 1: Install Dependencies

pip install streamlit graphviz antlr4-python3-runtime pandas streamlit-ace


### ⚙️ Step 2: Generate Parser (if grammar changes)


java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor ViperLang.g4


### 🚀 Step 3: Run the Compiler Studio

streamlit run app.py


## 🎯 Final Thoughts

ViperLang is not just a compiler project — it's a **complete interactive system** that demonstrates:

* Compiler design concepts
* Runtime execution
* Memory management
* Real-world software integration



Just tell me 👍
