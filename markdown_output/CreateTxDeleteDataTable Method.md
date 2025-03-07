Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteDataTable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteDataTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dataTable_
    The data table to be deleted.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified data table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteDataTable( _
       ByVal _dataTable_ As [ProjectDataTable](topic4282.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim dataTable As [ProjectDataTable](topic4282.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteDataTable(dataTable)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteDataTable( 
       [ProjectDataTable](topic4282.md) _dataTable_
    )  
  
#### Parameters

 _dataTable_
    The data table to be deleted.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


