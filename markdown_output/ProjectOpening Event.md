Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectOpening Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : ProjectOpening Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a project is about to be opened. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProjectOpening As EventHandler(Of ProjectOpeningEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim handler As EventHandler(Of ProjectOpeningEventArgs)
     
    AddHandler instance.ProjectOpening, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ProjectOpeningEventArgs> ProjectOpening  
  
# Event Data

The event handler receives an argument of type [ProjectOpeningEventArgs](topic898.md) containing data related to this event. The following **ProjectOpeningEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CancelOpening](topic905.md)| Gets/sets whether or not opening of the project should be canceled.   
[ProjectDetails](topic906.md)| Gets the [ProjectDetails](topic906.md) of the project that is opening.   
  
# Remarks

The [ProjectOpeningEventArgs](topic898.md) will be null if this event is fired as a result of creating a new project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)


