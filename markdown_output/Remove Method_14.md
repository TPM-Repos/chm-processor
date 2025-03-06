![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14764.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedAnnotationCollection Class](topic14756.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_annotation_
    The annotation to remove.

Glossary Item Box

Removes the given annotation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Remove( _
       ByVal _annotation_ As [ReleasedAnnotation](topic14746.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReleasedAnnotationCollection](topic14756.md)
    Dim annotation As [ReleasedAnnotation](topic14746.md)
     
    instance.Remove(annotation)  
  
C#|   
---|---  
      
    
    public void Remove( 
       [ReleasedAnnotation](topic14746.md) _annotation_
    )  
  
#### Parameters

 _annotation_
    The annotation to remove.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleasedAnnotationCollection Class](topic14756.md)   
[ReleasedAnnotationCollection Members](topic14757.md)

©2024 DriveWorks Ltd. All Rights Reserved.
