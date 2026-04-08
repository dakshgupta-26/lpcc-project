🚀 ViperLang: Advanced Compiler Studio
A Full-Stack, Web-Based Compiler Implementation using ANTLR4 and Python

📖 Table of Contents
Project Overview
Why This Project? (Motivation)
System Architecture: How ANTLR Works Here
Core Features
Language Specification
Project Structure & File Definitions
Installation & Execution

📌 Project Overview
ViperLang is a custom, dynamically-typed programming language accompanied by a fully functional web-based Compiler Studio. Unlike standard academic compiler projects that stop at syntax validation (Parsing), this project features a complete end-to-end pipeline. It reads source code, generates an Abstract Syntax Tree (AST) using ANTLR4, and executes the logic in real-time using a custom Python-based Execution Engine (Visitor Pattern).

The entire environment is hosted on a modern Streamlit web dashboard, providing a visual, IDE-like experience complete with syntax highlighting, live memory tracking, and execution tracing.

💡 Why This Project? (Motivation)
The primary goal of this project was to bridge the gap between theoretical compiler design and practical software engineering.

The Problem: Most beginner compiler projects only build a Lexer and Parser, outputting a static tree without actually running the code.

The Solution: By implementing the Visitor Design Pattern, this project steps into Semantic Analysis and Execution. It demonstrates how compilers manage memory (Symbol Tables), evaluate mathematical expressions, and handle control flow (like while loops and if statements) at runtime.

⚙️ System Architecture: How ANTLR Works Here
This compiler operates in three distinct phases, seamlessly blending Java-based ANTLR generation with Python-based execution.

Phase 1: Lexical Analysis (The Lexer)
What it does: The Lexer reads the raw text input (e.g., score = 9;) character by character and groups them into meaningful Tokens (e.g., ID, ASSIGN, INT, SEMI).

How ANTLR handles it: Defined in ViperLang.g4, ANTLR auto-generates ViperLangLexer.py. If it encounters an invalid character, it throws a Lexical Error.

Phase 2: Syntax Analysis (The Parser & AST)
What it does: The Parser takes the stream of Tokens and checks them against the grammatical rules defined in our .g4 file.

How ANTLR handles it: If the grammar is mathematically correct, ANTLR builds an Abstract Syntax Tree (AST). This tree represents the hierarchical structure of the code. For example, an addition operation becomes a parent node (+) with two child nodes representing the numbers.

Phase 3: Semantic Execution (The Custom Visitor)
What it does: ANTLR itself does not execute code. It only builds the tree. To actually run the code, we built a custom Python class (ViperExecutionEngine) that inherits from ANTLR's ViperLangVisitor.

How it works: The engine "walks" down the AST. When it visits an assignment node (score = 9), it allocates memory in a Python Dictionary (acting as our Symbol Table). When it visits a while loop, it recursively evaluates the condition and executes the inner statements until the condition becomes false.

✨ Core Features
Modern Web IDE (Streamlit-Ace): * Embedded code editor with Monokai dark theme, syntax highlighting, line numbers (gutters), and auto-update capabilities.

Live AST Visualization (Graphviz): * Dynamically generates and renders the mathematical tree structure of the parsed code on the dashboard.

Real-Time Semantic Execution: * Executes the code immediately upon successful compilation and displays standard output in a dedicated Console UI.

Live Symbol Table (Memory Manager): * A dynamic data table (built with Pandas) that tracks variable states, allocations, and mutations during runtime.

Robust Error Handling Architecture:

Syntax Errors: Caught by a custom ANTLR ErrorListener (e.g., missing semicolons).

Semantic Errors: Caught by the Execution Engine (e.g., using undefined variables, division by zero).

Compiler Thought-Process Logger (Trace):

An expandable logging interface that reveals the compiler's internal state—showing iteration counts, memory assignments, and decision-making for conditional branches.

📜 Language Specification (ViperLang)
ViperLang is a dynamically typed language. Data types (Integers, Floats) are inferred at runtime, eliminating the need for strict type declarations (like int or float). It strictly utilizes the semicolon ; as a Statement Terminator to resolve multi-line ambiguities.

// Variable Initialization
score = 9;
bonus = 5;

// While Loop Execution
count = 1;
while (count < 4) {
    print(count);
    count = count + 1;
}

// Conditional Logic
if (score > 5) {
    print(score + bonus);
}

File Name,Purpose and Technical Details
ViperLang.g4,The Grammar Blueprint: Contains the Lexer and Parser rules. It dictates the syntax of ViperLang using ANTLR's meta-language.
app.py,"The Control Center: The main Streamlit Python script. It wires together the UI, the AST Graph generator, the Custom Error Listeners, and the Execution Engine."
ViperLangLexer.py,(Auto-generated) The Python class responsible for Tokenizing the input string.
ViperLangParser.py,(Auto-generated) The Python class responsible for enforcing syntax rules and generating the raw AST.
ViperLangVisitor.py,"(Auto-generated) The base class interface provided by ANTLR, which we override in app.py to create our Execution logic."
antlr-4.13.2-complete.jar,The core ANTLR Java binary used to compile the .g4 file into Python components.

💻 Installation & Execution
Prerequisites
Python 3.8+

Java Runtime Environment (JRE) 11+ (Required to run the ANTLR tool)

Step 1: Install Python Dependencies
Bash
pip install streamlit graphviz antlr4-python3-runtime pandas streamlit-ace
Step 2: Generate the Parser (If Grammar is modified)
Run the following command to translate the .g4 grammar into Python files:

Bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor ViperLang.g4
Step 3: Launch the Compiler Studio
Bash
streamlit run app.py
