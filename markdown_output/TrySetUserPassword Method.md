TrySetUserPassword Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TrySetUserPassword Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_loginName_
    The login name of the user.

_newPassword_
    The new password to apply to the user.

Glossary Item Box

Updates an existing user with the specified information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TrySetUserPassword( _
       ByVal _loginName_ As String, _
       ByVal _newPassword_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim loginName As String
    Dim newPassword As String
    Dim value As Boolean
     
    value = instance.TrySetUserPassword(loginName, newPassword)  
  
C#|   
---|---  
      
    
    public bool TrySetUserPassword( 
       string _loginName_ ,
       string _newPassword_
    )  
  
#### Parameters

 _loginName_
    The login name of the user.
_newPassword_
    The new password to apply to the user.

#### Return Value

True if the user is found and updated, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


