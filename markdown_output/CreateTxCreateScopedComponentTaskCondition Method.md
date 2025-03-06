![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateScopedComponentTaskCondition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13056.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateScopedComponentTaskCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    The scope of the task that the condition should be associated with.

_taskName_
    The name of the task to associate the new condition with.

_conditionType_
    The type of the condition to create.

_name_
    The name to give the newly created condition.

Glossary Item Box

Creates a new transaction that when executed will create a new component task condition for a scoped component task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateScopedComponentTaskCondition( _
       ByVal _scope_ As String, _
       ByVal _taskName_ As String, _
       ByVal _conditionType_ As Type, _
       ByVal _name_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim scope As String
    Dim taskName As String
    Dim conditionType As Type
    Dim name As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateScopedComponentTaskCondition(scope, taskName, conditionType, name)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateScopedComponentTaskCondition( 
       string _scope_ ,
       string _taskName_ ,
       Type _conditionType_ ,
       string _name_
    )  
  
#### Parameters

 _scope_
    The scope of the task that the condition should be associated with.
_taskName_
    The name of the task to associate the new condition with.
_conditionType_
    The type of the condition to create.
_name_
    The name to give the newly created condition.

#### Return Value

A transaction that when executed will create the specified condition.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| Any of the arguments are null.  
System.ArgumentException| name is an empty string.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
