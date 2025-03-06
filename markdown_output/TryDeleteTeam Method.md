TryDeleteTeam Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TryDeleteTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to delete.

Glossary Item Box

Deletes the named team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryDeleteTeam( _
       ByVal _teamId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim value As Boolean
     
    value = instance.TryDeleteTeam(teamId)  
  
C#|   
---|---  
      
    
    public bool TryDeleteTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to delete.

#### Return Value

True if the team was successfully found and deleted, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


