Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRenameScopedComponentTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxRenameScopedComponentTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to rename.

_newName_
    The new name to give the task.

Glossary Item Box

Creates a new transaction that when executed will change the name of the given task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxRenameScopedComponentTask( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRenameScopedComponentTask(task, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRenameScopedComponentTask( 
       [ComponentTask](topic6407.md) _task_ ,
       string _newName_
    )  
  
#### Parameters

 _task_
    The task to rename.
_newName_
    The new name to give the task.

#### Return Value

A transaction that when executed will change the name of the given task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


