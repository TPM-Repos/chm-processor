Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Move Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) : Move Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnIndex_
    The index of the column to move.

_newIndex_
    The new index to give the column.

Glossary Item Box

Moves a column from an index to the specified new index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Move( _
       ByVal _columnIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim columnIndex As Integer
    Dim newIndex As Integer
     
    instance.Move(columnIndex, newIndex)  
  
C#|   
---|---  
      
    
    public void Move( 
       int _columnIndex_ ,
       int _newIndex_
    )  
  
#### Parameters

 _columnIndex_
    The index of the column to move.
_newIndex_
    The new index to give the column.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)


