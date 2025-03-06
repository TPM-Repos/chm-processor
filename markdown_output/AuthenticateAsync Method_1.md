![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AuthenticateAsync Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AzureAuthenticationProvider Class](topic10634.md) : AuthenticateAsync Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_credentials_
    The [AzureCredentials](topic10646.md) to authenticate.

Glossary Item Box

Authenticates [AzureCredentials](topic10646.md) asynchronously. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AsyncStateMachineAttribute(DriveWorks.Security.AzureAuthenticationProvider+VB$StateMachine_8_AuthenticateAsync)>
    Public Function AuthenticateAsync( _
       ByVal _credentials_ As [IProviderCredentials](topic10588.md) _
    ) As Task(Of IProviderPrincipal)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [AzureAuthenticationProvider](topic10634.md)
    Dim credentials As [IProviderCredentials](topic10588.md)
    Dim value As Task(Of IProviderPrincipal)
     
    value = instance.AuthenticateAsync(credentials)  
  
C#|   
---|---  
      
    
    [AsyncStateMachineAttribute(DriveWorks.Security.AzureAuthenticationProvider+VB$StateMachine_8_AuthenticateAsync)]
    public Task<IProviderPrincipal> AuthenticateAsync( 
       [IProviderCredentials](topic10588.md) _credentials_
    )  
  
#### Parameters

 _credentials_
    The [AzureCredentials](topic10646.md) to authenticate.

#### Return Value

A principal representing a DriveWorks user.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AzureAuthenticationProvider Class](topic10634.md)   
[AzureAuthenticationProvider Members](topic10635.md)


