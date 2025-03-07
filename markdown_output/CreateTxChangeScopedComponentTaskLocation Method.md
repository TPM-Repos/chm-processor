Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeScopedComponentTaskLocation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeScopedComponentTaskLocation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_task_
    The task to rename.

_location_
    The new location of the task.

Glossary Item Box

Creates a new transaction that when executed will change the location of the given task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeScopedComponentTaskLocation( _
       ByVal _task_ As [ComponentTask](topic6407.md), _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim task As [ComponentTask](topic6407.md)
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeScopedComponentTaskLocation(task, location)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeScopedComponentTaskLocation( 
       [ComponentTask](topic6407.md) _task_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _location_
    )  
  
#### Parameters

 _task_
    The task to rename.
_location_
    The new location of the task.

#### Return Value

A transaction that when executed will change the location of the given task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


