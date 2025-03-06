![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentSetNameChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4161.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : ComponentSetNameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a component set's name changes. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ComponentSetNameChanged As EventHandler(Of ProjectComponentSetNameChangedEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim handler As EventHandler(Of ProjectComponentSetNameChangedEventArgs)
     
    AddHandler instance.ComponentSetNameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ProjectComponentSetNameChangedEventArgs> ComponentSetNameChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ProjectComponentSetNameChangedEventArgs](topic4134.md) containing data related to this event. The following **ProjectComponentSetNameChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ComponentSet](topic4140.md)| Gets the component set that was changed.   
[NewName](topic4141.md)| Gets the new name of the component set.   
[OldName](topic4142.md)| Gets the old name of the component set.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)

©2024 DriveWorks Ltd. All Rights Reserved.
