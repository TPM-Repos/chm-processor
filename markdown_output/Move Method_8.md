Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Move Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) : Move Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldIndex_
    The old index of the control.

_newIndex_
    The new index of the control.

Glossary Item Box

Move a control from its current index to the specified index, to adjust it's z-index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Move( _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
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
    The old index of the control.
_newIndex_
    The new index of the control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)


