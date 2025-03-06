![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRows Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3126.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTable Class](topic3110.md) : SetRows Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dataToWrite_
    The data used to update the table.

_controlColumnNames_
    The name of the control columns used to identify which rows to update.

Glossary Item Box

Updates rows of this table with the specified data based on control column names. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetRows( _
       ByVal _dataToWrite_(,) As String, _
       ByVal _controlColumnNames_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTable](topic3110.md)
    Dim dataToWrite() As String
    Dim controlColumnNames As String
     
    instance.SetRows(dataToWrite, controlColumnNames)  
  
C#|   
---|---  
      
    
    public void SetRows( 
       string[,] _dataToWrite_ ,
       string _controlColumnNames_
    )  
  
#### Parameters

 _dataToWrite_
    The data used to update the table.
_controlColumnNames_
    The name of the control columns used to identify which rows to update.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupDataTable Class](topic3110.md)   
[GroupDataTable Members](topic3111.md)

©2024 DriveWorks Ltd. All Rights Reserved.
