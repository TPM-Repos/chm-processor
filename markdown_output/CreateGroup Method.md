![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateGroup Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : CreateGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupName_
    The name of the group to create.

_creationUsername_
    The server's admin username.

_creationPassword_
    The server's admin password.

_credentials_
    Initial login details for the new group.

Glossary Item Box

Creates a new group with the specified details 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub CreateGroup( _
       ByVal _groupName_ As String, _
       ByVal _creationUsername_ As String, _
       ByVal _creationPassword_ As String, _
       ByVal _credentials_ As [IProviderCredentials](topic10588.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim groupName As String
    Dim creationUsername As String
    Dim creationPassword As String
    Dim credentials As [IProviderCredentials](topic10588.md)
     
    instance.CreateGroup(groupName, creationUsername, creationPassword, credentials)  
  
C#|   
---|---  
      
    
    public void CreateGroup( 
       string _groupName_ ,
       string _creationUsername_ ,
       string _creationPassword_ ,
       [IProviderCredentials](topic10588.md) _credentials_
    )  
  
#### Parameters

 _groupName_
    The name of the group to create.
_creationUsername_
    The server's admin username.
_creationPassword_
    The server's admin password.
_credentials_
    Initial login details for the new group.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


