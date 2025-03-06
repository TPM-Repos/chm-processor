![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeComponentTaskCondition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeComponentTaskCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to which the task owning the condition belongs to.

_taskTitle_
    The name of the task the condition is associated with.

_conditionTitle_
    The name of the condition to update.

_newTitle_
    The new title to give the condition (or the old title if no change is desired).

_ruleChanges_
    The changes to the condition's rules to apply.

Glossary Item Box

Creates a new transaction that when executed will change the given component task condition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeComponentTaskCondition( _
       ByVal _component_ As [ProjectComponent](topic6183.md), _
       ByVal _taskTitle_ As String, _
       ByVal _conditionTitle_ As String, _
       ByVal _newTitle_ As String, _
       ByVal ParamArray _ruleChanges_() As [RuleChangeData](topic5254.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim taskTitle As String
    Dim conditionTitle As String
    Dim newTitle As String
    Dim ruleChanges() As [RuleChangeData](topic5254.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeComponentTaskCondition(component, taskTitle, conditionTitle, newTitle, ruleChanges)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeComponentTaskCondition( 
       [ProjectComponent](topic6183.md) _component_ ,
       string _taskTitle_ ,
       string _conditionTitle_ ,
       string _newTitle_ ,
       params [RuleChangeData](topic5254.md)[] _ruleChanges_
    )  
  
#### Parameters

 _component_
    The component to which the task owning the condition belongs to.
_taskTitle_
    The name of the task the condition is associated with.
_conditionTitle_
    The name of the condition to update.
_newTitle_
    The new title to give the condition (or the old title if no change is desired).
_ruleChanges_
    The changes to the condition's rules to apply.

#### Return Value

A transaction that when executed will update the title of the given condition.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| component, taskTitle, conditionTitle, or newTitle is null.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


