Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Move Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskCollection Class](topic6466.md) : Move Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldIndex_
    The index of the task to move.

_newIndex_
    The new index of the task.

Glossary Item Box

Moves the task at oldIndex to newIndex. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Move( _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskCollection](topic6466.md)
    Dim oldIndex As Integer
    Dim newIndex As Integer
     
    instance.Move(oldIndex, newIndex)  
  
C#|   
---|---  
      
    
    public void Move( 
       int _oldIndex_ ,
       int _newIndex_
    )  
  
#### Parameters

 _oldIndex_
    The index of the task to move.
_newIndex_
    The new index of the task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskCollection Class](topic6466.md)   
[ComponentTaskCollection Members](topic6467.md)


