Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CurrentUserTeams Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : CurrentUserTeams Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the teams to which the logged-on user belongs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property CurrentUserTeams As [TeamDetails()](topic10703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim value() As [TeamDetails](topic10703.md)
     
    value = instance.CurrentUserTeams  
  
C#|   
---|---  
      
    
    public [TeamDetails[]](topic10703.md) CurrentUserTeams {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


