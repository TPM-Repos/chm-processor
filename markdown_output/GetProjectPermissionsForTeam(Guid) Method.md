Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectPermissionsForTeam(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetProjectPermissionsForTeam Method](topic3301.md) : GetProjectPermissionsForTeam(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team.

Glossary Item Box

Gets the list of project permissions for the specified team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetProjectPermissionsForTeam( _
       ByVal _teamId_ As Guid _
    ) As [TeamProjectPermission()](topic10729.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim value() As [TeamProjectPermission](topic10729.md)
     
    value = instance.GetProjectPermissionsForTeam(teamId)  
  
C#|   
---|---  
      
    
    public [TeamProjectPermission[]](topic10729.md) GetProjectPermissionsForTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team.

#### Return Value

An array of instances of the [DriveWorks.Security.TeamProjectPermission](topic10729.md) type for the project permissions.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3301.md)


