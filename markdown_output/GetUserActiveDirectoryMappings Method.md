Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUserActiveDirectoryMappings Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetUserActiveDirectoryMappings( _
       ByVal _providerName_ As String, _
       ByVal _userId_ As Guid _
    ) As List(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


