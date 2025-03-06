![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5588.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportColumns Class](topic5579.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_column_
    The column to remove.

Glossary Item Box

Removes the specified column from this collection of columns. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _column_ As [TableExportColumn](topic5568.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TableExportColumns](topic5579.md)
    Dim column As [TableExportColumn](topic5568.md)
    Dim value As Boolean
     
    value = instance.Remove(column)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [TableExportColumn](topic5568.md) _column_
    )  
  
#### Parameters

 _column_
    The column to remove.

#### Return Value

True if the column was removed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TableExportColumns Class](topic5579.md)   
[TableExportColumns Members](topic5580.md)

©2024 DriveWorks Ltd. All Rights Reserved.
