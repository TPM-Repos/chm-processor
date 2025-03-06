![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxUndoDeleteTransition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxUndoDeleteTransition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceStateId_
    The Id of the source state.

_targetStateId_
    The Id of the target state.

_name_
    The name of the transition to re-create.

_title_
    The title of the transition to re-create.

_conditions_
    The conditions of the transition.

_teams_
    The teams of the transition.

_invokeEvent_
    The invoke event of the transition.

Glossary Item Box

Creates a transaction which, when committed, will undo the deletion of a transition with all its given parameters. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxUndoDeleteTransition( _
       ByVal _sourceStateId_ As Guid, _
       ByVal _targetStateId_ As Guid, _
       ByVal _name_ As String, _
       ByVal _title_ As String, _
       ByVal _conditions_ As [Conditions](topic10865.md), _
       ByVal _teams_ As [Teams](topic11737.md), _
       ByVal _invokeEvent_ As [FlowEvent](topic10897.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim sourceStateId As Guid
    Dim targetStateId As Guid
    Dim name As String
    Dim title As String
    Dim conditions As [Conditions](topic10865.md)
    Dim teams As [Teams](topic11737.md)
    Dim invokeEvent As [FlowEvent](topic10897.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxUndoDeleteTransition(sourceStateId, targetStateId, name, title, conditions, teams, invokeEvent)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxUndoDeleteTransition( 
       Guid _sourceStateId_ ,
       Guid _targetStateId_ ,
       string _name_ ,
       string _title_ ,
       [Conditions](topic10865.md) _conditions_ ,
       [Teams](topic11737.md) _teams_ ,
       [FlowEvent](topic10897.md) _invokeEvent_
    )  
  
#### Parameters

 _sourceStateId_
    The Id of the source state.
_targetStateId_
    The Id of the target state.
_name_
    The name of the transition to re-create.
_title_
    The title of the transition to re-create.
_conditions_
    The conditions of the transition.
_teams_
    The teams of the transition.
_invokeEvent_
    The invoke event of the transition.

# ![](dotnetimages/collapse.gif)Remarks

Parameters can be set to nothing for no prefernce.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


