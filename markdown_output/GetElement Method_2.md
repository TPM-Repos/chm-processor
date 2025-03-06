![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetElement Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2336.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ITableValue Interface](topic2331.md) : GetElement Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rowIndex_
    The row index of the element to get.

_columnIndex_
    The column index of the element to get.

Glossary Item Box

Gets the element at the given row and column index. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetElement( _
       ByVal _rowIndex_ As Integer, _
       ByVal _columnIndex_ As Integer _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ITableValue](topic2331.md)
    Dim rowIndex As Integer
    Dim columnIndex As Integer
    Dim value As Object
     
    value = instance.GetElement(rowIndex, columnIndex)  
  
C#|   
---|---  
      
    
    object GetElement( 
       int _rowIndex_ ,
       int _columnIndex_
    )  
  
#### Parameters

 _rowIndex_
    The row index of the element to get.
_columnIndex_
    The column index of the element to get.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ITableValue Interface](topic2331.md)   
[ITableValue Members](topic2332.md)

©2024 DriveWorks Ltd. All Rights Reserved.
