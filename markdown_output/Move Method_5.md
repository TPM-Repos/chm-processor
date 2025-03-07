Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Move Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : Move Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldIndex_
    The index of the component set to move.

_newIndex_
    The new index of the component set.

Glossary Item Box

Moves the component set at the given index to the specified new index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Move( _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
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
    The index of the component set to move.
_newIndex_
    The new index of the component set.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)


