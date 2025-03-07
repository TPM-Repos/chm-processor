Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlsDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) : ControlsDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when one or more controls are deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ControlsDeleted As [ControlsEventHandler](topic9367.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim handler As [ControlsEventHandler](topic9367.md)
     
    AddHandler instance.ControlsDeleted, handler  
  
C#|   
---|---  
      
    
    public event [ControlsEventHandler](topic9367.md) ControlsDeleted  
  
# Event Data

The event handler receives an argument of type [ControlsEventArgs](topic7816.md) containing data related to this event. The following **ControlsEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Controls](topic7825.md)| Gets the controls that were affected by the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)


