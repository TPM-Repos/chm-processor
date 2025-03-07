Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionsForTeam Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionsForTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to get the permissions for.

Glossary Item Box

Returns a collection permissions that the specified team has for group tables. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionsForTeam( _
       ByVal _teamId_ As Guid _
    ) As [TeamGroupTablePermission()](topic10718.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim value() As [TeamGroupTablePermission](topic10718.md)
     
    value = instance.GetTeamGroupTablePermissionsForTeam(teamId)  
  
C#|   
---|---  
      
    
    public [TeamGroupTablePermission[]](topic10718.md) GetTeamGroupTablePermissionsForTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to get the permissions for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


