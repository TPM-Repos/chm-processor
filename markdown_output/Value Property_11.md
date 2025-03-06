Value Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : Value Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnIndex_
    Zero based column index of the cell to get the value of.

_rowIndex_
    Zero based row index of the cell to get the value of.

Glossary Item Box

Gets a cell's value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Value( _
       ByVal _columnIndex_ As Integer, _
       ByVal _rowIndex_ As Integer _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTable](topic3926.md)
    Dim columnIndex As Integer
    Dim rowIndex As Integer
    Dim value As Object
     
    value = instance.Value(columnIndex, rowIndex)  
  
C#|   
---|---  
      
    
    public object this[ 
       int _columnIndex_ ,
       int _rowIndex_
    ]; {get;}  
  
#### Parameters

 _columnIndex_
    Zero based column index of the cell to get the value of.
_rowIndex_
    Zero based row index of the cell to get the value of.

# Remarks

Includes header row.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


