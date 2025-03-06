       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdatePreviewPath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3268.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : TryUpdatePreviewPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The Id of the released component for which to update the path.

_newPreviewPath_
    The full path to the preview file.

Glossary Item Box

Updates the path to the preview file created for the specified component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdatePreviewPath( _
       ByVal _componentId_ As Guid, _
       ByVal _newPreviewPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim newPreviewPath As String
    Dim value As Boolean
     
    value = instance.TryUpdatePreviewPath(componentId, newPreviewPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdatePreviewPath( 
       Guid _componentId_ ,
       string _newPreviewPath_
    )  
  
#### Parameters

 _componentId_
    The Id of the released component for which to update the path.
_newPreviewPath_
    The full path to the preview file.

#### Return Value

True if the path was successfully updated, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
