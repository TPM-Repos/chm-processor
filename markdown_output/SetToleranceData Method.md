![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetToleranceData Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14833.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimension Class](topic14826.md) : SetToleranceData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The tolerance type.

_lower_
    The lower tolerance value.

_upper_
    The upper tolerance value.

Glossary Item Box

Sets the tolerance data for the dimension, creating it if it doesn't already exist. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetToleranceData( _
       ByVal _type_ As Integer, _
       ByVal _lower_ As Double, _
       ByVal _upper_ As Double _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimension](topic14826.md)
    Dim type As Integer
    Dim lower As Double
    Dim upper As Double
     
    instance.SetToleranceData(type, lower, upper)  
  
C#|   
---|---  
      
    
    public void SetToleranceData( 
       int _type_ ,
       double _lower_ ,
       double _upper_
    )  
  
#### Parameters

 _type_
    The tolerance type.
_lower_
    The lower tolerance value.
_upper_
    The upper tolerance value.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedDimension Class](topic14826.md)   
[ReleasedDimension Members](topic14827.md)

©2024 DriveWorks Ltd. All Rights Reserved.
