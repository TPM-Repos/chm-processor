Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUserById Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetUserById Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userId_
    The unique identifier of the group to get.

Glossary Item Box

Gets a users details from the given ID. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetUserById( _
       ByVal _userId_ As Guid _
    ) As [UserDetails](topic10740.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim userId As Guid
    Dim value As [UserDetails](topic10740.md)
     
    value = instance.GetUserById(userId)  
  
C#|   
---|---  
      
    
    public [UserDetails](topic10740.md) GetUserById( 
       Guid _userId_
    )  
  
#### Parameters

 _userId_
    The unique identifier of the group to get.

#### Return Value

The details for the specified user if it exists, otherwise a null reference.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


