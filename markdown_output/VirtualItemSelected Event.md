![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VirtualItemSelected Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic606.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IVirtualSplitCommandButton Interface](topic598.md) : VirtualItemSelected Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a virtual item on the drop down list is clicked. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event VirtualItemSelected As [VirtualItemSelectedEventHandler](topic1275.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IVirtualSplitCommandButton](topic598.md)
    Dim handler As [VirtualItemSelectedEventHandler](topic1275.md)
     
    AddHandler instance.VirtualItemSelected, handler  
  
C#|   
---|---  
      
    
    event [VirtualItemSelectedEventHandler](topic1275.md) VirtualItemSelected  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [VirtualItemSelectedEventArgs](topic1184.md) containing data related to this event. The following **VirtualItemSelectedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic1191.md)| Gets the data for the virtual item that was selected.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IVirtualSplitCommandButton Interface](topic598.md)   
[IVirtualSplitCommandButton Members](topic599.md)

©2024 DriveWorks Ltd. All Rights Reserved.
