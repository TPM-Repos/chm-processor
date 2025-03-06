TryGetResult Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) : TryGetResult Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The identifier of the rule for which to retrieve the result.

_result_
    A reference to a variable which will receive the result of the rule.

Glossary Item Box

Tries getting the result for the rule with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetResult( _
       ByVal _ruleId_ As String, _
       ByRef _result_ As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleResults](topic11136.md)
    Dim ruleId As String
    Dim result As Object
    Dim value As Boolean
     
    value = instance.TryGetResult(ruleId, result)  
  
C#|   
---|---  
      
    
    public bool TryGetResult( 
       string _ruleId_ ,
       ref object _result_
    )  
  
#### Parameters

 _ruleId_
    The identifier of the rule for which to retrieve the result.
_result_
    A reference to a variable which will receive the result of the rule.

#### Return Value

True if a value was found for the specified rule, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)


