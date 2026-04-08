# Generated from ViperLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ViperLangParser import ViperLangParser
else:
    from ViperLangParser import ViperLangParser

# This class defines a complete listener for a parse tree produced by ViperLangParser.
class ViperLangListener(ParseTreeListener):

    # Enter a parse tree produced by ViperLangParser#prog.
    def enterProg(self, ctx:ViperLangParser.ProgContext):
        pass

    # Exit a parse tree produced by ViperLangParser#prog.
    def exitProg(self, ctx:ViperLangParser.ProgContext):
        pass


    # Enter a parse tree produced by ViperLangParser#printStat.
    def enterPrintStat(self, ctx:ViperLangParser.PrintStatContext):
        pass

    # Exit a parse tree produced by ViperLangParser#printStat.
    def exitPrintStat(self, ctx:ViperLangParser.PrintStatContext):
        pass


    # Enter a parse tree produced by ViperLangParser#assignStat.
    def enterAssignStat(self, ctx:ViperLangParser.AssignStatContext):
        pass

    # Exit a parse tree produced by ViperLangParser#assignStat.
    def exitAssignStat(self, ctx:ViperLangParser.AssignStatContext):
        pass


    # Enter a parse tree produced by ViperLangParser#ifStat.
    def enterIfStat(self, ctx:ViperLangParser.IfStatContext):
        pass

    # Exit a parse tree produced by ViperLangParser#ifStat.
    def exitIfStat(self, ctx:ViperLangParser.IfStatContext):
        pass


    # Enter a parse tree produced by ViperLangParser#whileStat.
    def enterWhileStat(self, ctx:ViperLangParser.WhileStatContext):
        pass

    # Exit a parse tree produced by ViperLangParser#whileStat.
    def exitWhileStat(self, ctx:ViperLangParser.WhileStatContext):
        pass


    # Enter a parse tree produced by ViperLangParser#intExpr.
    def enterIntExpr(self, ctx:ViperLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by ViperLangParser#intExpr.
    def exitIntExpr(self, ctx:ViperLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by ViperLangParser#addSubExpr.
    def enterAddSubExpr(self, ctx:ViperLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ViperLangParser#addSubExpr.
    def exitAddSubExpr(self, ctx:ViperLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ViperLangParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:ViperLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ViperLangParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:ViperLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ViperLangParser#idExpr.
    def enterIdExpr(self, ctx:ViperLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by ViperLangParser#idExpr.
    def exitIdExpr(self, ctx:ViperLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by ViperLangParser#compareExpr.
    def enterCompareExpr(self, ctx:ViperLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by ViperLangParser#compareExpr.
    def exitCompareExpr(self, ctx:ViperLangParser.CompareExprContext):
        pass



del ViperLangParser