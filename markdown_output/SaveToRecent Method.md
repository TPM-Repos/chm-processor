SaveToRecent Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupCredentialsProvider Interface](topic244.md) : SaveToRecent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The contextual information about the credential request.

_group_
    The authenticated group.

_credentials_
    The credentials that were returned by a call to [QueryUserForGroupCredentials](topic249.md).

Glossary Item Box

Called after a successful logon to save the group to the recent list, including credentials if the user requested it. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub SaveToRecent( _
       ByVal _context_ As [GroupCredentialsRequestContext](topic835.md), _
       ByVal _group_ As [Group](topic2958.md), _
       ByVal _credentials_ As [IProviderCredentials](topic10588.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupCredentialsProvider](topic244.md)
    Dim context As [GroupCredentialsRequestContext](topic835.md)
    Dim group As [Group](topic2958.md)
    Dim credentials As [IProviderCredentials](topic10588.md)
     
    instance.SaveToRecent(context, group, credentials)  
  
C#|   
---|---  
      
    
    void SaveToRecent( 
       [GroupCredentialsRequestContext](topic835.md) _context_ ,
       [Group](topic2958.md) _group_ ,
       [IProviderCredentials](topic10588.md) _credentials_
    )  
  
#### Parameters

 _context_
    The contextual information about the credential request.
_group_
    The authenticated group.
_credentials_
    The credentials that were returned by a call to [QueryUserForGroupCredentials](topic249.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupCredentialsProvider Interface](topic244.md)   
[IGroupCredentialsProvider Members](topic245.md)


