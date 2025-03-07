Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operation_
    The operation to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete an operation by name on a state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteOperation( _
       ByVal _operation_ As [Operation](topic11068.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim operation As [Operation](topic11068.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteOperation(operation)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteOperation( 
       [Operation](topic11068.md) _operation_
    )  
  
#### Parameters

 _operation_
    The operation to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


