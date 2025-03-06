![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetGroupTablePermissionForTeam Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3323.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : SetGroupTablePermissionForTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to set the permissions for.

_groupTableId_
    The unique identifier of the group table to set the permissions of.

_permission_
    The permissions to set for the specified team and group data table.

Glossary Item Box

Sets the specified permissions for the specified team and group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetGroupTablePermissionForTeam( _
       ByVal _teamId_ As Guid, _
       ByVal _groupTableId_ As Guid, _
       ByVal _permission_ As [GroupTablePermission](topic10616.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim groupTableId As Guid
    Dim permission As [GroupTablePermission](topic10616.md)
     
    instance.SetGroupTablePermissionForTeam(teamId, groupTableId, permission)  
  
C#|   
---|---  
      
    
    public void SetGroupTablePermissionForTeam( 
       Guid _teamId_ ,
       Guid _groupTableId_ ,
       [GroupTablePermission](topic10616.md) _permission_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to set the permissions for.
_groupTableId_
    The unique identifier of the group table to set the permissions of.
_permission_
    The permissions to set for the specified team and group data table.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
