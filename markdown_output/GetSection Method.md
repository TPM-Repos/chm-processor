![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4653.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSection( _
       ByVal _sectionName_ As String, _
       ByVal _create_ As Boolean _
    ) As [ProjectMetadataSection](topic4654.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectMetadata Class](topic4647.md)   
[ProjectMetadata Members](topic4648.md)

©2024 DriveWorks Ltd. All Rights Reserved.
