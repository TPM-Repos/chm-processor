![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeStateProperties Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeStateProperties Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The state to update.

_newTitle_
    The new title of the state.

_newSpecFlowStateType_
    The new type for the state.

_newOnStateEnterEvent_
    The new enter event for the state.

_newOnStateLeaveEvent_
    The new leave event for the state.

Glossary Item Box

Creates a transaction which, when committed, will update a states properties, old title is the current title of the state - before update. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeStateProperties( _
       ByVal _state_ As [State](topic11559.md), _
       ByVal _newTitle_ As String, _
       ByVal _newSpecFlowStateType_ As [StateType](topic10773.md), _
       ByVal _newOnStateEnterEvent_() As [Task](topic11629.md), _
       ByVal _newOnStateLeaveEvent_() As [Task](topic11629.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim state As [State](topic11559.md)
    Dim newTitle As String
    Dim newSpecFlowStateType As [StateType](topic10773.md)
    Dim newOnStateEnterEvent() As [Task](topic11629.md)
    Dim newOnStateLeaveEvent() As [Task](topic11629.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeStateProperties(state, newTitle, newSpecFlowStateType, newOnStateEnterEvent, newOnStateLeaveEvent)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeStateProperties( 
       [State](topic11559.md) _state_ ,
       string _newTitle_ ,
       [StateType](topic10773.md) _newSpecFlowStateType_ ,
       [Task](topic11629.md)[] _newOnStateEnterEvent_ ,
       [Task](topic11629.md)[] _newOnStateLeaveEvent_
    )  
  
#### Parameters

 _state_
    The state to update.
_newTitle_
    The new title of the state.
_newSpecFlowStateType_
    The new type for the state.
_newOnStateEnterEvent_
    The new enter event for the state.
_newOnStateLeaveEvent_
    The new leave event for the state.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


