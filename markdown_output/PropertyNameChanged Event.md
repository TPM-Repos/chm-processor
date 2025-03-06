![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PropertyNameChanged Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4850.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) : PropertyNameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the name of a specification property is changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PropertyNameChanged As [ProjectSpecificationPropertyEventHandler](topic5934.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim handler As [ProjectSpecificationPropertyEventHandler](topic5934.md)
     
    AddHandler instance.PropertyNameChanged, handler  
  
C#|   
---|---  
      
    
    public event [ProjectSpecificationPropertyEventHandler](topic5934.md) PropertyNameChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ProjectSpecificationPropertyEventArgs](topic4874.md) containing data related to this event. The following **ProjectSpecificationPropertyEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SpecificationProperty](topic4884.md)| Gets the property that was affected by the event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)

©2024 DriveWorks Ltd. All Rights Reserved.
