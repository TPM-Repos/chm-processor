Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetElementAsBoolean Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ITableValue Interface](topic2331.md) : GetElementAsBoolean Method  
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

Gets the element at the given row and column index as a boolean, converting using Titan's data conversion rules if necessary. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetElementAsBoolean( _
       ByVal _ci_ As CultureInfo, _
       ByVal _rowIndex_ As Integer, _
       ByVal _columnIndex_ As Integer _
    ) As Nullable(Of Boolean)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITableValue](topic2331.md)
    Dim ci As CultureInfo
    Dim rowIndex As Integer
    Dim columnIndex As Integer
    Dim value As Nullable(Of Boolean)
     
    value = instance.GetElementAsBoolean(ci, rowIndex, columnIndex)  
  
C#|   
---|---  
      
    
    Nullable<bool> GetElementAsBoolean( 
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITableValue Interface](topic2331.md)   
[ITableValue Members](topic2332.md)


