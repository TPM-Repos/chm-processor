Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventsCleared Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplicationEventService Interface](topic49.md) : EventsCleared Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the events are cleared. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event EventsCleared As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationEventService](topic49.md)
    Dim handler As EventHandler
     
    AddHandler instance.EventsCleared, handler  
  
C#|   
---|---  
      
    
    event EventHandler EventsCleared  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationEventService Interface](topic49.md)   
[IApplicationEventService Members](topic50.md)


