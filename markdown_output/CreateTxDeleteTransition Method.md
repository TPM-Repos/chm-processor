Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteTransition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The transition to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete the transition by name from given state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteTransition( _
       ByVal _transition_ As [Transition](topic11757.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim transition As [Transition](topic11757.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteTransition(transition)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteTransition( 
       [Transition](topic11757.md) _transition_
    )  
  
#### Parameters

 _transition_
    The transition to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


