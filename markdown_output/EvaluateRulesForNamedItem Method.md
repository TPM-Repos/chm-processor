![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRulesForNamedItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : EvaluateRulesForNamedItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_qualifiedName_
    The fully qualified name of the item for which to evaluate the rules, e.g. "DWVariable1".

_ruleFormulae_
    The formulae which define the rules.

Glossary Item Box

Evaluates the result of the specified rule formulae as if they had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EvaluateRulesForNamedItem( _
       ByVal _qualifiedName_ As String, _
       ByVal _ruleFormulae_() As String _
    ) As Object()  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim qualifiedName As String
    Dim ruleFormulae() As String
    Dim value() As Object
     
    value = instance.EvaluateRulesForNamedItem(qualifiedName, ruleFormulae)  
  
C#|   
---|---  
      
    
    public object[] EvaluateRulesForNamedItem( 
       string _qualifiedName_ ,
       string[] _ruleFormulae_
    )  
  
#### Parameters

 _qualifiedName_
    The fully qualified name of the item for which to evaluate the rules, e.g. "DWVariable1".
_ruleFormulae_
    The formulae which define the rules.

#### Return Value

The result of executing the rules.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


