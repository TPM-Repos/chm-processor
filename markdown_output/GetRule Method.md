![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3958.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : GetRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rowIndex_
    The index of the row to get, where 0 is the first data row.

_create_
    Whether or not to create the cell, if it doesn't exist.

Glossary Item Box

Gets an explicit rule from this column for the specified row. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRule( _
       ByVal _rowIndex_ As Integer, _
       Optional ByVal _create_ As Boolean _
    ) As [ProjectCalculationTableRule](topic3986.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumn](topic3946.md)
    Dim rowIndex As Integer
    Dim create As Boolean
    Dim value As [ProjectCalculationTableRule](topic3986.md)
     
    value = instance.GetRule(rowIndex, create)  
  
C#|   
---|---  
      
    
    public [ProjectCalculationTableRule](topic3986.md) GetRule( 
       int _rowIndex_ ,
       bool _create_
    )  
  
#### Parameters

 _rowIndex_
    The index of the row to get, where 0 is the first data row.
_create_
    Whether or not to create the cell, if it doesn't exist.

#### Return Value

The matching cell item if it exists, or null when create is false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)

©2024 DriveWorks Ltd. All Rights Reserved.
