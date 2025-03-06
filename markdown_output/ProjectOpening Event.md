![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectOpening Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic400.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : ProjectOpening Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a project is about to be opened. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProjectOpening As EventHandler(Of ProjectOpeningEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim handler As EventHandler(Of ProjectOpeningEventArgs)
     
    AddHandler instance.ProjectOpening, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ProjectOpeningEventArgs> ProjectOpening  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ProjectOpeningEventArgs](topic898.md) containing data related to this event. The following **ProjectOpeningEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CancelOpening](topic905.md)| Gets/sets whether or not opening of the project should be canceled.   
[ProjectDetails](topic906.md)| Gets the [ProjectDetails](topic906.md) of the project that is opening.   
  
# ![](dotnetimages/collapse.gif)Remarks

The [ProjectOpeningEventArgs](topic898.md) will be null if this event is fired as a result of creating a new project.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)

©2024 DriveWorks Ltd. All Rights Reserved.
