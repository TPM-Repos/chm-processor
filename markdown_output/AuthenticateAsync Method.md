Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AuthenticateAsync Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [IAuthenticationProviderAsync Interface](topic10582.md) : AuthenticateAsync Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_credentials_
    The credentials to authenticate.

Glossary Item Box

Authenticates the given credentials and returns the relevant principal. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AuthenticateAsync( _
       ByVal _credentials_ As [IProviderCredentials](topic10588.md) _
    ) As Task(Of IProviderPrincipal)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAuthenticationProviderAsync](topic10582.md)
    Dim credentials As [IProviderCredentials](topic10588.md)
    Dim value As Task(Of IProviderPrincipal)
     
    value = instance.AuthenticateAsync(credentials)  
  
C#|   
---|---  
      
    
    Task<IProviderPrincipal> AuthenticateAsync( 
       [IProviderCredentials](topic10588.md) _credentials_
    )  
  
#### Parameters

 _credentials_
    The credentials to authenticate.

#### Return Value

An instance of a type derived from [IProviderPrincipal](topic10597.md) which represents the authenticated principal, or a null reference if the credentials are invalid.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAuthenticationProviderAsync Interface](topic10582.md)   
[IAuthenticationProviderAsync Members](topic10583.md)


