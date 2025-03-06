![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveUserActiveDirectoryMapping Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3319.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : RemoveUserActiveDirectoryMapping Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerName_
    The identity provider.

_userId_
    The DriveWorks user Id.

_activeDirectoryId_
    The Active Directory principal ID to remove.

Glossary Item Box

Removes an Azure Active Directory User mapping from the provided DriveWorks User. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveUserActiveDirectoryMapping( _
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
     
    instance.RemoveUserActiveDirectoryMapping(providerName, userId, activeDirectoryId)  
  
C#|   
---|---  
      
    
    public void RemoveUserActiveDirectoryMapping( 
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
    The Active Directory principal ID to remove.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
