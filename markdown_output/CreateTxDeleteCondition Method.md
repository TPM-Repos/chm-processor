Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionRef_
    The reference to the condition to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete the specified condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteCondition( _
       ByVal _conditionRef_ As [ConditionRef](topic12843.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionRef As [ConditionRef](topic12843.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteCondition(conditionRef)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteCondition( 
       [ConditionRef](topic12843.md) _conditionRef_
    )  
  
#### Parameters

 _conditionRef_
    The reference to the condition to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


