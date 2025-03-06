![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransactionEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1115.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [TransactionEventArgs Class](topic1109.md) : TransactionEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transactionType_
    The type of the transaction that was committed.

_view_
    The view responsible for the transaction.

_isRegistering_
    Whether or not this transaction is a registering transaction, see [IsRegistering](topic1116.md).

Glossary Item Box

Initializes a new instance of the [TransactionEventArgs](topic1109.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _transactionType_ As Type, _
       ByVal _view_ As [IView](topic534.md), _
       ByVal _isRegistering_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim transactionType As Type
    Dim view As [IView](topic534.md)
    Dim isRegistering As Boolean
     
    Dim instance As New [TransactionEventArgs](topic1109.md)(transactionType, view, isRegistering)  
  
C#|   
---|---  
      
    
    public TransactionEventArgs( 
       Type _transactionType_ ,
       [IView](topic534.md) _view_ ,
       bool _isRegistering_
    )  
  
#### Parameters

 _transactionType_
    The type of the transaction that was committed.
_view_
    The view responsible for the transaction.
_isRegistering_
    Whether or not this transaction is a registering transaction, see [IsRegistering](topic1116.md).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TransactionEventArgs Class](topic1109.md)   
[TransactionEventArgs Members](topic1110.md)

©2024 DriveWorks Ltd. All Rights Reserved.
