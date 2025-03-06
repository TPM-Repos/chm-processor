![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetElementAsDateTime Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2338.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ITableValue Interface](topic2331.md) : GetElementAsDateTime Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ci_
    The culture information to use for conversions.

_rowIndex_
    The row index of the element to get.

_columnIndex_
    The column index of the element to get.

Glossary Item Box

Gets the element at the given row and column index as a date-time, converting using Titan's data conversion rules if necessary. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetElementAsDateTime( _
       ByVal _ci_ As CultureInfo, _
       ByVal _rowIndex_ As Integer, _
       ByVal _columnIndex_ As Integer _
    ) As Nullable(Of Date)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ITableValue](topic2331.md)
    Dim ci As CultureInfo
    Dim rowIndex As Integer
    Dim columnIndex As Integer
    Dim value As Nullable(Of Date)
     
    value = instance.GetElementAsDateTime(ci, rowIndex, columnIndex)  
  
C#|   
---|---  
      
    
    Nullable<DateTime> GetElementAsDateTime( 
       CultureInfo _ci_ ,
       int _rowIndex_ ,
       int _columnIndex_
    )  
  
#### Parameters

 _ci_
    The culture information to use for conversions.
_rowIndex_
    The row index of the element to get.
_columnIndex_
    The column index of the element to get.

#### Return Value

The value, converted value, or a null reference if conversion fails.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ITableValue Interface](topic2331.md)   
[ITableValue Members](topic2332.md)

©2024 DriveWorks Ltd. All Rights Reserved.
