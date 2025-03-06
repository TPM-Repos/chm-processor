![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Clicked Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic123.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButton Interface](topic115.md) : Clicked Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the command button is clicked. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Clicked As MouseEventHandler  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandButton](topic115.md)
    Dim handler As MouseEventHandler
     
    AddHandler instance.Clicked, handler  
  
C#|   
---|---  
      
    
    event MouseEventHandler Clicked  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type MouseEventArgs containing data related to this event. The following **MouseEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Button|   
Clicks|   
Delta|   
Location|   
X|   
Y|   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandButton Interface](topic115.md)   
[ICommandButton Members](topic116.md)

©2024 DriveWorks Ltd. All Rights Reserved.
