Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxMoveCondition(ConditionSequenceRef,Int32,Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxMoveCondition Method](topic13112.md) : CreateTxMoveCondition(ConditionSequenceRef,Int32,Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionSequenceRef_
    The reference to the condition sequence.

_oldIndex_
    The index of the condition to move.

_newIndex_
    The index of where to move the condition.

Glossary Item Box

Creates a transaction which, when committed, will move the given condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxMoveCondition( _
       ByVal _conditionSequenceRef_ As [ConditionSequenceRef](topic12852.md), _
       ByVal _oldIndex_ As Integer, _
       ByVal _newIndex_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionSequenceRef As [ConditionSequenceRef](topic12852.md)
    Dim oldIndex As Integer
    Dim newIndex As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxMoveCondition(conditionSequenceRef, oldIndex, newIndex)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxMoveCondition( 
       [ConditionSequenceRef](topic12852.md) _conditionSequenceRef_ ,
       int _oldIndex_ ,
       int _newIndex_
    )  
  
#### Parameters

 _conditionSequenceRef_
    The reference to the condition sequence.
_oldIndex_
    The index of the condition to move.
_newIndex_
    The index of where to move the condition.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13112.md)


