SetLighting Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetLighting Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_presetName_
    The name of the lighting preset to use.

Glossary Item Box

Sets the Lighting preset to load. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetLighting( _
       ByVal _presetName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim presetName As String
     
    instance.SetLighting(presetName)  
  
C#|   
---|---  
      
    
    void SetLighting( 
       string _presetName_
    )  
  
#### Parameters

 _presetName_
    The name of the lighting preset to use.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)


