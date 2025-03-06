![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionsForGroupTable Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3305.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionsForGroupTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupTableId_
    The unique identifier of the group data table to get the permissions for.

Glossary Item Box

Returns a collection group data table permissions that the specified group data table has. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionsForGroupTable( _
       ByVal _groupTableId_ As Guid _
    ) As [TeamGroupTablePermission()](topic10718.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim groupTableId As Guid
    Dim value() As [TeamGroupTablePermission](topic10718.md)
     
    value = instance.GetTeamGroupTablePermissionsForGroupTable(groupTableId)  
  
C#|   
---|---  
      
    
    public [TeamGroupTablePermission[]](topic10718.md) GetTeamGroupTablePermissionsForGroupTable( 
       Guid _groupTableId_
    )  
  
#### Parameters

 _groupTableId_
    The unique identifier of the group data table to get the permissions for.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
