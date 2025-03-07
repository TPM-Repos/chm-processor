Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeScopedComponentTaskIndex Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeScopedComponentTaskIndex Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to rename.

_index_
    The new index of the task.

Glossary Item Box

Creates a new transaction that when executed will change the index of the given task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeScopedComponentTaskIndex( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeScopedComponentTaskIndex(task, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeScopedComponentTaskIndex( 
       [ComponentTask](topic6407.md) _task_ ,
       int _index_
    )  
  
#### Parameters

 _task_
    The task to rename.
_index_
    The new index of the task.

#### Return Value

A transaction that when executed will change the index of the given task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


