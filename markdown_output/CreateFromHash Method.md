Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateFromHash Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [DriveWorksCredentials Class](topic10669.md) : CreateFromHash Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userName_
    The name of the DriveWorks user.

_passwordHash_
    The hashed password of the DriveWorks user.

Glossary Item Box

Initializes a new instance of the [DriveWorksCredentials](topic10669.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreateFromHash( _
       ByVal _userName_ As String, _
       ByVal _passwordHash_ As String _
    ) As [DriveWorksCredentials](topic10669.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim userName As String
    Dim passwordHash As String
    Dim value As [DriveWorksCredentials](topic10669.md)
     
    value = [DriveWorksCredentials](topic10669.md).CreateFromHash(userName, passwordHash)  
  
C#|   
---|---  
      
    
    public static [DriveWorksCredentials](topic10669.md) CreateFromHash( 
       string _userName_ ,
       string _passwordHash_
    )  
  
#### Parameters

 _userName_
    The name of the DriveWorks user.
_passwordHash_
    The hashed password of the DriveWorks user.

#### Return Value

An initialized instance of the type with the given credentials.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorksCredentials Class](topic10669.md)   
[DriveWorksCredentials Members](topic10670.md)


