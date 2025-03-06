![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUserActiveDirectoryMappings Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3312.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetUserActiveDirectoryMappings Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_providerName_
    The identity provider.

_userId_
    The DriveWorks User Id.

Glossary Item Box

Gets a list of mapped Azure Active Directory User Principal ID's for a given DriveWorks User Id. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetUserActiveDirectoryMappings( _
       ByVal _providerName_ As String, _
       ByVal _userId_ As Guid _
    ) As List(Of Guid)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim providerName As String
    Dim userId As Guid
    Dim value As List(Of Guid)
     
    value = instance.GetUserActiveDirectoryMappings(providerName, userId)  
  
C#|   
---|---  
      
    
    public List<Guid> GetUserActiveDirectoryMappings( 
       string _providerName_ ,
       Guid _userId_
    )  
  
#### Parameters

 _providerName_
    The identity provider.
_userId_
    The DriveWorks User Id.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
