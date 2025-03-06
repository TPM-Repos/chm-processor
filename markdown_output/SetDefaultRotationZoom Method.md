![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDefaultRotationZoom Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic368.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetDefaultRotationZoom Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_defaultRotationZoom_
    The default rotation and zoom.

Glossary Item Box

Sets the default rotation and zoom of the preview control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetDefaultRotationZoom( _
       ByVal _defaultRotationZoom_ As DriveWorks.Support.RotationZoom _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim defaultRotationZoom As DriveWorks.Support.RotationZoom
     
    instance.SetDefaultRotationZoom(defaultRotationZoom)  
  
C#|   
---|---  
      
    
    void SetDefaultRotationZoom( 
       DriveWorks.Support.RotationZoom _defaultRotationZoom_
    )  
  
#### Parameters

 _defaultRotationZoom_
    The default rotation and zoom.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)

©2024 DriveWorks Ltd. All Rights Reserved.
