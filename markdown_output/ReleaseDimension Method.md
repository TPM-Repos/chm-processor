![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseDimension Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15036.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSolidWorksComponent Class](topic15029.md) : ReleaseDimension Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controller_
    

_data_
    

_param_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Shared Sub ReleaseDimension( _
       ByVal _controller_ As [ReleaseComponentController](topic6252.md), _
       ByVal _data_ As ReleasedComponentData, _
       ByVal _param_ As ReleasedParameterData _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controller As [ReleaseComponentController](topic6252.md)
    Dim data As ReleasedComponentData
    Dim param As ReleasedParameterData
     
    [ReleasedSolidWorksComponent](topic15029.md).ReleaseDimension(controller, data, param)  
  
C#|   
---|---  
      
    
    protected static void ReleaseDimension( 
       [ReleaseComponentController](topic6252.md) _controller_ ,
       ReleasedComponentData _data_ ,
       ReleasedParameterData _param_
    )  
  
#### Parameters

 _controller_
    
_data_
    
_param_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedSolidWorksComponent Class](topic15029.md)   
[ReleasedSolidWorksComponent Members](topic15030.md)

©2024 DriveWorks Ltd. All Rights Reserved.
