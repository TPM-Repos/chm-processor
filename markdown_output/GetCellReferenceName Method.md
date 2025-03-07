Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCellReferenceName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : GetCellReferenceName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    The name of the column.

_rowIndex_
    The row index of the cell - zero based.

Glossary Item Box

Converts a column display name to a rule reference name that can be used within a table only. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetCellReferenceName( _
       ByVal _columnName_ As String, _
       ByVal _rowIndex_ As Integer _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim columnName As String
    Dim rowIndex As Integer
    Dim value As String
     
    value = [ProjectCalculationTableColumn](topic3946.md).GetCellReferenceName(columnName, rowIndex)  
  
C#|   
---|---  
      
    
    public static string GetCellReferenceName( 
       string _columnName_ ,
       int _rowIndex_
    )  
  
#### Parameters

 _columnName_
    The name of the column.
_rowIndex_
    The row index of the cell - zero based.

#### Return Value

The generated name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)


