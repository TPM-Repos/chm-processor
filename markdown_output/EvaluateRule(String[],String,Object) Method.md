Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateRule(String[],String,Object) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) > [EvaluateRule Method](topic3869.md) : EvaluateRule(String[],String,Object) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleFormulae_
    The formulae which define the rules.

_qualifiedName_
    The fully qualified name of the item for which to evaluate the rules, e.g. "DWVariable1".

_context_
    The context to use when evaluating the rules.

Glossary Item Box

Evaluates the result of the specified rule formulae as if they had been applied to a particular named item. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function EvaluateRule( _
       ByVal _ruleFormulae_() As String, _
       ByVal _qualifiedName_ As String, _
       ByVal _context_ As Object _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim ruleFormulae() As String
    Dim qualifiedName As String
    Dim context As Object
    Dim value As Object
     
    value = instance.EvaluateRule(ruleFormulae, qualifiedName, context)  
  
C#|   
---|---  
      
    
    public object EvaluateRule( 
       string[] _ruleFormulae_ ,
       string _qualifiedName_ ,
       object _context_
    )  
  
#### Parameters

 _ruleFormulae_
    The formulae which define the rules.
_qualifiedName_
    The fully qualified name of the item for which to evaluate the rules, e.g. "DWVariable1".
_context_
    The context to use when evaluating the rules.

#### Return Value

The result of executing the rules.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)   
[Overload List](topic3869.md)


