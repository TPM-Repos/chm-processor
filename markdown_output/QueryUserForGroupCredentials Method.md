Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryUserForGroupCredentials Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupCredentialsProvider Interface](topic244.md) : QueryUserForGroupCredentials Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    Information about the credentials request.

Glossary Item Box

Requests credentials from the user to be used to log on to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function QueryUserForGroupCredentials( _
       ByVal _context_ As [GroupCredentialsRequestContext](topic835.md) _
    ) As [IProviderCredentials](topic10588.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupCredentialsProvider](topic244.md)
    Dim context As [GroupCredentialsRequestContext](topic835.md)
    Dim value As [IProviderCredentials](topic10588.md)
     
    value = instance.QueryUserForGroupCredentials(context)  
  
C#|   
---|---  
      
    
    [IProviderCredentials](topic10588.md) QueryUserForGroupCredentials( 
       [GroupCredentialsRequestContext](topic835.md) _context_
    )  
  
#### Parameters

 _context_
    Information about the credentials request.

#### Return Value

A credentials object which can be passed to the Group open method to log on to the group.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupCredentialsProvider Interface](topic244.md)   
[IGroupCredentialsProvider Members](topic245.md)


