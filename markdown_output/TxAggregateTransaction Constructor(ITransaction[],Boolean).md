![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TxAggregateTransaction Constructor(ITransaction[],Boolean)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13180.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TxAggregateTransaction Class](topic13172.md) > [TxAggregateTransaction Constructor](topic13178.md) : TxAggregateTransaction Constructor(ITransaction[],Boolean)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transactions_
    The transactions to aggregate into a single transaction.

_preserveOrder_
    Determines if the order of the reverse transaction should be kept the same as the forward.

Glossary Item Box

Initializes a new instance of the [TxAggregateTransaction](topic13172.md) transaction class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _transactions_() As [ITransaction](topic12837.md), _
       ByVal _preserveOrder_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim transactions() As [ITransaction](topic12837.md)
    Dim preserveOrder As Boolean
     
    Dim instance As New [TxAggregateTransaction](topic13172.md)(transactions, preserveOrder)  
  
C#|   
---|---  
      
    
    public TxAggregateTransaction( 
       [ITransaction](topic12837.md)[] _transactions_ ,
       bool _preserveOrder_
    )  
  
#### Parameters

 _transactions_
    The transactions to aggregate into a single transaction.
_preserveOrder_
    Determines if the order of the reverse transaction should be kept the same as the forward.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TxAggregateTransaction Class](topic13172.md)   
[TxAggregateTransaction Members](topic13173.md)   
[Overload List](topic13178.md)

©2024 DriveWorks Ltd. All Rights Reserved.
