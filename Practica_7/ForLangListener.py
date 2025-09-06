# Generated from ForLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ForLangParser import ForLangParser
else:
    from ForLangParser import ForLangParser

# This class defines a complete listener for a parse tree produced by ForLangParser.
class ForLangListener(ParseTreeListener):

    # Enter a parse tree produced by ForLangParser#prog.
    def enterProg(self, ctx:ForLangParser.ProgContext):
        pass

    # Exit a parse tree produced by ForLangParser#prog.
    def exitProg(self, ctx:ForLangParser.ProgContext):
        pass


    # Enter a parse tree produced by ForLangParser#AssignStatAlt.
    def enterAssignStatAlt(self, ctx:ForLangParser.AssignStatAltContext):
        pass

    # Exit a parse tree produced by ForLangParser#AssignStatAlt.
    def exitAssignStatAlt(self, ctx:ForLangParser.AssignStatAltContext):
        pass


    # Enter a parse tree produced by ForLangParser#ForStatAlt.
    def enterForStatAlt(self, ctx:ForLangParser.ForStatAltContext):
        pass

    # Exit a parse tree produced by ForLangParser#ForStatAlt.
    def exitForStatAlt(self, ctx:ForLangParser.ForStatAltContext):
        pass


    # Enter a parse tree produced by ForLangParser#assignStat.
    def enterAssignStat(self, ctx:ForLangParser.AssignStatContext):
        pass

    # Exit a parse tree produced by ForLangParser#assignStat.
    def exitAssignStat(self, ctx:ForLangParser.AssignStatContext):
        pass


    # Enter a parse tree produced by ForLangParser#forStat.
    def enterForStat(self, ctx:ForLangParser.ForStatContext):
        pass

    # Exit a parse tree produced by ForLangParser#forStat.
    def exitForStat(self, ctx:ForLangParser.ForStatContext):
        pass


    # Enter a parse tree produced by ForLangParser#MulExpr.
    def enterMulExpr(self, ctx:ForLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#MulExpr.
    def exitMulExpr(self, ctx:ForLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#DivExpr.
    def enterDivExpr(self, ctx:ForLangParser.DivExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#DivExpr.
    def exitDivExpr(self, ctx:ForLangParser.DivExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#IdExpr.
    def enterIdExpr(self, ctx:ForLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#IdExpr.
    def exitIdExpr(self, ctx:ForLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#SubExpr.
    def enterSubExpr(self, ctx:ForLangParser.SubExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#SubExpr.
    def exitSubExpr(self, ctx:ForLangParser.SubExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#LtExpr.
    def enterLtExpr(self, ctx:ForLangParser.LtExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#LtExpr.
    def exitLtExpr(self, ctx:ForLangParser.LtExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#AddExpr.
    def enterAddExpr(self, ctx:ForLangParser.AddExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#AddExpr.
    def exitAddExpr(self, ctx:ForLangParser.AddExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#IntExpr.
    def enterIntExpr(self, ctx:ForLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#IntExpr.
    def exitIntExpr(self, ctx:ForLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by ForLangParser#ParenExpr.
    def enterParenExpr(self, ctx:ForLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ForLangParser#ParenExpr.
    def exitParenExpr(self, ctx:ForLangParser.ParenExprContext):
        pass



del ForLangParser