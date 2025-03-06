![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionsForUser Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3307.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionsForUser Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userId_
    The unique identifier of the user to fetch the permissions for.

Glossary Item Box

Returns a collection of group data table permissions that the specified user has. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionsForUser( _
       ByVal _userId_ As Guid _
    ) As [TeamGroupTablePermission()](topic10718.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim userId As Guid
    Dim value() As [TeamGroupTablePermission](topic10718.md)
     
    value = instance.GetTeamGroupTablePermissionsForUser(userId)  
  
C#|   
---|---  
      
    
    public [TeamGroupTablePermission[]](topic10718.md) GetTeamGroupTablePermissionsForUser( 
       Guid _userId_
    )  
  
#### Parameters

 _userId_
    The unique identifier of the user to fetch the permissions for.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
