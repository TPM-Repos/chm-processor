![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub HistoricalTransactionFinished( _
       ByVal _transactionType_ As Type _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Remarks

Only called for Undo and Redo transactions.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)


