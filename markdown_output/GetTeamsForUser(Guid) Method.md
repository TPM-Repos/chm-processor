Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamsForUser(Guid) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetTeamsForUser Method](topic3309.md) : GetTeamsForUser(Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userId_
    The unique identifier of the user to check.

Glossary Item Box

Gets all the teams to which the given user belongs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetTeamsForUser( _
       ByVal _userId_ As Guid _
    ) As [TeamDetails()](topic10703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim userId As Guid
    Dim value() As [TeamDetails](topic10703.md)
     
    value = instance.GetTeamsForUser(userId)  
  
C#|   
---|---  
      
    
    public [TeamDetails[]](topic10703.md) GetTeamsForUser( 
       Guid _userId_
    )  
  
#### Parameters

 _userId_
    The unique identifier of the user to check.

#### Return Value

An array of teams.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3309.md)


