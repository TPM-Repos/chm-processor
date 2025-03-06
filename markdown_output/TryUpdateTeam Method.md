       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateTeam Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TryUpdateTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamDetails_
    The changed team details.

Glossary Item Box

Updates the team with the specified details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateTeam( _
       ByVal _teamDetails_ As [TeamDetails](topic10703.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamDetails As [TeamDetails](topic10703.md)
    Dim value As Boolean
     
    value = instance.TryUpdateTeam(teamDetails)  
  
C#|   
---|---  
      
    
    public bool TryUpdateTeam( 
       [TeamDetails](topic10703.md) _teamDetails_
    )  
  
#### Parameters

 _teamDetails_
    The changed team details.

#### Return Value

True if the team was successfully found and updated, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


