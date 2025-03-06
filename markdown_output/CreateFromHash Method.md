![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateFromHash Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10678.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreateFromHash( _
       ByVal _userName_ As String, _
       ByVal _passwordHash_ As String _
    ) As [DriveWorksCredentials](topic10669.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorksCredentials Class](topic10669.md)   
[DriveWorksCredentials Members](topic10670.md)

©2024 DriveWorks Ltd. All Rights Reserved.
