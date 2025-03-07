Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUserByActiveDirectoryId Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetUserByActiveDirectoryId Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_principalId_
    The AAD User ID.

_excludeUserId_
    Don't include the current User ID.

Glossary Item Box

Get a specific DriveWorks User details that is already registered against an AAD User, if one exists. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetUserByActiveDirectoryId( _
       ByVal _principalId_ As Guid, _
       ByVal _excludeUserId_ As Guid _
    ) As [UserDetails](topic10740.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim principalId As Guid
    Dim excludeUserId As Guid
    Dim value As [UserDetails](topic10740.md)
     
    value = instance.GetUserByActiveDirectoryId(principalId, excludeUserId)  
  
C#|   
---|---  
      
    
    public [UserDetails](topic10740.md) GetUserByActiveDirectoryId( 
       Guid _principalId_ ,
       Guid _excludeUserId_
    )  
  
#### Parameters

 _principalId_
    The AAD User ID.
_excludeUserId_
    Don't include the current User ID.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


