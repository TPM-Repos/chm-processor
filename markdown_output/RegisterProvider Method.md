Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterProvider Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AuthenticationProviderFactory Class](topic10617.md) : RegisterProvider Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerType_
    The type of the provider to register.

Glossary Item Box

Registers an authentication provider with DriveWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub RegisterProvider( _
       ByVal _providerType_ As Type _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Remarks

Authentication providers must implement the [IAuthenticationProvider](topic10576.md) interface and be marked with the [AuthenticationProviderNameAttribute](topic10626.md) attribute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AuthenticationProviderFactory Class](topic10617.md)   
[AuthenticationProviderFactory Members](topic10618.md)


