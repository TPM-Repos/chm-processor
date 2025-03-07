Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteScopedComponentTaskCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteScopedComponentTaskCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope the task that owns the condition belongs to.

_taskName_
    The name of the task that owns the condition to delete.

_conditionName_
    The name of the condition to delete.

Glossary Item Box

Creates a new transaction that when executed will delete the given condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteScopedComponentTaskCondition( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String, _
       ByVal _conditionName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim conditionName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteScopedComponentTaskCondition(scope, taskName, conditionName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteScopedComponentTaskCondition( 
       string _scope_ ,
       string _taskName_ ,
       string _conditionName_
    )  
  
#### Parameters

 _scope_
    The scope the task that owns the condition belongs to.
_taskName_
    The name of the task that owns the condition to delete.
_conditionName_
    The name of the condition to delete.

#### Return Value

A transaction that when executed will delete the given condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| Any of the arguments are null.  
System.ArgumentException| scope is an empty string.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


