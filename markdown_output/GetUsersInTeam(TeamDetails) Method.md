![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUsersInTeam(TeamDetails) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3317.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetUsersInTeam Method](topic3316.md) : GetUsersInTeam(TeamDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_team_
    The team to check.

Glossary Item Box

Gets all the users that belong to the specified team. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetUsersInTeam( _
       ByVal _team_ As [TeamDetails](topic10703.md) _
    ) As [UserDetails()](topic10740.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim team As [TeamDetails](topic10703.md)
    Dim value() As [UserDetails](topic10740.md)
     
    value = instance.GetUsersInTeam(team)  
  
C#|   
---|---  
      
    
    public [UserDetails[]](topic10740.md) GetUsersInTeam( 
       [TeamDetails](topic10703.md) _team_
    )  
  
#### Parameters

 _team_
    The team to check.

#### Return Value

An array of users.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3316.md)

©2024 DriveWorks Ltd. All Rights Reserved.
