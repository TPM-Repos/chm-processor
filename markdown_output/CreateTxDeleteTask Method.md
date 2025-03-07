Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_taskRef_
    The reference to the task to delete.

Glossary Item Box

Creates a transaction which, when committed, will delete a task from the given parent object's task sequence. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteTask( _
       ByVal _taskRef_ As [TaskRef](topic13149.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim taskRef As [TaskRef](topic13149.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteTask(taskRef)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteTask( 
       [TaskRef](topic13149.md) _taskRef_
    )  
  
#### Parameters

 _taskRef_
    The reference to the task to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


