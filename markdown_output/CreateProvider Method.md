![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateProvider Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10624.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AuthenticationProviderFactory Class](topic10617.md) : CreateProvider Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerName_
    The name of the provider to instantiate.

Glossary Item Box

Creates an instance of the provider which has been registered with the specified providerName. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreateProvider( _
       ByVal _providerName_ As String _
    ) As [IAuthenticationProvider](topic10576.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim providerName As String
    Dim value As [IAuthenticationProvider](topic10576.md)
     
    value = [AuthenticationProviderFactory](topic10617.md).CreateProvider(providerName)  
  
C#|   
---|---  
      
    
    public static [IAuthenticationProvider](topic10576.md) CreateProvider( 
       string _providerName_
    )  
  
#### Parameters

 _providerName_
    The name of the provider to instantiate.

#### Return Value

A provider implementation or a null reference (Nothing in Visual Basic) if the providerName is unknown.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AuthenticationProviderFactory Class](topic10617.md)   
[AuthenticationProviderFactory Members](topic10618.md)

©2024 DriveWorks Ltd. All Rights Reserved.
