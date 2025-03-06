TranslatePreview Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [IPreviewTranslator Interface](topic7296.md) : TranslatePreview Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_desiredExtension_
    Extension of the file type the [EffectivePreviewResult](topic8075.md) should be translated to.

_originalResult_
    Original [EffectivePreviewResult](topic8075.md) that is to be translated.

Glossary Item Box

Attempts to translate the given [EffectivePreviewResult](topic8075.md). See remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TranslatePreview( _
       ByVal _desiredExtension_ As String, _
       ByVal _originalResult_ As [EffectivePreviewResult](topic8075.md) _
    ) As [EffectivePreviewResult](topic8075.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewTranslator](topic7296.md)
    Dim desiredExtension As String
    Dim originalResult As [EffectivePreviewResult](topic8075.md)
    Dim value As [EffectivePreviewResult](topic8075.md)
     
    value = instance.TranslatePreview(desiredExtension, originalResult)  
  
C#|   
---|---  
      
    
    [EffectivePreviewResult](topic8075.md) TranslatePreview( 
       string _desiredExtension_ ,
       [EffectivePreviewResult](topic8075.md) _originalResult_
    )  
  
#### Parameters

 _desiredExtension_
    Extension of the file type the [EffectivePreviewResult](topic8075.md) should be translated to.
_originalResult_
    Original [EffectivePreviewResult](topic8075.md) that is to be translated.

#### Return Value

A version of the given [EffectivePreviewResult](topic8075.md) translated to the desired type if successful; otherwise returns a null reference (Nothing in Visual Basic).

# Remarks

If the desired extension is not supported by the translator, then a null reference (Nothing in Visual Basic) will be returned and the translator will not attempt to translate the given [EffectivePreviewResult](topic8075.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewTranslator Interface](topic7296.md)   
[IPreviewTranslator Members](topic7297.md)


