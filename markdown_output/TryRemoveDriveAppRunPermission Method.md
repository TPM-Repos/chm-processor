       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryRemoveDriveAppRunPermission Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : TryRemoveDriveAppRunPermission Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    The unique identifier of the DriveApp to remove run permissions for.

_teamId_
    The unique identifier of the team to remove DriveApp run permissions from.

Glossary Item Box

Attempts to remove run permissions for a DriveApp from the chosen team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryRemoveDriveAppRunPermission( _
       ByVal _driveAppId_ As Guid, _
       ByVal _teamId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim teamId As Guid
    Dim value As Boolean
     
    value = instance.TryRemoveDriveAppRunPermission(driveAppId, teamId)  
  
C#|   
---|---  
      
    
    public bool TryRemoveDriveAppRunPermission( 
       Guid _driveAppId_ ,
       Guid _teamId_
    )  
  
#### Parameters

 _driveAppId_
    The unique identifier of the DriveApp to remove run permissions for.
_teamId_
    The unique identifier of the team to remove DriveApp run permissions from.

#### Return Value

True if the permission was removed, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


