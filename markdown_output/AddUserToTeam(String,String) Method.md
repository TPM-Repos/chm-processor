Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddUserToTeam(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [AddUserToTeam Method](topic3289.md) : AddUserToTeam(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamName_
    The name of the team to which to add the user.

_loginName_
    The login name of the user to add to the team.

Glossary Item Box

Adds the specified user to the given team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddUserToTeam( _
       ByVal _teamName_ As String, _
       ByVal _loginName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamName As String
    Dim loginName As String
    Dim value As Boolean
     
    value = instance.AddUserToTeam(teamName, loginName)  
  
C#|   
---|---  
      
    
    public bool AddUserToTeam( 
       string _teamName_ ,
       string _loginName_
    )  
  
#### Parameters

 _teamName_
    The name of the team to which to add the user.
_loginName_
    The login name of the user to add to the team.

#### Return Value

True if both the user and the team were found, and the user was added to the team.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3289.md)


