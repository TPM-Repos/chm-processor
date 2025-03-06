![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TrackParameterRelease Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15038.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSolidWorksComponent Class](topic15029.md) : TrackParameterRelease Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tracker_
    

_parameter_
    

_value_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub TrackParameterRelease( _
       ByVal _tracker_ As [IReleaseParameterTracker](topic6113.md), _
       ByVal _parameter_ As ProjectParameterData, _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedSolidWorksComponent](topic15029.md)
    Dim tracker As [IReleaseParameterTracker](topic6113.md)
    Dim parameter As ProjectParameterData
    Dim value As String
     
    instance.TrackParameterRelease(tracker, parameter, value)  
  
C#|   
---|---  
      
    
    protected override void TrackParameterRelease( 
       [IReleaseParameterTracker](topic6113.md) _tracker_ ,
       ProjectParameterData _parameter_ ,
       string _value_
    )  
  
#### Parameters

 _tracker_
    
_parameter_
    
_value_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedSolidWorksComponent Class](topic15029.md)   
[ReleasedSolidWorksComponent Members](topic15030.md)

©2024 DriveWorks Ltd. All Rights Reserved.
