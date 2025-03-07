Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NavigationStepDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : NavigationStepDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a navigation step is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NavigationStepDeleted As [NavigationStepChangedEventHandler](topic10264.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim handler As [NavigationStepChangedEventHandler](topic10264.md)
     
    AddHandler instance.NavigationStepDeleted, handler  
  
C#|   
---|---  
      
    
    public event [NavigationStepChangedEventHandler](topic10264.md) NavigationStepDeleted  
  
# Event Data

The event handler receives an argument of type [NavigationStepEventArgs](topic10205.md) containing data related to this event. The following **NavigationStepEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[NavigationStep](topic10212.md)| Gets the navigation step that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


