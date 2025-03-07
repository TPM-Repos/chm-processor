Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeDataTableName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeDataTableName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dataTable_
    The data table that will have its name changed.

_newName_
    The new name to give the data table.

Glossary Item Box

Creates a transaction which, when committed, will rename a transaction with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeDataTableName( _
       ByVal _dataTable_ As [ProjectDataTable](topic4282.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim dataTable As [ProjectDataTable](topic4282.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeDataTableName(dataTable, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeDataTableName( 
       [ProjectDataTable](topic4282.md) _dataTable_ ,
       string _newName_
    )  
  
#### Parameters

 _dataTable_
    The data table that will have its name changed.
_newName_
    The new name to give the data table.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


