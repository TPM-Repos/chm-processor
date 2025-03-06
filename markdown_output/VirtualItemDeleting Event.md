![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemDeleting Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic605.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IVirtualSplitCommandButton Interface](topic598.md) : VirtualItemDeleting Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the user presses the delete key on a virtual item on the drop down list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event VirtualItemDeleting As [VirtualItemDeletingEventHandler](topic1274.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IVirtualSplitCommandButton](topic598.md)
    Dim handler As [VirtualItemDeletingEventHandler](topic1274.md)
     
    AddHandler instance.VirtualItemDeleting, handler  
  
C#|   
---|---  
      
    
    event [VirtualItemDeletingEventHandler](topic1274.md) VirtualItemDeleting  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [VirtualItemDeletingEventArgs](topic1175.md) containing data related to this event. The following **VirtualItemDeletingEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Cancel](topic1182.md)| Gets/sets whether the delete should be cancelled.   
[Item](topic1183.md)| Gets the data for the virtual item that was selected.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IVirtualSplitCommandButton Interface](topic598.md)   
[IVirtualSplitCommandButton Members](topic599.md)

©2024 DriveWorks Ltd. All Rights Reserved.
