![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeCondition(ConditionRef,String,ConditionFailBehavior,FlowPropertyData[],Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12954.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxChangeCondition Method](topic12952.md) : CreateTxChangeCondition(ConditionRef,String,ConditionFailBehavior,FlowPropertyData[],Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_conditionRef_
    The reference to the condition to modify.

_newTitle_
    

_newFailBehavior_
    The new failure behavior of the condition.

_newProperties_
    The new properties to assign the condition.

_allowEmptyRules_
    True to allow rules to be made dynamic with empty rules.

Glossary Item Box

Creates a transaction which, when committed, will change the properties of the specified condition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxChangeCondition( _
       ByVal _conditionRef_ As [ConditionRef](topic12843.md), _
       ByVal _newTitle_ As String, _
       ByVal _newFailBehavior_ As [ConditionFailBehavior](topic10766.md), _
       ByVal _newProperties_() As [FlowPropertyData](topic12873.md), _
       ByVal _allowEmptyRules_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim conditionRef As [ConditionRef](topic12843.md)
    Dim newTitle As String
    Dim newFailBehavior As [ConditionFailBehavior](topic10766.md)
    Dim newProperties() As [FlowPropertyData](topic12873.md)
    Dim allowEmptyRules As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeCondition(conditionRef, newTitle, newFailBehavior, newProperties, allowEmptyRules)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeCondition( 
       [ConditionRef](topic12843.md) _conditionRef_ ,
       string _newTitle_ ,
       [ConditionFailBehavior](topic10766.md) _newFailBehavior_ ,
       [FlowPropertyData](topic12873.md)[] _newProperties_ ,
       bool _allowEmptyRules_
    )  
  
#### Parameters

 _conditionRef_
    The reference to the condition to modify.
_newTitle_
    
_newFailBehavior_
    The new failure behavior of the condition.
_newProperties_
    The new properties to assign the condition.
_allowEmptyRules_
    True to allow rules to be made dynamic with empty rules.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic12952.md)

©2024 DriveWorks Ltd. All Rights Reserved.
