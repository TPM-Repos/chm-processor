Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateScopedComponentTaskReleaseCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateScopedComponentTaskReleaseCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope of the task to create the condition on.

_taskName_
    The task to associate the new condition with.

_conditionType_
    The type of the condition to create.

_name_
    The title to give the newly created condition.

Glossary Item Box

Creates a new transaction that when executed will create a new component task release condition for a scoped component task. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateScopedComponentTaskReleaseCondition( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String, _
       ByVal _conditionType_ As Type, _
       ByVal _name_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim conditionType As Type
    Dim name As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateScopedComponentTaskReleaseCondition(scope, taskName, conditionType, name)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateScopedComponentTaskReleaseCondition( 
       string _scope_ ,
       string _taskName_ ,
       Type _conditionType_ ,
       string _name_
    )  
  
#### Parameters

 _scope_
    The scope of the task to create the condition on.
_taskName_
    The task to associate the new condition with.
_conditionType_
    The type of the condition to create.
_name_
    The title to give the newly created condition.

#### Return Value

A transaction that when executed will create the specified condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| Any of the arguments are null.  
System.ArgumentException| The parameter name is an empty string.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


