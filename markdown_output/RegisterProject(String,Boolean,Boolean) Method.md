Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterProject(String,Boolean,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [RegisterProject Method](topic3218.md) : RegisterProject(String,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectPath_
    The path to the project file.

_hidden_
    True if the project is hidden, see [ProjectDetails.Hidden](topic4343.md) for more information.

_deployed_
    True if the project is deployed, see [ProjectDetails.Deployed](topic4340.md) for more information.

Glossary Item Box

Registers a new project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterProject( _
       ByVal _projectPath_ As String, _
       ByVal _hidden_ As Boolean, _
       ByVal _deployed_ As Boolean _
    ) As [ProjectDetails](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectPath As String
    Dim hidden As Boolean
    Dim deployed As Boolean
    Dim value As [ProjectDetails](topic4330.md)
     
    value = instance.RegisterProject(projectPath, hidden, deployed)  
  
C#|   
---|---  
      
    
    public [ProjectDetails](topic4330.md) RegisterProject( 
       string _projectPath_ ,
       bool _hidden_ ,
       bool _deployed_
    )  
  
#### Parameters

 _projectPath_
    The path to the project file.
_hidden_
    True if the project is hidden, see [ProjectDetails.Hidden](topic4343.md) for more information.
_deployed_
    True if the project is deployed, see [ProjectDetails.Deployed](topic4340.md) for more information.

#### Return Value

An instance of the [ProjectDetails](topic4330.md) type representing the newly registered project.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3218.md)


