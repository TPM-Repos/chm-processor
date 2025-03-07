Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteScopedComponentTask Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteScopedComponentTask Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope of the task to delete.

_taskName_
    The name of the task to delete.

Glossary Item Box

Creates a new transaction that when executed will delete the given scoped [DriveWorks.Components.Tasks.ComponentTask](topic6407.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteScopedComponentTask( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteScopedComponentTask(scope, taskName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteScopedComponentTask( 
       string _scope_ ,
       string _taskName_
    )  
  
#### Parameters

 _scope_
    The scope of the task to delete.
_taskName_
    The name of the task to delete.

#### Return Value

A transaction that when executed will delete the task with the given name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


