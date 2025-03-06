![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTeam(Guid,TeamDetails) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3330.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [TryGetTeam Method](topic3329.md) : TryGetTeam(Guid,TeamDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to retrieve.

_teamDetails_
    A reference to the variable which will receive the team details.

Glossary Item Box

Gets the specified team. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetTeam( _
       ByVal _teamId_ As Guid, _
       ByRef _teamDetails_ As [TeamDetails](topic10703.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim teamDetails As [TeamDetails](topic10703.md)
    Dim value As Boolean
     
    value = instance.TryGetTeam(teamId, teamDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetTeam( 
       Guid _teamId_ ,
       ref [TeamDetails](topic10703.md) _teamDetails_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to retrieve.
_teamDetails_
    A reference to the variable which will receive the team details.

#### Return Value

True if the team was located and returns, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3329.md)

©2024 DriveWorks Ltd. All Rights Reserved.
