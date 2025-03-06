![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConstantCreated Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4267.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstants Class](topic4246.md) : ConstantCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a constant is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConstantCreated As [ConstantChangedEventHandler](topic5929.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstants](topic4246.md)
    Dim handler As [ConstantChangedEventHandler](topic5929.md)
     
    AddHandler instance.ConstantCreated, handler  
  
C#|   
---|---  
      
    
    public event [ConstantChangedEventHandler](topic5929.md) ConstantCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ConstantEventArgs](topic2595.md) containing data related to this event. The following **ConstantEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Constant](topic2605.md)| Gets the constant that was changed.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectConstants Class](topic4246.md)   
[ProjectConstants Members](topic4247.md)

©2024 DriveWorks Ltd. All Rights Reserved.
