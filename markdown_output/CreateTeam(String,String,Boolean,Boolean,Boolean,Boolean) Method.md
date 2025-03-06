![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTeam(String,String,Boolean,Boolean,Boolean,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [CreateTeam Method](topic3295.md) : CreateTeam(String,String,Boolean,Boolean,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamName_
    The name of the team.

_displayName_
    The display name of the team.

_isAllowedCapture_
    Whether or not the team can capture components.

_canEditAllSpecificatons_
    Whether or not the team can edit all specifications.

_editGroupSecurity_
    Whether or not the team can edit group security.

_editDriveApps_
    Whether or not the team can edit DriveApps.

Glossary Item Box

Creates a new team with the specified information. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTeam( _
       ByVal _teamName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _isAllowedCapture_ As Boolean, _
       ByVal _canEditAllSpecificatons_ As Boolean, _
       ByVal _editGroupSecurity_ As Boolean, _
       ByVal _editDriveApps_ As Boolean _
    ) As [TeamDetails](topic10703.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamName As String
    Dim displayName As String
    Dim isAllowedCapture As Boolean
    Dim canEditAllSpecificatons As Boolean
    Dim editGroupSecurity As Boolean
    Dim editDriveApps As Boolean
    Dim value As [TeamDetails](topic10703.md)
     
    value = instance.CreateTeam(teamName, displayName, isAllowedCapture, canEditAllSpecificatons, editGroupSecurity, editDriveApps)  
  
C#|   
---|---  
      
    
    public [TeamDetails](topic10703.md) CreateTeam( 
       string _teamName_ ,
       string _displayName_ ,
       bool _isAllowedCapture_ ,
       bool _canEditAllSpecificatons_ ,
       bool _editGroupSecurity_ ,
       bool _editDriveApps_
    )  
  
#### Parameters

 _teamName_
    The name of the team.
_displayName_
    The display name of the team.
_isAllowedCapture_
    Whether or not the team can capture components.
_canEditAllSpecificatons_
    Whether or not the team can edit all specifications.
_editGroupSecurity_
    Whether or not the team can edit group security.
_editDriveApps_
    Whether or not the team can edit DriveApps.

#### Return Value

An instance of the [DriveWorks.Security.TeamDetails](topic10703.md) type representing the newly created team.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3295.md)


