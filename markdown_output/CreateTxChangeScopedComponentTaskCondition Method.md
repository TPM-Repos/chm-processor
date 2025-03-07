Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeScopedComponentTaskCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeScopedComponentTaskCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope to which the task that owns the condition belongs to.

_taskName_
    The name of the task that owns the condition to change.

_conditionName_
    The name of the condition to change.

_newName_
    The new name of the condition (or the old name if no change is desired).

_ruleChanges_
    The changes to the condition's rules to apply.

Glossary Item Box

Creates a new transaction that when executed will change the title of the given condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeScopedComponentTaskCondition( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String, _
       ByVal _conditionName_ As String, _
       ByVal _newName_ As String, _
       ByVal ParamArray _ruleChanges_() As [RuleChangeData](topic5254.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim conditionName As String
    Dim newName As String
    Dim ruleChanges() As [RuleChangeData](topic5254.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeScopedComponentTaskCondition(scope, taskName, conditionName, newName, ruleChanges)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeScopedComponentTaskCondition( 
       string _scope_ ,
       string _taskName_ ,
       string _conditionName_ ,
       string _newName_ ,
       params [RuleChangeData](topic5254.md)[] _ruleChanges_
    )  
  
#### Parameters

 _scope_
    The scope to which the task that owns the condition belongs to.
_taskName_
    The name of the task that owns the condition to change.
_conditionName_
    The name of the condition to change.
_newName_
    The new name of the condition (or the old name if no change is desired).
_ruleChanges_
    The changes to the condition's rules to apply.

#### Return Value

A transaction that when executed will change the given condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| Any of the arguments are null.  
System.ArgumentException| newName is an empty string.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


