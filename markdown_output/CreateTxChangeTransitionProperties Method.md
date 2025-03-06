![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeTransitionProperties Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeTransitionProperties Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_transition_
    The the transition to update.

_targetStateTitle_
    The title of the target state.

_newTitle_
    The new title for the transition.

_newConditons_
    The new conditions for the transition.

_newInvokeTaskSequence_
    The new invoke task sequence for the transition

Glossary Item Box

Creates a transaction which, when committed, will update a transition with the given properties. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeTransitionProperties( _
       ByVal _transition_ As [Transition](topic11757.md), _
       ByVal _targetStateTitle_ As String, _
       ByVal _newTitle_ As String, _
       ByVal _newConditons_() As [Condition](topic10804.md), _
       ByVal _newInvokeTaskSequence_() As [Task](topic11629.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim transition As [Transition](topic11757.md)
    Dim targetStateTitle As String
    Dim newTitle As String
    Dim newConditons() As [Condition](topic10804.md)
    Dim newInvokeTaskSequence() As [Task](topic11629.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeTransitionProperties(transition, targetStateTitle, newTitle, newConditons, newInvokeTaskSequence)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeTransitionProperties( 
       [Transition](topic11757.md) _transition_ ,
       string _targetStateTitle_ ,
       string _newTitle_ ,
       [Condition](topic10804.md)[] _newConditons_ ,
       [Task](topic11629.md)[] _newInvokeTaskSequence_
    )  
  
#### Parameters

 _transition_
    The the transition to update.
_targetStateTitle_
    The title of the target state.
_newTitle_
    The new title for the transition.
_newConditons_
    The new conditions for the transition.
_newInvokeTaskSequence_
    The new invoke task sequence for the transition

# ![](dotnetimages/collapse.gif)Remarks

Arguments can be set to nothing if no change is needed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


