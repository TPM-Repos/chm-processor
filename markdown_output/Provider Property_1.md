Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Provider Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [IProviderRole Interface](topic10608.md) : Provider Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the provider which returned the role. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Provider As [IAuthenticationProvider](topic10576.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProviderRole](topic10608.md)
    Dim value As [IAuthenticationProvider](topic10576.md)
     
    value = instance.Provider  
  
C#|   
---|---  
      
    
    [IAuthenticationProvider](topic10576.md) Provider {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProviderRole Interface](topic10608.md)   
[IProviderRole Members](topic10609.md)


