RemoveTeam Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) : RemoveTeam Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to remove.

Glossary Item Box

Removes the team with the specified identifier from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveTeam( _
       ByVal _teamId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim teamId As Guid
     
    instance.RemoveTeam(teamId)  
  
C#|   
---|---  
      
    
    public void RemoveTeam( 
       Guid _teamId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to remove.

# Remarks

If an attempt is made to remove a team from an instance which is marked as "All Teams Allowed", i.e. the [IsUniversal](topic11756.md) property returns true, no action is taken by this method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)


