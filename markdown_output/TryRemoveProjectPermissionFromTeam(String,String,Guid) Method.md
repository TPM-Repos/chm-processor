TryRemoveProjectPermissionFromTeam(String,String,Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [TryRemoveProjectPermissionFromTeam Method](topic3333.md) : TryRemoveProjectPermissionFromTeam(String,String,Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamName_
    The name of the team to modify.

_projectName_
    The name of the project from which to remove access.

_permissionId_
    The unique identifier of the permission.

Glossary Item Box

Removes the specified project from the list of projects to which users in the given team have access. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryRemoveProjectPermissionFromTeam( _
       ByVal _teamName_ As String, _
       ByVal _projectName_ As String, _
       ByVal _permissionId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamName As String
    Dim projectName As String
    Dim permissionId As Guid
    Dim value As Boolean
     
    value = instance.TryRemoveProjectPermissionFromTeam(teamName, projectName, permissionId)  
  
C#|   
---|---  
      
    
    public bool TryRemoveProjectPermissionFromTeam( 
       string _teamName_ ,
       string _projectName_ ,
       Guid _permissionId_
    )  
  
#### Parameters

 _teamName_
    The name of the team to modify.
_projectName_
    The name of the project from which to remove access.
_permissionId_
    The unique identifier of the permission.

#### Return Value

True if both the team and the project were found, and the project permission list was updated successfully, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3333.md)


