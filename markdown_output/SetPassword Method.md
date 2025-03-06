SetPassword Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [DriveWorksCredentials Class](topic10669.md) : SetPassword Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_password_
    The password to hash and store.

_preservePassword_
    True to store the password, false to discard it after the hash has been computed.

Glossary Item Box

Hashes and stores the given password. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetPassword( _
       ByVal _password_ As String, _
       ByVal _preservePassword_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DriveWorksCredentials](topic10669.md)
    Dim password As String
    Dim preservePassword As Boolean
     
    instance.SetPassword(password, preservePassword)  
  
C#|   
---|---  
      
    
    public void SetPassword( 
       string _password_ ,
       bool _preservePassword_
    )  
  
#### Parameters

 _password_
    The password to hash and store.
_preservePassword_
    True to store the password, false to discard it after the hash has been computed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorksCredentials Class](topic10669.md)   
[DriveWorksCredentials Members](topic10670.md)


