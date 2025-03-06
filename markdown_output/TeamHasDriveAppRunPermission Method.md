![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TeamHasDriveAppRunPermission Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3226.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TeamHasDriveAppRunPermission( _
       ByVal _driveAppId_ As Guid, _
       ByVal _teamId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)

©2024 DriveWorks Ltd. All Rights Reserved.
