Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OpenProjectForQuery Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : OpenProjectForQuery Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectDetails_
    The details which indicate the project to open.

Glossary Item Box

Opens the specified project so that it's constants and variable information can be queried, and returns it as an System.IDisposable object. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function OpenProjectForQuery( _
       ByVal _projectDetails_ As [ProjectDetails](topic4330.md) _
    ) As [DisposableProject](topic2728.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim projectDetails As [ProjectDetails](topic4330.md)
    Dim value As [DisposableProject](topic2728.md)
     
    value = instance.OpenProjectForQuery(projectDetails)  
  
C#|   
---|---  
      
    
    public [DisposableProject](topic2728.md) OpenProjectForQuery( 
       [ProjectDetails](topic4330.md) _projectDetails_
    )  
  
#### Parameters

 _projectDetails_
    The details which indicate the project to open.

#### Return Value

An instance of the [DisposableProject](topic2728.md) class.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


