Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskReleaseConditionTitle Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeComponentTaskReleaseConditionTitle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to which the task owning the condition belongs to.

_taskName_
    The name of the task that owns the condition.

_conditionName_
    The title of the condition to update.

_newName_
    The new title to give the condition (or the old title if no change is desired).

_ruleChanges_
    The changes to the condition's rules to apply.

Glossary Item Box

Creates a new transaction that when executed will change the title of the given component task release condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeComponentTaskReleaseConditionTitle( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _taskName_ As String, _
       ByVal _conditionName_ As String, _
       ByVal _newName_ As String, _
       ByVal ParamArray _ruleChanges_() As [FlowPropertyData](topic12873.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim taskName As String
    Dim conditionName As String
    Dim newName As String
    Dim ruleChanges() As [FlowPropertyData](topic12873.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskReleaseConditionTitle(component, taskName, conditionName, newName, ruleChanges)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskReleaseConditionTitle( 
       [ProjectComponent](topic6183.md) _component_ ,
       string _taskName_ ,
       string _conditionName_ ,
       string _newName_ ,
       params [FlowPropertyData](topic12873.md)[] _ruleChanges_
    )  
  
#### Parameters

 _component_
    The component to which the task owning the condition belongs to.
_taskName_
    The name of the task that owns the condition.
_conditionName_
    The title of the condition to update.
_newName_
    The new title to give the condition (or the old title if no change is desired).
_ruleChanges_
    The changes to the condition's rules to apply.

#### Return Value

A transaction that when executed will update the title of the given condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| component, conditionName, conditionName, or newName is null.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


