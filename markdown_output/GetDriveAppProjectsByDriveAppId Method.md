Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDriveAppProjectsByDriveAppId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : GetDriveAppProjectsByDriveAppId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    

Glossary Item Box

Gets all Projects linked to a DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetDriveAppProjectsByDriveAppId( _
       ByVal _driveAppId_ As Guid _
    ) As [ProjectDetails()](topic4330.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim value() As [ProjectDetails](topic4330.md)
     
    value = instance.GetDriveAppProjectsByDriveAppId(driveAppId)  
  
C#|   
---|---  
      
    
    public [ProjectDetails[]](topic4330.md) GetDriveAppProjectsByDriveAppId( 
       Guid _driveAppId_
    )  
  
#### Parameters

 _driveAppId_
    

# Remarks

This method will return a project even if the current user doesn't have access to them.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


