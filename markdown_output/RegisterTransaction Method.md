![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterTransaction Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic510.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub RegisterTransaction( _
       ByVal _transaction_ As [ITransaction](topic12837.md), _
       ByVal _requiresCommit_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)

©2024 DriveWorks Ltd. All Rights Reserved.
