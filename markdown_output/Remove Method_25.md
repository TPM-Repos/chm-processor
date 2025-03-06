![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15086.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedViewDimensionCollection Class](topic15078.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dimension_
    The dimension to remove.

Glossary Item Box

Removes the given dimension. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Remove( _
       ByVal _dimension_ As [ReleasedViewDimension](topic15069.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedViewDimensionCollection](topic15078.md)
    Dim dimension As [ReleasedViewDimension](topic15069.md)
     
    instance.Remove(dimension)  
  
C#|   
---|---  
      
    
    public void Remove( 
       [ReleasedViewDimension](topic15069.md) _dimension_
    )  
  
#### Parameters

 _dimension_
    The dimension to remove.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedViewDimensionCollection Class](topic15078.md)   
[ReleasedViewDimensionCollection Members](topic15079.md)

©2024 DriveWorks Ltd. All Rights Reserved.
