Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IProviderCredentials Interface   
[Members](topic10589.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) : IProviderCredentials Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a set of credentials specific to an authentication provider. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Interface IProviderCredentials   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProviderCredentials](topic10588.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public interface IProviderCredentials   
  
# Remarks

This interface may be implemented by a derived type in order to integrate DriveWorks authentication with a 3rd party credential provider.

Users should consume either the [DriveWorksCredentials](topic10669.md) or the [WindowsCredentials](topic10756.md) types to logon as either a DriveWorks user or a Windows user respectively.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProviderCredentials Members](topic10589.md)   
[DriveWorks.Security Namespace](topic10574.md)


