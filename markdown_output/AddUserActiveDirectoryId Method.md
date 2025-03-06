![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddUserActiveDirectoryId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : AddUserActiveDirectoryId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerName_
    The identity provider.

_userId_
    The DriveWorks user Id.

_activeDirectoryId_
    The Active Directory principal ID to add.

Glossary Item Box

Adds an Azure Active Directory User mapping for the provided DriveWorks User. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddUserActiveDirectoryId( _
       ByVal _providerName_ As String, _
       ByVal _userId_ As Guid, _
       ByVal _activeDirectoryId_ As Guid _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim providerName As String
    Dim userId As Guid
    Dim activeDirectoryId As Guid
     
    instance.AddUserActiveDirectoryId(providerName, userId, activeDirectoryId)  
  
C#|   
---|---  
      
    
    public void AddUserActiveDirectoryId( 
       string _providerName_ ,
       Guid _userId_ ,
       Guid _activeDirectoryId_
    )  
  
#### Parameters

 _providerName_
    The identity provider.
_userId_
    The DriveWorks user Id.
_activeDirectoryId_
    The Active Directory principal ID to add.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


