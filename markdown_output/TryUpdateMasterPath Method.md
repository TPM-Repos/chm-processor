       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateMasterPath Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3267.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : TryUpdateMasterPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_originalPath_
    The original path.

_newPath_
    The new path.

Glossary Item Box

Tries to update the master path of all released components matching the specified master path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateMasterPath( _
       ByVal _originalPath_ As String, _
       ByVal _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim originalPath As String
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryUpdateMasterPath(originalPath, newPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdateMasterPath( 
       string _originalPath_ ,
       string _newPath_
    )  
  
#### Parameters

 _originalPath_
    The original path.
_newPath_
    The new path.

#### Return Value

True if the master path was successfully updated. False if we failed to update anything.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
