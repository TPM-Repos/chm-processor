Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateProvider Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AuthenticationProviderFactory Class](topic10617.md) : CreateProvider Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerName_
    The name of the provider to instantiate.

Glossary Item Box

Creates an instance of the provider which has been registered with the specified providerName. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreateProvider( _
       ByVal _providerName_ As String _
    ) As [IAuthenticationProvider](topic10576.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AuthenticationProviderFactory Class](topic10617.md)   
[AuthenticationProviderFactory Members](topic10618.md)


