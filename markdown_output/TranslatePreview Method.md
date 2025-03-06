TranslatePreview Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewHost Interface](topic7280.md) : TranslatePreview Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalResult_
    Original [EffectivePreviewResult](topic8075.md) to translate.

Glossary Item Box

Attempts to translate the given [EffectivePreviewResult](topic8075.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TranslatePreview( _
       ByVal _originalResult_ As [EffectivePreviewResult](topic8075.md) _
    ) As [EffectivePreviewResult](topic8075.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewHost Interface](topic7280.md)   
[IPreviewHost Members](topic7281.md)


