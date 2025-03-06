       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetImageMode Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetImageMode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isImageModeEnabled_
    Whether we are in image mode or not.

Glossary Item Box

Sets image mode on the control 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetImageMode( _
       ByVal _isImageModeEnabled_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim isImageModeEnabled As Boolean
     
    instance.SetImageMode(isImageModeEnabled)  
  
C#|   
---|---  
      
    
    void SetImageMode( 
       bool _isImageModeEnabled_
    )  
  
#### Parameters

 _isImageModeEnabled_
    Whether we are in image mode or not.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


