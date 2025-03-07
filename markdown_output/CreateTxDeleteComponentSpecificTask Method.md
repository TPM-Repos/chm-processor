Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteComponentSpecificTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteComponentSpecificTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The [DriveWorks.Components.ProjectComponent](topic6183.md) the task is associated with.

_taskName_
    The name of the task to delete.

Glossary Item Box

Creates a new transaction that when executed will delete the specified component specific [DriveWorks.Components.Tasks.ComponentTask](topic6407.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteComponentSpecificTask( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _taskName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim taskName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteComponentSpecificTask(component, taskName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteComponentSpecificTask( 
       [ProjectComponent](topic6183.md) _component_ ,
       string _taskName_
    )  
  
#### Parameters

 _component_
    The [DriveWorks.Components.ProjectComponent](topic6183.md) the task is associated with.
_taskName_
    The name of the task to delete.

#### Return Value

A transaction that when executed will delete the specified task.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


