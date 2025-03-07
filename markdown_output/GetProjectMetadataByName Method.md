Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectMetadataByName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : GetProjectMetadataByName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    The id of the project that the metadata entry belongs to.

_metadataName_
    The name of the metadata entry.

Glossary Item Box

Gets the metadata entry with the specified name that belongs to the provided project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectMetadataByName( _
       ByVal _projectId_ As Guid, _
       ByVal _metadataName_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim metadataName As String
    Dim value As String
     
    value = instance.GetProjectMetadataByName(projectId, metadataName)  
  
C#|   
---|---  
      
    
    public string GetProjectMetadataByName( 
       Guid _projectId_ ,
       string _metadataName_
    )  
  
#### Parameters

 _projectId_
    The id of the project that the metadata entry belongs to.
_metadataName_
    The name of the metadata entry.

#### Return Value

The value of the metadata entry.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


