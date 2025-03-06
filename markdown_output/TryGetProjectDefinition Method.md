TryGetProjectDefinition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : TryGetProjectDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectName_
    

_projectDef_
    

Glossary Item Box

Gets the project definition for a specific child specification project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetProjectDefinition( _
       ByVal _projectName_ As String, _
       ByRef _projectDef_ As [ProjectChildSpecificationProjectDef](topic4067.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim projectName As String
    Dim projectDef As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim value As Boolean
     
    value = instance.TryGetProjectDefinition(projectName, projectDef)  
  
C#|   
---|---  
      
    
    public bool TryGetProjectDefinition( 
       string _projectName_ ,
       ref [ProjectChildSpecificationProjectDef](topic4067.md) _projectDef_
    )  
  
#### Parameters

 _projectName_
    
_projectDef_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


