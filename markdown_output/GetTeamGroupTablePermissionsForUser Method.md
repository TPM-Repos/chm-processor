Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionsForUser Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionsForUser Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userId_
    The unique identifier of the user to fetch the permissions for.

Glossary Item Box

Returns a collection of group data table permissions that the specified user has. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionsForUser( _
       ByVal _userId_ As Guid _
    ) As [TeamGroupTablePermission()](topic10718.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim userId As Guid
    Dim value() As [TeamGroupTablePermission](topic10718.md)
     
    value = instance.GetTeamGroupTablePermissionsForUser(userId)  
  
C#|   
---|---  
      
    
    public [TeamGroupTablePermission[]](topic10718.md) GetTeamGroupTablePermissionsForUser( 
       Guid _userId_
    )  
  
#### Parameters

 _userId_
    The unique identifier of the user to fetch the permissions for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


