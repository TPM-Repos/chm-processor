       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetProjectMetadataValueByName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3225.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : SetProjectMetadataValueByName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    The id of the project that the metadata entry belongs to.

_metadataName_
    The name of the metadata entry to update.

_metadataValue_
    The value to set.

Glossary Item Box

Sets the value of a project's metadata entry with the specified value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function SetProjectMetadataValueByName( _
       ByVal _projectId_ As Guid, _
       ByVal _metadataName_ As String, _
       ByVal _metadataValue_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim metadataName As String
    Dim metadataValue As String
    Dim value As Boolean
     
    value = instance.SetProjectMetadataValueByName(projectId, metadataName, metadataValue)  
  
C#|   
---|---  
      
    
    public bool SetProjectMetadataValueByName( 
       Guid _projectId_ ,
       string _metadataName_ ,
       string _metadataValue_
    )  
  
#### Parameters

 _projectId_
    The id of the project that the metadata entry belongs to.
_metadataName_
    The name of the metadata entry to update.
_metadataValue_
    The value to set.

#### Return Value

True if the new value was set successfully.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)

©2024 DriveWorks Ltd. All Rights Reserved.
