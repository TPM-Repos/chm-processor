       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetMenuEnabled Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic373.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IPreviewControl Interface](topic362.md) : SetMenuEnabled Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isEnabled_
    Whether or not the control is visible.

Glossary Item Box

Sets the visibility of the preview control menu. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SetMenuEnabled( _
       ByVal _isEnabled_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewControl](topic362.md)
    Dim isEnabled As Boolean
     
    instance.SetMenuEnabled(isEnabled)  
  
C#|   
---|---  
      
    
    void SetMenuEnabled( 
       bool _isEnabled_
    )  
  
#### Parameters

 _isEnabled_
    Whether or not the control is visible.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewControl Interface](topic362.md)   
[IPreviewControl Members](topic363.md)

©2024 DriveWorks Ltd. All Rights Reserved.
