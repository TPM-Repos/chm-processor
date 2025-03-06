       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionInvoked Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11280.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : TransitionInvoked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a transition has been invoked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TransitionInvoked As [TransitionEventHandler](topic11827.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [TransitionEventHandler](topic11827.md)
     
    AddHandler instance.TransitionInvoked, handler  
  
C#|   
---|---  
      
    
    public event [TransitionEventHandler](topic11827.md) TransitionInvoked  
  
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

©2024 DriveWorks Ltd. All Rights Reserved.
