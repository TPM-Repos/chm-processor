Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningChangedOnDescendant Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : IsRunningChangedOnDescendant Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [IsRunning](topic11215.md) property of a descendent specification context changes. This can be a child or a child's child etc. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IsRunningChangedOnDescendant As [SpecificationContextEventHandler](topic11821.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As [SpecificationContextEventHandler](topic11821.md)
     
    AddHandler instance.IsRunningChangedOnDescendant, handler  
  
C#|   
---|---  
      
    
    public event [SpecificationContextEventHandler](topic11821.md) IsRunningChangedOnDescendant  
  
# Event Data

The event handler receives an argument of type [SpecificationContextEventArgs](topic11284.md) containing data related to this event. The following **SpecificationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic11291.md)| Get the specification context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


