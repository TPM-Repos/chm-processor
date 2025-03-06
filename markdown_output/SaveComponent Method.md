       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SaveComponent Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3048.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) : SaveComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_component_
    The component to save to the group.

Glossary Item Box

Saves a new or existing component to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SaveComponent( _
       ByVal _component_ As [CapturedComponent](topic6147.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim component As [CapturedComponent](topic6147.md)
     
    instance.SaveComponent(component)  
  
C#|   
---|---  
      
    
    public void SaveComponent( 
       [CapturedComponent](topic6147.md) _component_
    )  
  
#### Parameters

 _component_
    The component to save to the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)

©2024 DriveWorks Ltd. All Rights Reserved.
