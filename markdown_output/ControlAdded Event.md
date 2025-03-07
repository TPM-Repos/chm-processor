Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) : ControlAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a control is added to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ControlAdded As [ControlEventHandler](topic9366.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim handler As [ControlEventHandler](topic9366.md)
     
    AddHandler instance.ControlAdded, handler  
  
C#|   
---|---  
      
    
    public event [ControlEventHandler](topic9366.md) ControlAdded  
  
# Event Data

The event handler receives an argument of type [ControlEventArgs](topic7806.md) containing data related to this event. The following **ControlEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Control](topic7815.md)| Gets the control that was affected by the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)


