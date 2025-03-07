Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetResult Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [RuleResults Class](topic11136.md) : GetResult Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleId_
    The identifier of the rule for which to retrieve the result.

Glossary Item Box

Gets the result for the rule with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetResult( _
       ByVal _ruleId_ As String _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RuleResults](topic11136.md)
    Dim ruleId As String
    Dim value As Object
     
    value = instance.GetResult(ruleId)  
  
C#|   
---|---  
      
    
    public object GetResult( 
       string _ruleId_
    )  
  
#### Parameters

 _ruleId_
    The identifier of the rule for which to retrieve the result.

#### Return Value

The result of the calculated rule.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| Thrown if the specified rule identifier does not correspond to a value in the result set.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RuleResults Class](topic11136.md)   
[RuleResults Members](topic11137.md)


