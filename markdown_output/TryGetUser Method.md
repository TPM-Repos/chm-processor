       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetUser Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TryGetUser Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_loginName_
    The login name of the user to retrieve.

_userDetails_
    A variable which will receive a new instance of the [DriveWorks.Security.UserDetails](topic10740.md) type if successful.

Glossary Item Box

Gets information about the user with the specified login name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetUser( _
       ByVal _loginName_ As String, _
       ByRef _userDetails_ As [UserDetails](topic10740.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim loginName As String
    Dim userDetails As [UserDetails](topic10740.md)
    Dim value As Boolean
     
    value = instance.TryGetUser(loginName, userDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetUser( 
       string _loginName_ ,
       ref [UserDetails](topic10740.md) _userDetails_
    )  
  
#### Parameters

 _loginName_
    The login name of the user to retrieve.
_userDetails_
    A variable which will receive a new instance of the [DriveWorks.Security.UserDetails](topic10740.md) type if successful.

#### Return Value

True if the user was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


