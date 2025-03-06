![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectPermissionsForTeam(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [GetProjectPermissionsForTeam Method](topic3301.md) : GetProjectPermissionsForTeam(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamName_
    The name of the team.

Glossary Item Box

Gets the list of project permissions for the specified team. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetProjectPermissionsForTeam( _
       ByVal _teamName_ As String _
    ) As [TeamProjectPermission()](topic10729.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamName As String
    Dim value() As [TeamProjectPermission](topic10729.md)
     
    value = instance.GetProjectPermissionsForTeam(teamName)  
  
C#|   
---|---  
      
    
    public [TeamProjectPermission[]](topic10729.md) GetProjectPermissionsForTeam( 
       string _teamName_
    )  
  
#### Parameters

 _teamName_
    The name of the team.

#### Return Value

An array of instances of the [DriveWorks.Security.TeamProjectPermission](topic10729.md) type for the project permissions.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3301.md)


