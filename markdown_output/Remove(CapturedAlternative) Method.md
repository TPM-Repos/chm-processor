![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(CapturedAlternative) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14050.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAlternativeCollection Class](topic14039.md) > [Remove Method](topic14048.md) : Remove(CapturedAlternative) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_alternative_
    The alternative to remove from the collection.

Glossary Item Box

Removes the given alternative from the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _alternative_ As [CapturedAlternative](topic14031.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedAlternativeCollection](topic14039.md)
    Dim alternative As [CapturedAlternative](topic14031.md)
    Dim value As Boolean
     
    value = instance.Remove(alternative)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [CapturedAlternative](topic14031.md) _alternative_
    )  
  
#### Parameters

 _alternative_
    The alternative to remove from the collection.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedAlternativeCollection Class](topic14039.md)   
[CapturedAlternativeCollection Members](topic14040.md)   
[Overload List](topic14048.md)

©2024 DriveWorks Ltd. All Rights Reserved.
