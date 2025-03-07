Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeOperationName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeOperationName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The operation to rename.

_newName_
    The new name to give the operation.

Glossary Item Box

Creates a transaction which, when committed, will rename an operation with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeOperationName( _
       ByVal _operation_ As [Operation](topic11068.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim operation As [Operation](topic11068.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeOperationName(operation, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeOperationName( 
       [Operation](topic11068.md) _operation_ ,
       string _newName_
    )  
  
#### Parameters

 _operation_
    The operation to rename.
_newName_
    The new name to give the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


