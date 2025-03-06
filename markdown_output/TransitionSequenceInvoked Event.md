TransitionSequenceInvoked Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : TransitionSequenceInvoked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a transition task-sequence has been invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TransitionSequenceInvoked As [TransitionEventHandler](topic11827.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [TransitionEventHandler](topic11827.md)
     
    AddHandler instance.TransitionSequenceInvoked, handler  
  
C#|   
---|---  
      
    
    public event [TransitionEventHandler](topic11827.md) TransitionSequenceInvoked  
  
# Event Data

The event handler receives an argument of type [TransitionEventArgs](topic11776.md) containing data related to this event. The following **TransitionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Transition](topic11786.md)| Gets the transition which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


