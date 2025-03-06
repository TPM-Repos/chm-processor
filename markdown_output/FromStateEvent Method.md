![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromStateEvent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13168.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TaskSequenceRef Class](topic13159.md) : FromStateEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_state_
    The state to which the event belongs.

_flowEvent_
    The event.

Glossary Item Box

Constructs a task sequence reference for the given event on the given state. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromStateEvent( _
       ByVal _state_ As [State](topic11559.md), _
       ByVal _flowEvent_ As [FlowEvent](topic10897.md) _
    ) As [TaskSequenceRef](topic13159.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim state As [State](topic11559.md)
    Dim flowEvent As [FlowEvent](topic10897.md)
    Dim value As [TaskSequenceRef](topic13159.md)
     
    value = [TaskSequenceRef](topic13159.md).FromStateEvent(state, flowEvent)  
  
C#|   
---|---  
      
    
    public static [TaskSequenceRef](topic13159.md) FromStateEvent( 
       [State](topic11559.md) _state_ ,
       [FlowEvent](topic10897.md) _flowEvent_
    )  
  
#### Parameters

 _state_
    The state to which the event belongs.
_flowEvent_
    The event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TaskSequenceRef Class](topic13159.md)   
[TaskSequenceRef Members](topic13160.md)

©2024 DriveWorks Ltd. All Rights Reserved.
