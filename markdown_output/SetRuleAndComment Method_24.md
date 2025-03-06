SetRuleAndComment Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : SetRuleAndComment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newRule_
    The new rule to set.

_newComment_
    The new comment to set.

Glossary Item Box

Sets the rule and comment in a single operation and updates the version history. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub SetRuleAndComment( _
       ByVal _newRule_ As String, _
       ByVal _newComment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim newRule As String
    Dim newComment As String
     
    instance.SetRuleAndComment(newRule, newComment)  
  
C#|   
---|---  
      
    
    public override void SetRuleAndComment( 
       string _newRule_ ,
       string _newComment_
    )  
  
#### Parameters

 _newRule_
    The new rule to set.
_newComment_
    The new comment to set.

# Remarks

The version history will not be updated if neither the rule nor the comment has changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)


