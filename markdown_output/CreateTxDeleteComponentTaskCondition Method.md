Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteComponentTaskCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteComponentTaskCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to which the task owning the condition belongs to.

_taskName_
    The task that owns the condition to delete.

_conditionName_
    The condition to delete.

Glossary Item Box

Creates a new transaction that when executed will delete the given condition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteComponentTaskCondition( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _taskName_ As String, _
       ByVal _conditionName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim taskName As String
    Dim conditionName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteComponentTaskCondition(component, taskName, conditionName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteComponentTaskCondition( 
       [ProjectComponent](topic6183.md) _component_ ,
       string _taskName_ ,
       string _conditionName_
    )  
  
#### Parameters

 _component_
    The component to which the task owning the condition belongs to.
_taskName_
    The task that owns the condition to delete.
_conditionName_
    The condition to delete.

#### Return Value

A transaction that when executed will delete the given condition.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| component, taskName, or conditionName is null.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


