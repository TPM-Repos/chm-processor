Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Move Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Conditions Class](topic10865.md) : Move Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_oldIndex_
    The old index of the condition.

_newIndex_
    The new index of the condition.

Glossary Item Box

Move the condition from its current index to the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Move( _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Conditions](topic10865.md)
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
    The old index of the condition.
_newIndex_
    The new index of the condition.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Conditions Class](topic10865.md)   
[Conditions Members](topic10866.md)


