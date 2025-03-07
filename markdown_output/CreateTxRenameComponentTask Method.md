Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRenameComponentTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRenameComponentTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to rename.

_newName_
    The new name to give the task.

_component_
    The component the task is associated with.

Glossary Item Box

Creates a new transaction that when executed will change the name of the given task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRenameComponentTask( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _newName_ As String, _
       ByVal _component_ As [ProjectComponent](topic6183.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim newName As String
    Dim component As [ProjectComponent](topic6183.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRenameComponentTask(task, newName, component)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRenameComponentTask( 
       [ComponentTask](topic6407.md) _task_ ,
       string _newName_ ,
       [ProjectComponent](topic6183.md) _component_
    )  
  
#### Parameters

 _task_
    The task to rename.
_newName_
    The new name to give the task.
_component_
    The component the task is associated with.

#### Return Value

A transaction that when executed will change the name of the given task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


