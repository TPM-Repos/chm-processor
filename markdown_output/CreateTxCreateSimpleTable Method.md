Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateSimpleTable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateSimpleTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to be created.

_data_
    The data to populate the table with.

Glossary Item Box

Creates a transaction which, when committed, will create and populate a simple table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateSimpleTable( _
       ByVal _tableName_ As String, _
       ByVal _data_(,) As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim tableName As String
    Dim data() As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateSimpleTable(tableName, data)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateSimpleTable( 
       string _tableName_ ,
       string[,] _data_
    )  
  
#### Parameters

 _tableName_
    The name of the table to be created.
_data_
    The data to populate the table with.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


