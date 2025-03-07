Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddUserToTeam(Guid,Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [AddUserToTeam Method](topic3289.md) : AddUserToTeam(Guid,Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to which to add the user.

_userId_
    The unique identifier of the user to add to the team.

Glossary Item Box

Adds the specified user to the given team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddUserToTeam( _
       ByVal _teamId_ As Guid, _
       ByVal _userId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim userId As Guid
    Dim value As Boolean
     
    value = instance.AddUserToTeam(teamId, userId)  
  
C#|   
---|---  
      
    
    public bool AddUserToTeam( 
       Guid _teamId_ ,
       Guid _userId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to which to add the user.
_userId_
    The unique identifier of the user to add to the team.

#### Return Value

True if both the user and the team were found, and the user was added to the team.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3289.md)


