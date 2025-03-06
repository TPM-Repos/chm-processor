       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetOrthographic Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetOrthographic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isOrthographic_
    Whether the default camera should be orthographic

Glossary Item Box

Sets the default camera projection mode 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetOrthographic( _
       ByVal _isOrthographic_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim isOrthographic As Boolean
     
    instance.SetOrthographic(isOrthographic)  
  
C#|   
---|---  
      
    
    void SetOrthographic( 
       bool _isOrthographic_
    )  
  
#### Parameters

 _isOrthographic_
    Whether the default camera should be orthographic

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


