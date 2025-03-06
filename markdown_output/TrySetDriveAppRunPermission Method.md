![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TrySetDriveAppRunPermission Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3234.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : TrySetDriveAppRunPermission Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    The unique identifier of the DriveApp to give run permissions to.

_teamId_
    The unique identifier of the team to give DriveApp run permissions to.

Glossary Item Box

Attempts to give the chosen team permission to run the chosen DriveApp. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TrySetDriveAppRunPermission( _
       ByVal _driveAppId_ As Guid, _
       ByVal _teamId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim teamId As Guid
    Dim value As Boolean
     
    value = instance.TrySetDriveAppRunPermission(driveAppId, teamId)  
  
C#|   
---|---  
      
    
    public bool TrySetDriveAppRunPermission( 
       Guid _driveAppId_ ,
       Guid _teamId_
    )  
  
#### Parameters

 _driveAppId_
    The unique identifier of the DriveApp to give run permissions to.
_teamId_
    The unique identifier of the team to give DriveApp run permissions to.

#### Return Value

True if the permission was given, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)

©2024 DriveWorks Ltd. All Rights Reserved.
