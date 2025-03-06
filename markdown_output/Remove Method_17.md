![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14846.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDimensionCollection Class](topic14838.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dimension_
    The dimension to remove from the collection.

Glossary Item Box

Removes the given dimension from the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _dimension_ As [ReleasedDimension](topic14826.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDimensionCollection](topic14838.md)
    Dim dimension As [ReleasedDimension](topic14826.md)
    Dim value As Boolean
     
    value = instance.Remove(dimension)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ReleasedDimension](topic14826.md) _dimension_
    )  
  
#### Parameters

 _dimension_
    The dimension to remove from the collection.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedDimensionCollection Class](topic14838.md)   
[ReleasedDimensionCollection Members](topic14839.md)

©2024 DriveWorks Ltd. All Rights Reserved.
