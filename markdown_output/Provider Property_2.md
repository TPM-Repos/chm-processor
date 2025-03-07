Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Provider Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [DriveWorksPrincipal Class](topic10684.md) : Provider Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the DriveWorks Authentication Provider instance which created the principal. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Provider As [IAuthenticationProvider](topic10576.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DriveWorksPrincipal](topic10684.md)
    Dim value As [IAuthenticationProvider](topic10576.md)
     
    value = instance.Provider  
  
C#|   
---|---  
      
    
    public [IAuthenticationProvider](topic10576.md) Provider {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorksPrincipal Class](topic10684.md)   
[DriveWorksPrincipal Members](topic10685.md)


