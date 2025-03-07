Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRuleForNamedItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : EvaluateRuleForNamedItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_qualifiedName_
    The fully qualified name of the item for which to evaluate the rule, e.g. "DWVariable1".

_ruleFormula_
    The formula which defines the rule.

Glossary Item Box

Evaluates the result of the specified rule formula as if it had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EvaluateRuleForNamedItem( _
       ByVal _qualifiedName_ As String, _
       ByVal _ruleFormula_ As String _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim qualifiedName As String
    Dim ruleFormula As String
    Dim value As Object
     
    value = instance.EvaluateRuleForNamedItem(qualifiedName, ruleFormula)  
  
C#|   
---|---  
      
    
    public object EvaluateRuleForNamedItem( 
       string _qualifiedName_ ,
       string _ruleFormula_
    )  
  
#### Parameters

 _qualifiedName_
    The fully qualified name of the item for which to evaluate the rule, e.g. "DWVariable1".
_ruleFormula_
    The formula which defines the rule.

#### Return Value

The result of executing the rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


