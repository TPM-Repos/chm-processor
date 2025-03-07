Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [AzureAuthenticationProvider Class](topic10634.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tenantId_
    

_clientId_
    

Glossary Item Box

Creates a Public Client with the Tenant and Client IDs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Initialize( _
       ByVal _tenantId_ As String, _
       ByVal _clientId_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AzureAuthenticationProvider](topic10634.md)
    Dim tenantId As String
    Dim clientId As String
     
    instance.Initialize(tenantId, clientId)  
  
C#|   
---|---  
      
    
    public void Initialize( 
       string _tenantId_ ,
       string _clientId_
    )  
  
#### Parameters

 _tenantId_
    
_clientId_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AzureAuthenticationProvider Class](topic10634.md)   
[AzureAuthenticationProvider Members](topic10635.md)


