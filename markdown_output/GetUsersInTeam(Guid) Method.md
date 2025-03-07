Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUsersInTeam(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetUsersInTeam Method](topic3316.md) : GetUsersInTeam(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to check.

Glossary Item Box

Gets all the users that belong to the specified team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetUsersInTeam( _
       ByVal _teamId_ As Guid _
    ) As [UserDetails()](topic10740.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim value() As [UserDetails](topic10740.md)
     
    value = instance.GetUsersInTeam(teamId)  
  
C#|   
---|---  
      
    
    public [UserDetails[]](topic10740.md) GetUsersInTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to check.

#### Return Value

An array of users.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3316.md)


