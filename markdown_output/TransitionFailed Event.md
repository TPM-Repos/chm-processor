       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionFailed Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1790.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationRequest Interface](topic1778.md) : TransitionFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the specification is being processed and a transition with the given name is invalid. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event TransitionFailed As EventHandler(Of TransitionFailedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequest](topic1778.md)
    Dim handler As EventHandler(Of TransitionFailedEventArgs)
     
    AddHandler instance.TransitionFailed, handler  
  
C#|   
---|---  
      
    
    event EventHandler<TransitionFailedEventArgs> TransitionFailed  
  
# Event Data

The event handler receives an argument of type [TransitionFailedEventArgs](topic1968.md) containing data related to this event. The following **TransitionFailedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic1975.md)| The exception that occurred during execution of the transition, e.g. if the transition could not be found, or the user doesn't have permissions to access the transition.   
[Result](topic1976.md)| The result of executing the transition, e.g. false if the conditions on the transition could not be satisfied.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[ISpecificationRequest Members](topic1779.md)

©2024 DriveWorks Ltd. All Rights Reserved.
