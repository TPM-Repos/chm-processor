Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EmailAddress Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [DriveWorksPrincipal Class](topic10684.md) : EmailAddress Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Always returns a null reference. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property EmailAddress As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DriveWorksPrincipal](topic10684.md)
    Dim value As String
     
    value = instance.EmailAddress  
  
C#|   
---|---  
      
    
    public string EmailAddress {get;}  
  
# Remarks

DriveWorks user details are always stored in the DriveWorks database so there is no need or way to provide the details in a principal.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorksPrincipal Class](topic10684.md)   
[DriveWorksPrincipal Members](topic10685.md)


