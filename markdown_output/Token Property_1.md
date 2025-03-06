       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Token Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [IProviderPrincipal Interface](topic10597.md) : Token Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a string which is compared by DriveWorks with a stored token in the Group to validate the returned principal. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Token As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IProviderPrincipal](topic10597.md)
    Dim value As String
     
    value = instance.Token  
  
C#|   
---|---  
      
    
    string Token {get;}  
  
# Remarks

The return value may be a null reference as the token checking feature is an optional additional security measure.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IProviderPrincipal Interface](topic10597.md)   
[IProviderPrincipal Members](topic10598.md)


