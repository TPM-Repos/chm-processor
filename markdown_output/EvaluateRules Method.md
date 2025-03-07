Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRules Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : EvaluateRules Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleFormulae_
    The formulae the rules.

Glossary Item Box

Evaluates the result of the specified rule formulae. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EvaluateRules( _
       ByVal _ruleFormulae_() As String _
    ) As Object()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim ruleFormulae() As String
    Dim value() As Object
     
    value = instance.EvaluateRules(ruleFormulae)  
  
C#|   
---|---  
      
    
    public object[] EvaluateRules( 
       string[] _ruleFormulae_
    )  
  
#### Parameters

 _ruleFormulae_
    The formulae the rules.

#### Return Value

The result of executing the rules.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


