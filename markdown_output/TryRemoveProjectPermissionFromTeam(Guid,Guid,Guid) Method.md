![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryRemoveProjectPermissionFromTeam(Guid,Guid,Guid) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3334.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [TryRemoveProjectPermissionFromTeam Method](topic3333.md) : TryRemoveProjectPermissionFromTeam(Guid,Guid,Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to modify.

_projectId_
    The unique identifier of the project from which to remove access.

_permissionId_
    The unique identifier of the permission.

Glossary Item Box

Removes the specified project from the list of projects to which users in the given team have access. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryRemoveProjectPermissionFromTeam( _
       ByVal _teamId_ As Guid, _
       ByVal _projectId_ As Guid, _
       ByVal _permissionId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim projectId As Guid
    Dim permissionId As Guid
    Dim value As Boolean
     
    value = instance.TryRemoveProjectPermissionFromTeam(teamId, projectId, permissionId)  
  
C#|   
---|---  
      
    
    public bool TryRemoveProjectPermissionFromTeam( 
       Guid _teamId_ ,
       Guid _projectId_ ,
       Guid _permissionId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to modify.
_projectId_
    The unique identifier of the project from which to remove access.
_permissionId_
    The unique identifier of the permission.

#### Return Value

True if both the team and the project were found, and the project permission list was updated successfully, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3333.md)

©2024 DriveWorks Ltd. All Rights Reserved.
