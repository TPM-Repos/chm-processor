Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRule(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) > [EvaluateRule Method](topic3869.md) : EvaluateRule(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleFormula_
    The formula which defines the rule.

Glossary Item Box

Evaluates the result of the specified rule formula. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function EvaluateRule( _
       ByVal _ruleFormula_ As String _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim ruleFormula As String
    Dim value As Object
     
    value = instance.EvaluateRule(ruleFormula)  
  
C#|   
---|---  
      
    
    public object EvaluateRule( 
       string _ruleFormula_
    )  
  
#### Parameters

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
[Overload List](topic3869.md)


