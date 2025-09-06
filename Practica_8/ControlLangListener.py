# Generated from ControlLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ControlLangParser import ControlLangParser
else:
    from ControlLangParser import ControlLangParser

# This class defines a complete listener for a parse tree produced by ControlLangParser.
class ControlLangListener(ParseTreeListener):

    # Enter a parse tree produced by ControlLangParser#prog.
    def enterProg(self, ctx:ControlLangParser.ProgContext):
        pass

    # Exit a parse tree produced by ControlLangParser#prog.
    def exitProg(self, ctx:ControlLangParser.ProgContext):
        pass


    # Enter a parse tree produced by ControlLangParser#AssignStatAlt.
    def enterAssignStatAlt(self, ctx:ControlLangParser.AssignStatAltContext):
        pass

    # Exit a parse tree produced by ControlLangParser#AssignStatAlt.
    def exitAssignStatAlt(self, ctx:ControlLangParser.AssignStatAltContext):
        pass


    # Enter a parse tree produced by ControlLangParser#ForStatAlt.
    def enterForStatAlt(self, ctx:ControlLangParser.ForStatAltContext):
        pass

    # Exit a parse tree produced by ControlLangParser#ForStatAlt.
    def exitForStatAlt(self, ctx:ControlLangParser.ForStatAltContext):
        pass


    # Enter a parse tree produced by ControlLangParser#SwitchStatAlt.
    def enterSwitchStatAlt(self, ctx:ControlLangParser.SwitchStatAltContext):
        pass

    # Exit a parse tree produced by ControlLangParser#SwitchStatAlt.
    def exitSwitchStatAlt(self, ctx:ControlLangParser.SwitchStatAltContext):
        pass


    # Enter a parse tree produced by ControlLangParser#IfStatAlt.
    def enterIfStatAlt(self, ctx:ControlLangParser.IfStatAltContext):
        pass

    # Exit a parse tree produced by ControlLangParser#IfStatAlt.
    def exitIfStatAlt(self, ctx:ControlLangParser.IfStatAltContext):
        pass


    # Enter a parse tree produced by ControlLangParser#assignStat.
    def enterAssignStat(self, ctx:ControlLangParser.AssignStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#assignStat.
    def exitAssignStat(self, ctx:ControlLangParser.AssignStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#forStat.
    def enterForStat(self, ctx:ControlLangParser.ForStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#forStat.
    def exitForStat(self, ctx:ControlLangParser.ForStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#switchStat.
    def enterSwitchStat(self, ctx:ControlLangParser.SwitchStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#switchStat.
    def exitSwitchStat(self, ctx:ControlLangParser.SwitchStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#caseStat.
    def enterCaseStat(self, ctx:ControlLangParser.CaseStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#caseStat.
    def exitCaseStat(self, ctx:ControlLangParser.CaseStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#defaultStat.
    def enterDefaultStat(self, ctx:ControlLangParser.DefaultStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#defaultStat.
    def exitDefaultStat(self, ctx:ControlLangParser.DefaultStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#ifStat.
    def enterIfStat(self, ctx:ControlLangParser.IfStatContext):
        pass

    # Exit a parse tree produced by ControlLangParser#ifStat.
    def exitIfStat(self, ctx:ControlLangParser.IfStatContext):
        pass


    # Enter a parse tree produced by ControlLangParser#block.
    def enterBlock(self, ctx:ControlLangParser.BlockContext):
        pass

    # Exit a parse tree produced by ControlLangParser#block.
    def exitBlock(self, ctx:ControlLangParser.BlockContext):
        pass


    # Enter a parse tree produced by ControlLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:ControlLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:ControlLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ControlLangParser#IdExpr.
    def enterIdExpr(self, ctx:ControlLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#IdExpr.
    def exitIdExpr(self, ctx:ControlLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by ControlLangParser#RelExpr.
    def enterRelExpr(self, ctx:ControlLangParser.RelExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#RelExpr.
    def exitRelExpr(self, ctx:ControlLangParser.RelExprContext):
        pass


    # Enter a parse tree produced by ControlLangParser#IntExpr.
    def enterIntExpr(self, ctx:ControlLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#IntExpr.
    def exitIntExpr(self, ctx:ControlLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by ControlLangParser#ParenExpr.
    def enterParenExpr(self, ctx:ControlLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#ParenExpr.
    def exitParenExpr(self, ctx:ControlLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ControlLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:ControlLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ControlLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:ControlLangParser.AddSubExprContext):
        pass



del ControlLangParser