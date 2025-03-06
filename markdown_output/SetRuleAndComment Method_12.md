SetRuleAndComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessage Class](topic4601.md) : SetRuleAndComment Method  
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
      
    
    Public MustOverride Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessage](topic4601.md)
    Dim newRule As String
    Dim newComment As String
     
    instance.SetRuleAndComment(newRule, newComment)  
  
C#|   
---|---  
      
    
    public abstract void SetRuleAndComment( 
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _newRule_
    The new rule.
_newComment_
    The new comment.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessage Class](topic4601.md)   
[ProjectMessage Members](topic4602.md)


