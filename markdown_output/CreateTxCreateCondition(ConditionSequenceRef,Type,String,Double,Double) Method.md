Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateCondition(ConditionSequenceRef,Type,String,Double,Double) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateCondition Method](topic13034.md) : CreateTxCreateCondition(ConditionSequenceRef,Type,String,Double,Double) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionSequenceRef_
    The reference to the condition sequence.

_conditionType_
    The type of the condition to create.

_conditionTitle_
    The title to give the condition.

_left_
    The left position to give the condition.

_top_
    The top position to give the condition.

Glossary Item Box

Creates a transaction which, when committed, will create a new condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateCondition( _
       ByVal _conditionSequenceRef_ As [ConditionSequenceRef](topic12852.md), _
       ByVal _conditionType_ As Type, _
       ByVal _conditionTitle_ As String, _
       ByVal _left_ As Double, _
       ByVal _top_ As Double _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionSequenceRef As [ConditionSequenceRef](topic12852.md)
    Dim conditionType As Type
    Dim conditionTitle As String
    Dim left As Double
    Dim top As Double
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateCondition(conditionSequenceRef, conditionType, conditionTitle, left, top)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateCondition( 
       [ConditionSequenceRef](topic12852.md) _conditionSequenceRef_ ,
       Type _conditionType_ ,
       string _conditionTitle_ ,
       double _left_ ,
       double _top_
    )  
  
#### Parameters

 _conditionSequenceRef_
    The reference to the condition sequence.
_conditionType_
    The type of the condition to create.
_conditionTitle_
    The title to give the condition.
_left_
    The left position to give the condition.
_top_
    The top position to give the condition.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13034.md)


