Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IAuthenticationProvider Interface   
[Members](topic10577.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) : IAuthenticationProvider Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for pluggable authentication systems in DriveWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Interface IAuthenticationProvider   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAuthenticationProvider](topic10576.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public interface IAuthenticationProvider   
  
# Remarks

In order for an instance of a type derived from this interface to be registered with the [AuthenticationProviderFactory](topic10617.md), the derived type must be marked with the [AuthenticationProviderNameAttribute](topic10626.md) attribute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAuthenticationProvider Members](topic10577.md)   
[DriveWorks.Security Namespace](topic10574.md)


