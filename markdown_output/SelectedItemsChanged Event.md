![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectedItemsChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1153.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : SelectedItemsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SelectedItemsChanged As [SelectionChangedEventHandler](topic1270.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim handler As [SelectionChangedEventHandler](topic1270.md)
     
    AddHandler instance.SelectedItemsChanged, handler  
  
C#|   
---|---  
      
    
    public event [SelectionChangedEventHandler](topic1270.md) SelectedItemsChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [SelectionChangeEventArgs](topic926.md) containing data related to this event. The following **SelectionChangeEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[NewSelectedItems](topic933.md)| Gets the new selection.   
[OldSelectedItems](topic934.md)| Gets the selection before the change took place.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
