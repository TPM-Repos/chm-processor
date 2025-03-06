RegisterTransaction Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ITransactionManager Interface](topic502.md) : RegisterTransaction Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transaction_
    The transaction to register.

_requiresCommit_
    True if the commit method on the transaction should be called after the transaction has been registered, if the transaction has already taken place then false should be passed.

Glossary Item Box

Register's a transaction with the transaction manager's undo chain. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RegisterTransaction( _
       ByVal _transaction_ As [ITransaction](topic12837.md), _
       ByVal _requiresCommit_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITransactionManager](topic502.md)
    Dim transaction As [ITransaction](topic12837.md)
    Dim requiresCommit As Boolean
     
    instance.RegisterTransaction(transaction, requiresCommit)  
  
C#|   
---|---  
      
    
    void RegisterTransaction( 
       [ITransaction](topic12837.md) _transaction_ ,
       bool _requiresCommit_
    )  
  
#### Parameters

 _transaction_
    The transaction to register.
_requiresCommit_
    True if the commit method on the transaction should be called after the transaction has been registered, if the transaction has already taken place then false should be passed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)


