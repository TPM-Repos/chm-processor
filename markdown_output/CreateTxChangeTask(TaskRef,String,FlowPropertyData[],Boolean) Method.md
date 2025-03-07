Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeTask(TaskRef,String,FlowPropertyData[],Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeTask Method](topic13012.md) : CreateTxChangeTask(TaskRef,String,FlowPropertyData[],Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskRef_
    The reference to the task to modify.

_newTitle_
    The new title of the task.

_newProperties_
    A specific object array of the new properties for the task.

_allowEmptyRules_
    True to allow toggling properties to dynamic without a rule.

Glossary Item Box

Creates a transaction which, when committed, will change the properties of the specified task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeTask( _
       ByVal _taskRef_ As [TaskRef](topic13149.md), _
       ByVal _newTitle_ As String, _
       ByVal _newProperties_() As [FlowPropertyData](topic12873.md), _
       ByVal _allowEmptyRules_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskRef As [TaskRef](topic13149.md)
    Dim newTitle As String
    Dim newProperties() As [FlowPropertyData](topic12873.md)
    Dim allowEmptyRules As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeTask(taskRef, newTitle, newProperties, allowEmptyRules)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeTask( 
       [TaskRef](topic13149.md) _taskRef_ ,
       string _newTitle_ ,
       [FlowPropertyData](topic12873.md)[] _newProperties_ ,
       bool _allowEmptyRules_
    )  
  
#### Parameters

 _taskRef_
    The reference to the task to modify.
_newTitle_
    The new title of the task.
_newProperties_
    A specific object array of the new properties for the task.
_allowEmptyRules_
    True to allow toggling properties to dynamic without a rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13012.md)


