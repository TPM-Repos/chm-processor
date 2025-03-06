![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetChosenColumns Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5251.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RollupDataTable Class](topic5240.md) : SetChosenColumns Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnNames_
    The chosen column names.

Glossary Item Box

Sets the names of the columns that data will be retrieved for in any child specifications. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetChosenColumns( _
       ByVal _columnNames_() As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RollupDataTable](topic5240.md)
    Dim columnNames() As String
     
    instance.SetChosenColumns(columnNames)  
  
C#|   
---|---  
      
    
    public void SetChosenColumns( 
       string[] _columnNames_
    )  
  
#### Parameters

 _columnNames_
    The chosen column names.

# ![](dotnetimages/collapse.gif)Remarks

This will also update the placeholder data accordingly.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RollupDataTable Class](topic5240.md)   
[RollupDataTable Members](topic5241.md)

©2024 DriveWorks Ltd. All Rights Reserved.
