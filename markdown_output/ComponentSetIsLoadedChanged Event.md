Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentSetIsLoadedChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : ComponentSetIsLoadedChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a component set is loaded or unloaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ComponentSetIsLoadedChanged As [ProjectComponentSetEventHandler](topic5933.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim handler As [ProjectComponentSetEventHandler](topic5933.md)
     
    AddHandler instance.ComponentSetIsLoadedChanged, handler  
  
C#|   
---|---  
      
    
    public event [ProjectComponentSetEventHandler](topic5933.md) ComponentSetIsLoadedChanged  
  
# Event Data

The event handler receives an argument of type [ProjectComponentSetEventArgs](topic4125.md) containing data related to this event. The following **ProjectComponentSetEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ComponentSet](topic4133.md)| Gets the component set that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)


