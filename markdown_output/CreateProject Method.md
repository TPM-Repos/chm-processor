Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateProject Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IProjectTemplateHelper Interface](topic2091.md) : CreateProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_pcd_
    The project creation data which describe the project to be created.

Glossary Item Box

Creates the project based on the template. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub CreateProject( _
       ByVal _pcd_ As [ProjectCreationData](topic2132.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProjectTemplateHelper](topic2091.md)
    Dim pcd As [ProjectCreationData](topic2132.md)
     
    instance.CreateProject(pcd)  
  
C#|   
---|---  
      
    
    void CreateProject( 
       [ProjectCreationData](topic2132.md) _pcd_
    )  
  
#### Parameters

 _pcd_
    The project creation data which describe the project to be created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProjectTemplateHelper Interface](topic2091.md)   
[IProjectTemplateHelper Members](topic2092.md)


