Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRule(ProjectDocumentRule) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [EvaluateRule Method](topic4370.md) : EvaluateRule(ProjectDocumentRule) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to evaluate.

Glossary Item Box

Evaluates the specified rule into a displayable string. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overloads Function EvaluateRule( _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
    Dim value As String
     
    value = instance.EvaluateRule(rule)  
  
C#|   
---|---  
      
    
    protected string EvaluateRule( 
       [ProjectDocumentRule](topic4399.md) _rule_
    )  
  
#### Parameters

 _rule_
    The rule to evaluate.

#### Return Value

The result of the evaluated rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4370.md)


