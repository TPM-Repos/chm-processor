![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetPassword Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10681.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [DriveWorksCredentials Class](topic10669.md) : SetPassword Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_password_
    The password to hash and store.

_preservePassword_
    True to store the password, false to discard it after the hash has been computed.

Glossary Item Box

Hashes and stores the given password. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetPassword( _
       ByVal _password_ As String, _
       ByVal _preservePassword_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DriveWorksCredentials](topic10669.md)
    Dim password As String
    Dim preservePassword As Boolean
     
    instance.SetPassword(password, preservePassword)  
  
C#|   
---|---  
      
    
    public void SetPassword( 
       string _password_ ,
       bool _preservePassword_
    )  
  
#### Parameters

 _password_
    The password to hash and store.
_preservePassword_
    True to store the password, false to discard it after the hash has been computed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DriveWorksCredentials Class](topic10669.md)   
[DriveWorksCredentials Members](topic10670.md)

©2024 DriveWorks Ltd. All Rights Reserved.
