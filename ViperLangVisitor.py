# Generated from ViperLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ViperLangParser import ViperLangParser
else:
    from ViperLangParser import ViperLangParser

# This class defines a complete generic visitor for a parse tree produced by ViperLangParser.

class ViperLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ViperLangParser#prog.
    def visitProg(self, ctx:ViperLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#printStat.
    def visitPrintStat(self, ctx:ViperLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#assignStat.
    def visitAssignStat(self, ctx:ViperLangParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#ifStat.
    def visitIfStat(self, ctx:ViperLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#whileStat.
    def visitWhileStat(self, ctx:ViperLangParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#intExpr.
    def visitIntExpr(self, ctx:ViperLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ViperLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ViperLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#idExpr.
    def visitIdExpr(self, ctx:ViperLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ViperLangParser#compareExpr.
    def visitCompareExpr(self, ctx:ViperLangParser.CompareExprContext):
        return self.visitChildren(ctx)



del ViperLangParser