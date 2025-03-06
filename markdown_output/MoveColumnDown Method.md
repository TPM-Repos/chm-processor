![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MoveColumnDown Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2525.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Columns Class](topic2516.md) : MoveColumnDown Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnToMove_
    The Column to move.

Glossary Item Box

Moves the column to a position after its following sibling. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MoveColumnDown( _
       ByVal _columnToMove_ As [Column](topic2506.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Remarks

If this column is the last column in the column set, this method does nothing.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Columns Class](topic2516.md)   
[Columns Members](topic2517.md)

©2024 DriveWorks Ltd. All Rights Reserved.
