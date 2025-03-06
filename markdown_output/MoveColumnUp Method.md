![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MoveColumnUp Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Columns Class](topic2516.md) : MoveColumnUp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnToMove_
    The Column to move.

Glossary Item Box

Moves the column to a position before its preceding sibling. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MoveColumnUp( _
       ByVal _columnToMove_ As [Column](topic2506.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Columns](topic2516.md)
    Dim columnToMove As [Column](topic2506.md)
     
    instance.MoveColumnUp(columnToMove)  
  
C#|   
---|---  
      
    
    public void MoveColumnUp( 
       [Column](topic2506.md) _columnToMove_
    )  
  
#### Parameters

 _columnToMove_
    The Column to move.

# ![](dotnetimages/collapse.gif)Remarks

If this column is the first column in the column set, this method does nothing.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Columns Class](topic2516.md)   
[Columns Members](topic2517.md)


