![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatePrincipal Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10643.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AzureAuthenticationProvider Class](topic10634.md) : CreatePrincipal Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_credentials_
    The principal's credentials.

_principalId_
    The unique identifier of the principal.

_username_
    The login name for the principal.

_accessToken_
    The OAuth2 access token for the principal.

Glossary Item Box

Constructs a principal corresponding to the given information. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreatePrincipal( _
       ByVal _credentials_ As [AzureCredentials](topic10646.md), _
       ByVal _principalId_ As String, _
       ByVal _username_ As String, _
       ByVal _accessToken_ As String _
    ) As [IProviderPrincipal](topic10597.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [AzureAuthenticationProvider](topic10634.md)
    Dim credentials As [AzureCredentials](topic10646.md)
    Dim principalId As String
    Dim username As String
    Dim accessToken As String
    Dim value As [IProviderPrincipal](topic10597.md)
     
    value = instance.CreatePrincipal(credentials, principalId, username, accessToken)  
  
C#|   
---|---  
      
    
    public [IProviderPrincipal](topic10597.md) CreatePrincipal( 
       [AzureCredentials](topic10646.md) _credentials_ ,
       string _principalId_ ,
       string _username_ ,
       string _accessToken_
    )  
  
#### Parameters

 _credentials_
    The principal's credentials.
_principalId_
    The unique identifier of the principal.
_username_
    The login name for the principal.
_accessToken_
    The OAuth2 access token for the principal.

#### Return Value

An object implementing the [IProviderPrincipal](topic10597.md) interface.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AzureAuthenticationProvider Class](topic10634.md)   
[AzureAuthenticationProvider Members](topic10635.md)

©2024 DriveWorks Ltd. All Rights Reserved.
