Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateUser(String,Boolean,String,String,Boolean,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [CreateUser Method](topic3299.md) : CreateUser(String,Boolean,String,String,Boolean,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_loginName_
    The login name of the user.

_isEnabled_
    

_emailAddress_
    The email address of the user.

_displayName_
    The display name for the user.

_isTeamLeader_
    Specifies if the user is a team leader.

_password_
    The password to give to the user.

Glossary Item Box

Creates a new user with the specified information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateUser( _
       ByVal _loginName_ As String, _
       ByVal _isEnabled_ As Boolean, _
       ByVal _emailAddress_ As String, _
       ByVal _displayName_ As String, _
       ByVal _isTeamLeader_ As Boolean, _
       ByVal _password_ As String _
    ) As [UserDetails](topic10740.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim loginName As String
    Dim isEnabled As Boolean
    Dim emailAddress As String
    Dim displayName As String
    Dim isTeamLeader As Boolean
    Dim password As String
    Dim value As [UserDetails](topic10740.md)
     
    value = instance.CreateUser(loginName, isEnabled, emailAddress, displayName, isTeamLeader, password)  
  
C#|   
---|---  
      
    
    public [UserDetails](topic10740.md) CreateUser( 
       string _loginName_ ,
       bool _isEnabled_ ,
       string _emailAddress_ ,
       string _displayName_ ,
       bool _isTeamLeader_ ,
       string _password_
    )  
  
#### Parameters

 _loginName_
    The login name of the user.
_isEnabled_
    
_emailAddress_
    The email address of the user.
_displayName_
    The display name for the user.
_isTeamLeader_
    Specifies if the user is a team leader.
_password_
    The password to give to the user.

#### Return Value

An instance of the [DriveWorks.Security.UserDetails](topic10740.md) structure containing information about the newly created user.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3299.md)


