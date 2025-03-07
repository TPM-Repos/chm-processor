Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeams Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeams Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information about all registered teams. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeams() As [TeamDetails()](topic10703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim value() As [TeamDetails](topic10703.md)
     
    value = instance.GetTeams()  
  
C#|   
---|---  
      
    
    public [TeamDetails[]](topic10703.md) GetTeams()  
  
#### Return Value

An array containing an instance of the [DriveWorks.Security.TeamDetails](topic10703.md) type for each registered team.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


