Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteDecision Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteDecision Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_decision_
    The decision to be deleted.

Glossary Item Box

Creates a transaction which, when committed, will delete a decision by the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteDecision( _
       ByVal _decision_ As [DecisionNavigationStep](topic10125.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim decision As [DecisionNavigationStep](topic10125.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteDecision(decision)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteDecision( 
       [DecisionNavigationStep](topic10125.md) _decision_
    )  
  
#### Parameters

 _decision_
    The decision to be deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


