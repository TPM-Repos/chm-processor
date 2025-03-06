SetPreview Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetPreview Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_preview_
    The preview object to render.

Glossary Item Box

Gives the previewer a preview object to render. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetPreview( _
       ByVal _preview_ As IDisposable _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim preview As IDisposable
     
    instance.SetPreview(preview)  
  
C#|   
---|---  
      
    
    void SetPreview( 
       IDisposable _preview_
    )  
  
#### Parameters

 _preview_
    The preview object to render.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


