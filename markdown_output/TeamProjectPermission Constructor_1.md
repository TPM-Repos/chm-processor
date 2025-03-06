TeamProjectPermission Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [TeamProjectPermission Class](topic10729.md) : TeamProjectPermission Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to which the permission applies.

_projectId_
    The unique identifier of the project to which permission is given.

_permissionId_
    The unique identifier of the permission which is enabled, generally one of the values from [StandardProjectPermissions](topic10695.md).

Glossary Item Box

Initializes a new instance of the [TeamProjectPermission](topic10729.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _teamId_ As Guid, _
       ByVal _projectId_ As Guid, _
       ByVal _permissionId_ As Guid _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim teamId As Guid
    Dim projectId As Guid
    Dim permissionId As Guid
     
    Dim instance As New [TeamProjectPermission](topic10729.md)(teamId, projectId, permissionId)  
  
C#|   
---|---  
      
    
    public TeamProjectPermission( 
       Guid _teamId_ ,
       Guid _projectId_ ,
       Guid _permissionId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to which the permission applies.
_projectId_
    The unique identifier of the project to which permission is given.
_permissionId_
    The unique identifier of the permission which is enabled, generally one of the values from [StandardProjectPermissions](topic10695.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TeamProjectPermission Class](topic10729.md)   
[TeamProjectPermission Members](topic10730.md)


