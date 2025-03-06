![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventSequenceEventArgs Constructor(FlowEvent)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [EventSequenceEventArgs Class](topic10886.md) > [EventSequenceEventArgs Constructor](topic10892.md) : EventSequenceEventArgs Constructor(FlowEvent)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_event_
    The event which is the target of the event.

Glossary Item Box

Initializes a new instance of the [EventSequenceEventArgs](topic10886.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _event_ As [FlowEvent](topic10897.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim event As [FlowEvent](topic10897.md)
     
    Dim instance As New [EventSequenceEventArgs](topic10886.md)(event)  
  
C#|   
---|---  
      
    
    public EventSequenceEventArgs( 
       [FlowEvent](topic10897.md) _event_
    )  
  
#### Parameters

 _event_
    The event which is the target of the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[EventSequenceEventArgs Class](topic10886.md)   
[EventSequenceEventArgs Members](topic10887.md)   
[Overload List](topic10892.md)


