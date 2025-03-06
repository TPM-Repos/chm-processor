       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TxAggregateTransaction Constructor(ITransaction[])   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13179.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TxAggregateTransaction Class](topic13172.md) > [TxAggregateTransaction Constructor](topic13178.md) : TxAggregateTransaction Constructor(ITransaction[])  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transactions_
    The transactions to aggregate into a single transaction.

Glossary Item Box

Initializes a new instance of the [TxAggregateTransaction](topic13172.md) transaction class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _transactions_() As [ITransaction](topic12837.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim transactions() As [ITransaction](topic12837.md)
     
    Dim instance As New [TxAggregateTransaction](topic13172.md)(transactions)  
  
C#|   
---|---  
      
    
    public TxAggregateTransaction( 
       [ITransaction](topic12837.md)[] _transactions_
    )  
  
#### Parameters

 _transactions_
    The transactions to aggregate into a single transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TxAggregateTransaction Class](topic13172.md)   
[TxAggregateTransaction Members](topic13173.md)   
[Overload List](topic13178.md)

©2024 DriveWorks Ltd. All Rights Reserved.
