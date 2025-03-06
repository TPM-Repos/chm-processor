TryGetTeam(String,TeamDetails) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [TryGetTeam Method](topic3329.md) : TryGetTeam(String,TeamDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamName_
    The name of the team to retrieve.

_teamDetails_
    A reference to the variable which will receive the team details.

Glossary Item Box

Gets the named team. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetTeam( _
       ByVal _teamName_ As String, _
       ByRef _teamDetails_ As [TeamDetails](topic10703.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamName As String
    Dim teamDetails As [TeamDetails](topic10703.md)
    Dim value As Boolean
     
    value = instance.TryGetTeam(teamName, teamDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetTeam( 
       string _teamName_ ,
       ref [TeamDetails](topic10703.md) _teamDetails_
    )  
  
#### Parameters

 _teamName_
    The name of the team to retrieve.
_teamDetails_
    A reference to the variable which will receive the team details.

#### Return Value

True if the team was located and returns, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3329.md)


