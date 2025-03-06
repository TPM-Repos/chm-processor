       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransactionRolledBack Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic518.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ITransactionManager Interface](topic502.md) : TransactionRolledBack Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a transaction is rolled back. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event TransactionRolledBack As [TransactionEventHandler](topic1272.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITransactionManager](topic502.md)
    Dim handler As [TransactionEventHandler](topic1272.md)
     
    AddHandler instance.TransactionRolledBack, handler  
  
C#|   
---|---  
      
    
    event [TransactionEventHandler](topic1272.md) TransactionRolledBack  
  
# Event Data

The event handler receives an argument of type [TransactionEventArgs](topic1109.md) containing data related to this event. The following **TransactionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[IsRegistering](topic1116.md)| Gets whether this transaction is being registered for the first time. As apposed to being run through undo or redo.   
[TransactionType](topic1117.md)| Gets the type of the transaction that was committed.   
[View](topic1118.md)| Gets the view responsible for the transaction.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)

©2024 DriveWorks Ltd. All Rights Reserved.
