TeamHasDriveAppRunPermission Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : TeamHasDriveAppRunPermission Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    The unique identifier of the DriveApp to check run permissions for.

_teamId_
    The unique identifier of the team to check permissions for.

Glossary Item Box

Gets whether or not the chosen team has run permissions for a DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TeamHasDriveAppRunPermission( _
       ByVal _driveAppId_ As Guid, _
       ByVal _teamId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim teamId As Guid
    Dim value As Boolean
     
    value = instance.TeamHasDriveAppRunPermission(driveAppId, teamId)  
  
C#|   
---|---  
      
    
    public bool TeamHasDriveAppRunPermission( 
       Guid _driveAppId_ ,
       Guid _teamId_
    )  
  
#### Parameters

 _driveAppId_
    The unique identifier of the DriveApp to check run permissions for.
_teamId_
    The unique identifier of the team to check permissions for.

#### Return Value

True if the chosen team has run permissions for the DriveApp, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


