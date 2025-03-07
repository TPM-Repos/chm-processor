Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateConditionFromExisting Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateConditionFromExisting Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionSequnceRef_
    The reference to the condition sequence to modify.

_conditionType_
    The type of condition to create.

_conditionData_
    The XElement containing the data for the condition.

_index_
    The index at which the condition will be placed.

Glossary Item Box

Creates a transaction which, when committed, will create a new condition from existing condition data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateConditionFromExisting( _
       ByVal _conditionSequnceRef_ As [ConditionSequenceRef](topic12852.md), _
       ByVal _conditionType_ As Type, _
       ByVal _conditionData_ As XElement, _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionSequnceRef As [ConditionSequenceRef](topic12852.md)
    Dim conditionType As Type
    Dim conditionData As XElement
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateConditionFromExisting(conditionSequnceRef, conditionType, conditionData, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateConditionFromExisting( 
       [ConditionSequenceRef](topic12852.md) _conditionSequnceRef_ ,
       Type _conditionType_ ,
       XElement _conditionData_ ,
       int _index_
    )  
  
#### Parameters

 _conditionSequnceRef_
    The reference to the condition sequence to modify.
_conditionType_
    The type of condition to create.
_conditionData_
    The XElement containing the data for the condition.
_index_
    The index at which the condition will be placed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


