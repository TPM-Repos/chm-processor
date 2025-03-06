![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectedItemsChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic428.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISelectionSite Interface](topic422.md) : SelectedItemsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the selected items property has been changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event SelectedItemsChanged As [SelectionChangedEventHandler](topic1270.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISelectionSite](topic422.md)
    Dim handler As [SelectionChangedEventHandler](topic1270.md)
     
    AddHandler instance.SelectedItemsChanged, handler  
  
C#|   
---|---  
      
    
    event [SelectionChangedEventHandler](topic1270.md) SelectedItemsChanged  
  
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

[ISelectionSite Interface](topic422.md)   
[ISelectionSite Members](topic423.md)

©2024 DriveWorks Ltd. All Rights Reserved.
