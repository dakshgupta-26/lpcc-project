import streamlit as st
import graphviz
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ViperLangLexer import ViperLangLexer
from ViperLangParser import ViperLangParser
from ViperLangVisitor import ViperLangVisitor
from antlr4.tree.Tree import TerminalNodeImpl
import pandas as pd
from streamlit_ace import st_ace  # 🔥 NAYI LIBRARY FOR REAL IDE 🔥

# --- MODERN UI INJECTION ---
st.set_page_config(page_title="Viper Compiler Studio", layout="wide")
st.markdown("""
    <style>
    .stButton>button { background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%); color: black !important; font-weight: bold; border-radius: 8px; border: none; transition: 0.3s; width: 100%; margin-top: 10px;}
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 4px 15px rgba(0, 201, 255, 0.4); }
    .console-box { background-color: #0d0d0d; color: #00ff00; padding: 15px; border-radius: 8px; font-family: monospace; height: 150px; overflow-y: auto; border: 1px solid #333;}
    </style>
""", unsafe_allow_html=True)

st.title("🚀 ViperLang: Advanced Compiler Studio")
st.markdown("Lexical Analysis • AST Graph • Semantic Execution • **Robust Error Handling**")


# --- CUSTOM ERROR LISTENER ---
class ViperErrorListener(ErrorListener):
    def __init__(self):
        super(ViperErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")


# --- EXECUTION ENGINE ---
class ViperExecutionEngine(ViperLangVisitor):
    def __init__(self):
        self.memory = {}
        self.console = []

    def visitAssignStat(self, ctx: ViperLangParser.AssignStatContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrintStat(self, ctx: ViperLangParser.PrintStatContext):
        value = self.visit(ctx.expr())
        self.console.append(str(value))
        return value

    def visitIfStat(self, ctx: ViperLangParser.IfStatContext):
        condition = self.visit(ctx.expr())
        if condition:
            for statement in ctx.stat():
                self.visit(statement)
        return 0

    def visitCompareExpr(self, ctx: ViperLangParser.CompareExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '==': return left == right
        return False

    def visitMulDivExpr(self, ctx: ViperLangParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*': return left * right
        if right == 0:
            raise ValueError("Math Error: Division by zero is not allowed!")
        return left / right

    def visitAddSubExpr(self, ctx: ViperLangParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+': return left + right
        return left - right

    def visitIntExpr(self, ctx: ViperLangParser.IntExprContext):
        return int(ctx.INT().getText())

    def visitIdExpr(self, ctx: ViperLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            raise ValueError(f"Semantic Error: Variable '{var_name}' is not defined!")
        return self.memory[var_name]


# --- AST GRAPH BUILDER ---
def build_graph(tree, parser, graph, parent_id=None, node_counter=0):
    node_id = str(node_counter)
    if isinstance(tree, TerminalNodeImpl):
        graph.node(node_id, f"{tree.getText()}", shape="rect", style="rounded,filled", fillcolor="#2b2b2b",
                   fontcolor="#00ffcc", fontname="Courier")
    else:
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        graph.node(node_id, rule_name, shape="ellipse", style="filled", fillcolor="#4a4a4a", fontcolor="white",
                   fontname="Helvetica-Bold")
    if parent_id is not None:
        graph.edge(parent_id, node_id, color="#666666")
    node_counter += 1
    if hasattr(tree, 'children') and tree.children is not None:
        for child in tree.children:
            node_counter = build_graph(child, parser, graph, node_id, node_counter)
    return node_counter


# --- UI LAYOUT ---
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("📝 Source Code Editor")
    default_code = "score = 90;\nprint(s);\n"

    # 🔥 YAHAN ASLI IDE (ACE EDITOR) LAGA DIYA HAI 🔥
    source_code = st_ace(
        value=default_code,
        language='c_cpp',  # Gives correct syntax coloring for semicolons/braces
        theme='monokai',  # Premium Dark IDE Theme
        show_gutter=True,  # THIS ENABLES LINE NUMBERS (1, 2, 3...)
        font_size=16,
        height=250,
        key="ace_editor"
    )

    if st.button("Compile & Execute", type="primary"):
        if source_code.strip() != "":
            error_listener = ViperErrorListener()

            # 1. Lexical Analysis
            input_stream = InputStream(source_code)
            lexer = ViperLangLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)

            stream = CommonTokenStream(lexer)
            stream.fill()

            # 2. Parsing
            parser = ViperLangParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            tree = parser.prog()

            if len(error_listener.errors) > 0:
                st.error("❌ Syntax Errors Found! Compilation Stopped.")
                for err in error_listener.errors:
                    st.warning(err)
            else:
                try:
                    # 3. Execution
                    engine = ViperExecutionEngine()
                    engine.visit(tree)

                    st.subheader("🔍 Lexical Tokens")
                    token_output = ""
                    for token in stream.tokens:
                        if token.type != Token.EOF:
                            token_name = lexer.symbolicNames[token.type] if (
                                        0 <= token.type < len(lexer.symbolicNames)) else "SYMBOL"
                            token_output += f"<b style='color:#ff9900;'>{token_name}</b> : '{token.text}' <br>"
                    st.markdown(
                        f"<div style='background-color:#111; padding:10px; border-radius:5px; height:120px; overflow-y:auto; font-family:monospace;'>{token_output}</div>",
                        unsafe_allow_html=True)

                    with col2:
                        st.subheader("🌳 Abstract Syntax Tree")
                        dot = graphviz.Digraph(comment='AST',
                                               graph_attr={'rankdir': 'TB', 'bgcolor': 'transparent', 'size': '8,5'})
                        build_graph(tree, parser, dot)
                        st.graphviz_chart(dot.source, use_container_width=True)

                        c_out, c_mem = st.columns(2)
                        with c_out:
                            st.subheader("💻 Console Output")
                            out_text = "<br>".join(engine.console) if engine.console else "No output"
                            st.markdown(f"<div class='console-box'> > Executing...<br>> {out_text}</div>",
                                        unsafe_allow_html=True)

                        with c_mem:
                            st.subheader("🧠 Symbol Table (Memory)")
                            if engine.memory:
                                df = pd.DataFrame(list(engine.memory.items()), columns=['Variable Name', 'Value (Int)'])
                                st.dataframe(df, use_container_width=True, hide_index=True)
                            else:
                                st.info("Memory is empty.")

                except ValueError as ve:
                    st.error("⚠️ Runtime / Semantic Error!")
                    st.warning(str(ve))
                except Exception as e:
                    st.error(f"Critical Execution Error: {e}")