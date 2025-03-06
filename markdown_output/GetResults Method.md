![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetResults Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12412.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [RealTimeReleaseModelsTask Class](topic12405.md) : GetResults Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    The specification context for the active specification.

Glossary Item Box

Releases the configured models and returns the results. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetResults( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RealTimeReleaseModelsTask](topic12405.md)
    Dim ctx As [SpecificationContext](topic11149.md)
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = instance.GetResults(ctx)  
  
C#|   
---|---  
      
    
    public [ReleaseComponentsResults](topic6300.md) GetResults( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    The specification context for the active specification.

#### Return Value

The results of releasing the components.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RealTimeReleaseModelsTask Class](topic12405.md)   
[RealTimeReleaseModelsTask Members](topic12406.md)

©2024 DriveWorks Ltd. All Rights Reserved.
