Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectClosing Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : ProjectClosing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the active project is about to be closed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProjectClosing As CancelEventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim handler As CancelEventHandler
     
    AddHandler instance.ProjectClosing, handler  
  
C#|   
---|---  
      
    
    event CancelEventHandler ProjectClosing  
  
# Event Data

The event handler receives an argument of type CancelEventArgs containing data related to this event. The following **CancelEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Cancel|   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)


