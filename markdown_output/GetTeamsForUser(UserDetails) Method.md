Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamsForUser(UserDetails) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetTeamsForUser Method](topic3309.md) : GetTeamsForUser(UserDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_user_
    The user to check.

Glossary Item Box

Gets all the teams to which the given user belongs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetTeamsForUser( _
       ByVal _user_ As [UserDetails](topic10740.md) _
    ) As [TeamDetails()](topic10703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim user As [UserDetails](topic10740.md)
    Dim value() As [TeamDetails](topic10703.md)
     
    value = instance.GetTeamsForUser(user)  
  
C#|   
---|---  
      
    
    public [TeamDetails[]](topic10703.md) GetTeamsForUser( 
       [UserDetails](topic10740.md) _user_
    )  
  
#### Parameters

 _user_
    The user to check.

#### Return Value

An array of teams.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3309.md)


