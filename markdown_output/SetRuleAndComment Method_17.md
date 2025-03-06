SetRuleAndComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IHasRule Interface](topic5947.md) : SetRuleAndComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newRule_
    The new rule.

_newComment_
    The new comment.

Glossary Item Box

Sets the rule and comment in a single operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasRule](topic5947.md)
    Dim newRule As String
    Dim newComment As String
     
    instance.SetRuleAndComment(newRule, newComment)  
  
C#|   
---|---  
      
    
    void SetRuleAndComment( 
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _newRule_
    The new rule.
_newComment_
    The new comment.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The rule is not writable.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasRule Interface](topic5947.md)   
[IHasRule Members](topic5948.md)


