Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeInitialState Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeInitialState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The new state to set as the intitial state.

Glossary Item Box

Creates a transaction which, when committed, will Change the intitial state of the specification flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeInitialState( _
       ByVal _state_ As [State](topic11559.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim state As [State](topic11559.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeInitialState(state)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeInitialState( 
       [State](topic11559.md) _state_
    )  
  
#### Parameters

 _state_
    The new state to set as the intitial state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


