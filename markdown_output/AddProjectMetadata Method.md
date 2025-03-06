![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddProjectMetadata Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : AddProjectMetadata Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The id of the metadata.

_projectId_
    The id of the project to create a metadata for.

_metadataName_
    The name of the metadata entry.

_metadataValue_
    The value of the metadata entry.

_isReadOnly_
    Whether or not the metadata value can be changed after creation.

Glossary Item Box

Creates a metadata entry for the provided project in the form of a key/value pair. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddProjectMetadata( _
       ByVal _id_ As Guid, _
       ByVal _projectId_ As Guid, _
       ByVal _metadataName_ As String, _
       ByVal _metadataValue_ As String, _
       ByVal _isReadOnly_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim id As Guid
    Dim projectId As Guid
    Dim metadataName As String
    Dim metadataValue As String
    Dim isReadOnly As Boolean
    Dim value As Boolean
     
    value = instance.AddProjectMetadata(id, projectId, metadataName, metadataValue, isReadOnly)  
  
C#|   
---|---  
      
    
    public bool AddProjectMetadata( 
       Guid _id_ ,
       Guid _projectId_ ,
       string _metadataName_ ,
       string _metadataValue_ ,
       bool _isReadOnly_
    )  
  
#### Parameters

 _id_
    The id of the metadata.
_projectId_
    The id of the project to create a metadata for.
_metadataName_
    The name of the metadata entry.
_metadataValue_
    The value of the metadata entry.
_isReadOnly_
    Whether or not the metadata value can be changed after creation.

#### Return Value

True if the metadata entry was created successfully.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


