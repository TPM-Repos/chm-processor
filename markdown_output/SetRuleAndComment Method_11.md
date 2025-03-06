SetRuleAndComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocumentRule Class](topic4399.md) : SetRuleAndComment Method  
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
      
    
    Public Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocumentRule](topic4399.md)
    Dim newRule As String
    Dim newComment As String
     
    instance.SetRuleAndComment(newRule, newComment)  
  
C#|   
---|---  
      
    
    public void SetRuleAndComment( 
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

[ProjectDocumentRule Class](topic4399.md)   
[ProjectDocumentRule Members](topic4400.md)


