Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUsers Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetUsers Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information about all registered users. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetUsers() As [UserDetails()](topic10740.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim value() As [UserDetails](topic10740.md)
     
    value = instance.GetUsers()  
  
C#|   
---|---  
      
    
    public [UserDetails[]](topic10740.md) GetUsers()  
  
#### Return Value

An array containing an instance of the [DriveWorks.Security.UserDetails](topic10740.md) type for each registered user.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


