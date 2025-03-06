![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddProjectDefinition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : AddProjectDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectName_
    The name of the project that this definition will represent.

Glossary Item Box

Creates a new [ProjectChildSpecificationProjectDef](topic4067.md) instance and adds it to this [ProjectChildSpecificationDef](topic4019.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddProjectDefinition( _
       ByVal _projectName_ As String _
    ) As [ProjectChildSpecificationProjectDef](topic4067.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim projectName As String
    Dim value As [ProjectChildSpecificationProjectDef](topic4067.md)
     
    value = instance.AddProjectDefinition(projectName)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationProjectDef](topic4067.md) AddProjectDefinition( 
       string _projectName_
    )  
  
#### Parameters

 _projectName_
    The name of the project that this definition will represent.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


