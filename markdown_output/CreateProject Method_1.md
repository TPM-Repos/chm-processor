![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateProject Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic388.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IProjectService Interface](topic382.md) : CreateProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_group_
    The group in which to create the project.

_path_
    The fully qualified path to the new project file.

_additionalParameters_
    Optional additional parameters to pass to the project being created.

Glossary Item Box

Creates a new project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub CreateProject( _
       ByVal _group_ As [Group](topic2958.md), _
       ByVal _path_ As String, _
       ByVal _additionalParameters_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IProjectService](topic382.md)
    Dim group As [Group](topic2958.md)
    Dim path As String
    Dim additionalParameters As String
     
    instance.CreateProject(group, path, additionalParameters)  
  
C#|   
---|---  
      
    
    void CreateProject( 
       [Group](topic2958.md) _group_ ,
       string _path_ ,
       string _additionalParameters_
    )  
  
#### Parameters

 _group_
    The group in which to create the project.
_path_
    The fully qualified path to the new project file.
_additionalParameters_
    Optional additional parameters to pass to the project being created.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IProjectService Interface](topic382.md)   
[IProjectService Members](topic383.md)

©2024 DriveWorks Ltd. All Rights Reserved.
