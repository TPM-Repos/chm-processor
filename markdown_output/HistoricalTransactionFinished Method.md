Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HistoricalTransactionFinished Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : HistoricalTransactionFinished Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transactionType_
    The type of transaction that is about to be executed.

Glossary Item Box

When overridden by a derived class, performs transaction finished logic specific to the derived view. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub HistoricalTransactionFinished( _
       ByVal _transactionType_ As Type _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim transactionType As Type
     
    instance.HistoricalTransactionFinished(transactionType)  
  
C#|   
---|---  
      
    
    protected virtual void HistoricalTransactionFinished( 
       Type _transactionType_
    )  
  
#### Parameters

 _transactionType_
    The type of transaction that is about to be executed.

# Remarks

Only called for Undo and Redo transactions.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


