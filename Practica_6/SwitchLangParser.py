# Generated from SwitchLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,37,8,3,11,3,12,3,38,1,3,
        3,3,42,8,3,1,3,1,3,1,4,1,4,1,4,1,4,4,4,50,8,4,11,4,12,4,51,1,5,1,
        5,1,5,4,5,57,8,5,11,5,12,5,58,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,82,8,6,10,
        6,12,6,85,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,0,91,0,15,1,0,0,0,2,
        23,1,0,0,0,4,25,1,0,0,0,6,30,1,0,0,0,8,45,1,0,0,0,10,53,1,0,0,0,
        12,67,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,
        0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,
        24,3,4,2,0,22,24,3,6,3,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,
        0,25,26,5,15,0,0,26,27,5,1,0,0,27,28,3,12,6,0,28,29,5,2,0,0,29,5,
        1,0,0,0,30,31,5,3,0,0,31,32,5,4,0,0,32,33,5,15,0,0,33,34,5,5,0,0,
        34,36,5,6,0,0,35,37,3,8,4,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,
        0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,42,3,10,5,0,41,40,1,0,0,0,41,
        42,1,0,0,0,42,43,1,0,0,0,43,44,5,7,0,0,44,7,1,0,0,0,45,46,5,8,0,
        0,46,47,5,16,0,0,47,49,5,9,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,
        1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,54,5,10,0,0,
        54,56,5,9,0,0,55,57,3,2,1,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,
        0,0,0,58,59,1,0,0,0,59,11,1,0,0,0,60,61,6,6,-1,0,61,68,5,16,0,0,
        62,68,5,15,0,0,63,64,5,4,0,0,64,65,3,12,6,0,65,66,5,5,0,0,66,68,
        1,0,0,0,67,60,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,68,83,1,0,0,0,
        69,70,10,5,0,0,70,71,5,11,0,0,71,82,3,12,6,6,72,73,10,4,0,0,73,74,
        5,12,0,0,74,82,3,12,6,5,75,76,10,3,0,0,76,77,5,13,0,0,77,82,3,12,
        6,4,78,79,10,2,0,0,79,80,5,14,0,0,80,82,3,12,6,3,81,69,1,0,0,0,81,
        72,1,0,0,0,81,75,1,0,0,0,81,78,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,
        0,83,84,1,0,0,0,84,13,1,0,0,0,85,83,1,0,0,0,9,17,23,38,41,51,58,
        67,81,83
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'switch'", "'('", "')'", 
                     "'{'", "'}'", "'case'", "':'", "'default'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignStat = 2
    RULE_switchStat = 3
    RULE_caseStat = 4
    RULE_defaultStat = 5
    RULE_expr = 6

    ruleNames =  [ "prog", "stat", "assignStat", "switchStat", "caseStat", 
                   "defaultStat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    INT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SwitchLangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SwitchLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==15):
                    break

            self.state = 19
            self.match(SwitchLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SwitchStatAltContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def switchStat(self):
            return self.getTypedRuleContext(SwitchLangParser.SwitchStatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatAlt" ):
                listener.enterSwitchStatAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatAlt" ):
                listener.exitSwitchStatAlt(self)


    class AssignStatAltContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignStat(self):
            return self.getTypedRuleContext(SwitchLangParser.AssignStatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatAlt" ):
                listener.enterAssignStatAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatAlt" ):
                listener.exitAssignStatAlt(self)



    def stat(self):

        localctx = SwitchLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = SwitchLangParser.AssignStatAltContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assignStat()
                pass
            elif token in [3]:
                localctx = SwitchLangParser.SwitchStatAltContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.switchStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SwitchLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_assignStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)




    def assignStat(self):

        localctx = SwitchLangParser.AssignStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(SwitchLangParser.ID)
            self.state = 26
            self.match(SwitchLangParser.T__0)
            self.state = 27
            self.expr(0)
            self.state = 28
            self.match(SwitchLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)

        def caseStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.CaseStatContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.CaseStatContext,i)


        def defaultStat(self):
            return self.getTypedRuleContext(SwitchLangParser.DefaultStatContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_switchStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStat" ):
                listener.enterSwitchStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStat" ):
                listener.exitSwitchStat(self)




    def switchStat(self):

        localctx = SwitchLangParser.SwitchStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_switchStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(SwitchLangParser.T__2)
            self.state = 31
            self.match(SwitchLangParser.T__3)
            self.state = 32
            self.match(SwitchLangParser.ID)
            self.state = 33
            self.match(SwitchLangParser.T__4)
            self.state = 34
            self.match(SwitchLangParser.T__5)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 35
                self.caseStat()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 40
                self.defaultStat()


            self.state = 43
            self.match(SwitchLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_caseStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStat" ):
                listener.enterCaseStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStat" ):
                listener.exitCaseStat(self)




    def caseStat(self):

        localctx = SwitchLangParser.CaseStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_caseStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SwitchLangParser.T__7)
            self.state = 46
            self.match(SwitchLangParser.INT)
            self.state = 47
            self.match(SwitchLangParser.T__8)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.stat()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.StatContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.StatContext,i)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_defaultStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStat" ):
                listener.enterDefaultStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStat" ):
                listener.exitDefaultStat(self)




    def defaultStat(self):

        localctx = SwitchLangParser.DefaultStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_defaultStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(SwitchLangParser.T__9)
            self.state = 54
            self.match(SwitchLangParser.T__8)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.stat()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SwitchLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SwitchLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = SwitchLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 61
                self.match(SwitchLangParser.INT)
                pass
            elif token in [15]:
                localctx = SwitchLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(SwitchLangParser.ID)
                pass
            elif token in [4]:
                localctx = SwitchLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(SwitchLangParser.T__3)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(SwitchLangParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SwitchLangParser.AddExprContext(self, SwitchLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 70
                        self.match(SwitchLangParser.T__10)
                        self.state = 71
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = SwitchLangParser.SubExprContext(self, SwitchLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        self.match(SwitchLangParser.T__11)
                        self.state = 74
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = SwitchLangParser.MulExprContext(self, SwitchLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        self.match(SwitchLangParser.T__12)
                        self.state = 77
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = SwitchLangParser.DivExprContext(self, SwitchLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        self.match(SwitchLangParser.T__13)
                        self.state = 80
                        self.expr(3)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




