Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventLogged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplicationEventService Interface](topic49.md) : EventLogged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an event is logged. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event EventLogged As EventHandler(Of ApplicationEventEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationEventService](topic49.md)
    Dim handler As EventHandler(Of ApplicationEventEventArgs)
     
    AddHandler instance.EventLogged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ApplicationEventEventArgs> EventLogged  
  
# Event Data

The event handler receives an argument of type [ApplicationEventEventArgs](topic663.md) containing data related to this event. The following **ApplicationEventEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Event](topic670.md)| Gets the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationEventService Interface](topic49.md)   
[IApplicationEventService Members](topic50.md)


