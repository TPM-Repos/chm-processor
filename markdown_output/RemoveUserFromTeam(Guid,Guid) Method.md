![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveUserFromTeam(Guid,Guid) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3322.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [RemoveUserFromTeam Method](topic3320.md) : RemoveUserFromTeam(Guid,Guid) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team from which to remove the user.

_userId_
    The unique identifier of the user to remove from the team.

Glossary Item Box

Removes the specified user from the given team. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RemoveUserFromTeam( _
       ByVal _teamId_ As Guid, _
       ByVal _userId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim userId As Guid
    Dim value As Boolean
     
    value = instance.RemoveUserFromTeam(teamId, userId)  
  
C#|   
---|---  
      
    
    public bool RemoveUserFromTeam( 
       Guid _teamId_ ,
       Guid _userId_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team from which to remove the user.
_userId_
    The unique identifier of the user to remove from the team.

#### Return Value

True if both the user and the team were found, and the user was removed from the team.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3320.md)

©2024 DriveWorks Ltd. All Rights Reserved.
