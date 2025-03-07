Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxClearCalculationTableColumnRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxClearCalculationTableColumnRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to use.

_columnName_
    The name of the column to use.

_rowIndex_
    The row index of the cell to clear.

Glossary Item Box

Creates a transaction that will clear a calculation table column's cell rule (allowing it to use the column common rule). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxClearCalculationTableColumnRule( _
       ByVal _tableName_ As String, _
       ByVal _columnName_ As String, _
       ByVal _rowIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim tableName As String
    Dim columnName As String
    Dim rowIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxClearCalculationTableColumnRule(tableName, columnName, rowIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxClearCalculationTableColumnRule( 
       string _tableName_ ,
       string _columnName_ ,
       int _rowIndex_
    )  
  
#### Parameters

 _tableName_
    The name of the table to use.
_columnName_
    The name of the column to use.
_rowIndex_
    The row index of the cell to clear.

#### Return Value

A transaction that will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


