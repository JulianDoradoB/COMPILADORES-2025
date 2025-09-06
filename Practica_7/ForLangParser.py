# Generated from ForLang.g4 by ANTLR 4.13.2
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
        4,1,15,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,36,8,3,11,3,12,3,37,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,69,9,4,1,
        4,0,1,8,5,0,2,4,6,8,0,0,75,0,11,1,0,0,0,2,19,1,0,0,0,4,21,1,0,0,
        0,6,26,1,0,0,0,8,48,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,
        0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,
        1,1,0,0,0,17,20,3,4,2,0,18,20,3,6,3,0,19,17,1,0,0,0,19,18,1,0,0,
        0,20,3,1,0,0,0,21,22,5,13,0,0,22,23,5,1,0,0,23,24,3,8,4,0,24,25,
        5,2,0,0,25,5,1,0,0,0,26,27,5,3,0,0,27,28,5,4,0,0,28,29,3,4,2,0,29,
        30,3,8,4,0,30,31,5,2,0,0,31,32,3,4,2,0,32,33,5,5,0,0,33,35,5,6,0,
        0,34,36,3,2,1,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,39,1,0,0,0,39,40,5,7,0,0,40,7,1,0,0,0,41,42,6,4,-1,0,
        42,49,5,14,0,0,43,49,5,13,0,0,44,45,5,4,0,0,45,46,3,8,4,0,46,47,
        5,5,0,0,47,49,1,0,0,0,48,41,1,0,0,0,48,43,1,0,0,0,48,44,1,0,0,0,
        49,67,1,0,0,0,50,51,10,6,0,0,51,52,5,8,0,0,52,66,3,8,4,7,53,54,10,
        5,0,0,54,55,5,9,0,0,55,66,3,8,4,6,56,57,10,4,0,0,57,58,5,10,0,0,
        58,66,3,8,4,5,59,60,10,3,0,0,60,61,5,11,0,0,61,66,3,8,4,4,62,63,
        10,1,0,0,63,64,5,12,0,0,64,66,3,8,4,2,65,50,1,0,0,0,65,53,1,0,0,
        0,65,56,1,0,0,0,65,59,1,0,0,0,65,62,1,0,0,0,66,69,1,0,0,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,9,1,0,0,0,69,67,1,0,0,0,6,13,19,37,48,65,
        67
    ]

class ForLangParser ( Parser ):

    grammarFileName = "ForLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'for'", "'('", "')'", "'{'", 
                     "'}'", "'+'", "'-'", "'*'", "'/'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignStat = 2
    RULE_forStat = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "stat", "assignStat", "forStat", "expr" ]

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
    ID=13
    INT=14
    WS=15

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
            return self.getToken(ForLangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.StatContext)
            else:
                return self.getTypedRuleContext(ForLangParser.StatContext,i)


        def getRuleIndex(self):
            return ForLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ForLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==13):
                    break

            self.state = 15
            self.match(ForLangParser.EOF)
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
            return ForLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStatAltContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forStat(self):
            return self.getTypedRuleContext(ForLangParser.ForStatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatAlt" ):
                listener.enterForStatAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatAlt" ):
                listener.exitForStatAlt(self)


    class AssignStatAltContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignStat(self):
            return self.getTypedRuleContext(ForLangParser.AssignStatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatAlt" ):
                listener.enterAssignStatAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatAlt" ):
                listener.exitAssignStatAlt(self)



    def stat(self):

        localctx = ForLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = ForLangParser.AssignStatAltContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assignStat()
                pass
            elif token in [3]:
                localctx = ForLangParser.ForStatAltContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.forStat()
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
            return self.getToken(ForLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ForLangParser.ExprContext,0)


        def getRuleIndex(self):
            return ForLangParser.RULE_assignStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)




    def assignStat(self):

        localctx = ForLangParser.AssignStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(ForLangParser.ID)
            self.state = 22
            self.match(ForLangParser.T__0)
            self.state = 23
            self.expr(0)
            self.state = 24
            self.match(ForLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.AssignStatContext)
            else:
                return self.getTypedRuleContext(ForLangParser.AssignStatContext,i)


        def expr(self):
            return self.getTypedRuleContext(ForLangParser.ExprContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.StatContext)
            else:
                return self.getTypedRuleContext(ForLangParser.StatContext,i)


        def getRuleIndex(self):
            return ForLangParser.RULE_forStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStat" ):
                listener.enterForStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStat" ):
                listener.exitForStat(self)




    def forStat(self):

        localctx = ForLangParser.ForStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_forStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ForLangParser.T__2)
            self.state = 27
            self.match(ForLangParser.T__3)
            self.state = 28
            self.assignStat()
            self.state = 29
            self.expr(0)
            self.state = 30
            self.match(ForLangParser.T__1)
            self.state = 31
            self.assignStat()
            self.state = 32
            self.match(ForLangParser.T__4)
            self.state = 33
            self.match(ForLangParser.T__5)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.stat()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==13):
                    break

            self.state = 39
            self.match(ForLangParser.T__6)
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
            return ForLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ForLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)


    class LtExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtExpr" ):
                listener.enterLtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtExpr" ):
                listener.exitLtExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ForLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ForLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ForLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = ForLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(ForLangParser.INT)
                pass
            elif token in [13]:
                localctx = ForLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(ForLangParser.ID)
                pass
            elif token in [4]:
                localctx = ForLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(ForLangParser.T__3)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(ForLangParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ForLangParser.AddExprContext(self, ForLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 51
                        self.match(ForLangParser.T__7)
                        self.state = 52
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ForLangParser.SubExprContext(self, ForLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 54
                        self.match(ForLangParser.T__8)
                        self.state = 55
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ForLangParser.MulExprContext(self, ForLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 57
                        self.match(ForLangParser.T__9)
                        self.state = 58
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ForLangParser.DivExprContext(self, ForLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 60
                        self.match(ForLangParser.T__10)
                        self.state = 61
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ForLangParser.LtExprContext(self, ForLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 63
                        self.match(ForLangParser.T__11)
                        self.state = 64
                        self.expr(2)
                        pass

             
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




