Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeTransitionName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeTransitionName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The transition to rename.

_newName_
    The new name to give the transition.

Glossary Item Box

Creates a transaction which, when committed, will rename an transition with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeTransitionName( _
       ByVal _transition_ As [Transition](topic11757.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim transition As [Transition](topic11757.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeTransitionName(transition, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeTransitionName( 
       [Transition](topic11757.md) _transition_ ,
       string _newName_
    )  
  
#### Parameters

 _transition_
    The transition to rename.
_newName_
    The new name to give the transition.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


