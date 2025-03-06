       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDefaultRotationZoom Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetDefaultRotationZoom Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_defaultRotationZoom_
    The default rotation and zoom.

Glossary Item Box

Sets the default rotation and zoom of the preview control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetDefaultRotationZoom( _
       ByVal _defaultRotationZoom_ As DriveWorks.Support.RotationZoom _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim defaultRotationZoom As DriveWorks.Support.RotationZoom
     
    instance.SetDefaultRotationZoom(defaultRotationZoom)  
  
C#|   
---|---  
      
    
    void SetDefaultRotationZoom( 
       DriveWorks.Support.RotationZoom _defaultRotationZoom_
    )  
  
#### Parameters

 _defaultRotationZoom_
    The default rotation and zoom.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


