![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TranslatePreview Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7285.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewHost Interface](topic7280.md) : TranslatePreview Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalResult_
    Original [EffectivePreviewResult](topic8075.md) to translate.

Glossary Item Box

Attempts to translate the given [EffectivePreviewResult](topic8075.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TranslatePreview( _
       ByVal _originalResult_ As [EffectivePreviewResult](topic8075.md) _
    ) As [EffectivePreviewResult](topic8075.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IPreviewHost](topic7280.md)
    Dim originalResult As [EffectivePreviewResult](topic8075.md)
    Dim value As [EffectivePreviewResult](topic8075.md)
     
    value = instance.TranslatePreview(originalResult)  
  
C#|   
---|---  
      
    
    [EffectivePreviewResult](topic8075.md) TranslatePreview( 
       [EffectivePreviewResult](topic8075.md) _originalResult_
    )  
  
#### Parameters

 _originalResult_
    Original [EffectivePreviewResult](topic8075.md) to translate.

#### Return Value

A translated version of the given [EffectivePreviewResult](topic8075.md) if translation was successful; otherwise returns a null reference (or Nothing in Visual Basic).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewHost Interface](topic7280.md)   
[IPreviewHost Members](topic7281.md)

©2024 DriveWorks Ltd. All Rights Reserved.
