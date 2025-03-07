Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFullCellReferenceName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumn Class](topic3946.md) : GetFullCellReferenceName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to use.

_columnName_
    The column name to use.

_rowIndex_
    The cell row index.

Glossary Item Box

Gets a full rule reference name (including the table name) to the specified cell. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetFullCellReferenceName( _
       ByVal _tableName_ As String, _
       ByVal _columnName_ As String, _
       ByVal _rowIndex_ As Integer _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim tableName As String
    Dim columnName As String
    Dim rowIndex As Integer
    Dim value As String
     
    value = [ProjectCalculationTableColumn](topic3946.md).GetFullCellReferenceName(tableName, columnName, rowIndex)  
  
C#|   
---|---  
      
    
    public static string GetFullCellReferenceName( 
       string _tableName_ ,
       string _columnName_ ,
       int _rowIndex_
    )  
  
#### Parameters

 _tableName_
    The name of the table to use.
_columnName_
    The column name to use.
_rowIndex_
    The cell row index.

#### Return Value

The generated name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[ProjectCalculationTableColumn Members](topic3947.md)


