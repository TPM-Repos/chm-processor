Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMetadata Class](topic4647.md) : GetSection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sectionName_
    The name of the section to get from the project metadata file.

_create_
    Creates the metadata file if it doesn't already exist.

Glossary Item Box

Gets the specified section from the project metadata file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSection( _
       ByVal _sectionName_ As String, _
       ByVal _create_ As Boolean _
    ) As [ProjectMetadataSection](topic4654.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMetadata](topic4647.md)
    Dim sectionName As String
    Dim create As Boolean
    Dim value As [ProjectMetadataSection](topic4654.md)
     
    value = instance.GetSection(sectionName, create)  
  
C#|   
---|---  
      
    
    public [ProjectMetadataSection](topic4654.md) GetSection( 
       string _sectionName_ ,
       bool _create_
    )  
  
#### Parameters

 _sectionName_
    The name of the section to get from the project metadata file.
_create_
    Creates the metadata file if it doesn't already exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMetadata Class](topic4647.md)   
[ProjectMetadata Members](topic4648.md)


