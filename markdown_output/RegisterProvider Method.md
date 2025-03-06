![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterProvider Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10625.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AuthenticationProviderFactory Class](topic10617.md) : RegisterProvider Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerType_
    The type of the provider to register.

Glossary Item Box

Registers an authentication provider with DriveWorks. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub RegisterProvider( _
       ByVal _providerType_ As Type _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim providerType As Type
     
    [AuthenticationProviderFactory](topic10617.md).RegisterProvider(providerType)  
  
C#|   
---|---  
      
    
    public static void RegisterProvider( 
       Type _providerType_
    )  
  
#### Parameters

 _providerType_
    The type of the provider to register.

# ![](dotnetimages/collapse.gif)Remarks

Authentication providers must implement the [IAuthenticationProvider](topic10576.md) interface and be marked with the [AuthenticationProviderNameAttribute](topic10626.md) attribute.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AuthenticationProviderFactory Class](topic10617.md)   
[AuthenticationProviderFactory Members](topic10618.md)

©2024 DriveWorks Ltd. All Rights Reserved.
