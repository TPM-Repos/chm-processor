Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventSequenceInvoked Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : EventSequenceInvoked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an event task-sequence has been invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event EventSequenceInvoked As [EventSequenceEventHandler](topic11819.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [EventSequenceEventHandler](topic11819.md)
     
    AddHandler instance.EventSequenceInvoked, handler  
  
C#|   
---|---  
      
    
    public event [EventSequenceEventHandler](topic11819.md) EventSequenceInvoked  
  
# Event Data

The event handler receives an argument of type [EventSequenceEventArgs](topic10886.md) containing data related to this event. The following **EventSequenceEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Event](topic10896.md)| Gets the event which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


