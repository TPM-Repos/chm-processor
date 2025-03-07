Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRoles Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [IProviderPrincipal Interface](topic10597.md) : GetRoles Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the roles to which the principal belongs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetRoles() As [IProviderRole()](topic10608.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProviderPrincipal](topic10597.md)
    Dim value() As [IProviderRole](topic10608.md)
     
    value = instance.GetRoles()  
  
C#|   
---|---  
      
    
    [IProviderRole[]](topic10608.md) GetRoles()  
  
#### Return Value

An array of roles which may not be a null reference.

# Remarks

If the given principal is not registered in the DriveWorks Group, but it belongs to a role which is registered, the principal will be registered automatically in the Group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProviderPrincipal Interface](topic10597.md)   
[IProviderPrincipal Members](topic10598.md)


