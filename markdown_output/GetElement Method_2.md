Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetElement Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetElement( _
       ByVal _rowIndex_ As Integer, _
       ByVal _columnIndex_ As Integer _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITableValue Interface](topic2331.md)   
[ITableValue Members](topic2332.md)


