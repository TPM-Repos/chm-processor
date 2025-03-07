Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : ControlCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a control is created on any form or dialog. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ControlCreated As EventHandler(Of ControlEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim handler As EventHandler(Of ControlEventArgs)
     
    AddHandler instance.ControlCreated, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ControlEventArgs> ControlCreated  
  
# Event Data

The event handler receives an argument of type [ControlEventArgs](topic7806.md) containing data related to this event. The following **ControlEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Control](topic7815.md)| Gets the control that was affected by the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


