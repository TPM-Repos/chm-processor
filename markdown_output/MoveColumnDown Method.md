Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MoveColumnDown Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Columns Class](topic2516.md) : MoveColumnDown Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnToMove_
    The Column to move.

Glossary Item Box

Moves the column to a position after its following sibling. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MoveColumnDown( _
       ByVal _columnToMove_ As [Column](topic2506.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Columns](topic2516.md)
    Dim columnToMove As [Column](topic2506.md)
     
    instance.MoveColumnDown(columnToMove)  
  
C#|   
---|---  
      
    
    public void MoveColumnDown( 
       [Column](topic2506.md) _columnToMove_
    )  
  
#### Parameters

 _columnToMove_
    The Column to move.

# Remarks

If this column is the last column in the column set, this method does nothing.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Columns Class](topic2516.md)   
[Columns Members](topic2517.md)


