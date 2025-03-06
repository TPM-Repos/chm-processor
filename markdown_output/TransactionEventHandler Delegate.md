       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransactionEventHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : TransactionEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    The event data.

Glossary Item Box

The event delegate used for events which have transactional event data, for example [ITransactionManager.TransactionCommitted](topic515.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub TransactionEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [TransactionEventArgs](topic1109.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [TransactionEventHandler](topic1272.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void TransactionEventHandler( 
       object _sender_ ,
       [TransactionEventArgs](topic1109.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TransactionEventHandler Members](topic1272.md)   
[DriveWorks.Applications Namespace](topic16.md)


