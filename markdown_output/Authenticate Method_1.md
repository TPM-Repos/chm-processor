Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Authenticate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AzureAuthenticationProvider Class](topic10634.md) : Authenticate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_credentials_
    The [AzureCredentials](topic10646.md) to authenticate.

Glossary Item Box

Authenticates [AzureCredentials](topic10646.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Authenticate( _
       ByVal _credentials_ As [IProviderCredentials](topic10588.md) _
    ) As [IProviderPrincipal](topic10597.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AzureAuthenticationProvider](topic10634.md)
    Dim credentials As [IProviderCredentials](topic10588.md)
    Dim value As [IProviderPrincipal](topic10597.md)
     
    value = instance.Authenticate(credentials)  
  
C#|   
---|---  
      
    
    public [IProviderPrincipal](topic10597.md) Authenticate( 
       [IProviderCredentials](topic10588.md) _credentials_
    )  
  
#### Parameters

 _credentials_
    The [AzureCredentials](topic10646.md) to authenticate.

#### Return Value

A principal representing a DriveWorks user.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| The credentials are of the wrong type.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AzureAuthenticationProvider Class](topic10634.md)   
[AzureAuthenticationProvider Members](topic10635.md)


