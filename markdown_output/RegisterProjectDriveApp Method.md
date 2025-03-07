Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterProjectDriveApp Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : RegisterProjectDriveApp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_projectId_
    

_driveAppId_
    

Glossary Item Box

Create a link between the Project and DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RegisterProjectDriveApp( _
       ByVal _projectId_ As Guid, _
       ByVal _driveAppId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim projectId As Guid
    Dim driveAppId As Guid
     
    instance.RegisterProjectDriveApp(projectId, driveAppId)  
  
C#|   
---|---  
      
    
    public void RegisterProjectDriveApp( 
       Guid _projectId_ ,
       Guid _driveAppId_
    )  
  
#### Parameters

 _projectId_
    
_driveAppId_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


