Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTeam(Guid,String,String,Boolean,Boolean,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) > [CreateTeam Method](topic3295.md) : CreateTeam(Guid,String,String,Boolean,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The Id to give the team.

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

Glossary Item Box

Creates a new team with the specified information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTeam( _
       ByVal _teamId_ As Guid, _
       ByVal _teamName_ As String, _
       ByVal _displayName_ As String, _
       ByVal _isAllowedCapture_ As Boolean, _
       ByVal _canEditAllSpecificatons_ As Boolean, _
       ByVal _editGroupSecurity_ As Boolean _
    ) As [TeamDetails](topic10703.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim teamId As Guid
    Dim teamName As String
    Dim displayName As String
    Dim isAllowedCapture As Boolean
    Dim canEditAllSpecificatons As Boolean
    Dim editGroupSecurity As Boolean
    Dim value As [TeamDetails](topic10703.md)
     
    value = instance.CreateTeam(teamId, teamName, displayName, isAllowedCapture, canEditAllSpecificatons, editGroupSecurity)  
  
C#|   
---|---  
      
    
    public [TeamDetails](topic10703.md) CreateTeam( 
       Guid _teamId_ ,
       string _teamName_ ,
       string _displayName_ ,
       bool _isAllowedCapture_ ,
       bool _canEditAllSpecificatons_ ,
       bool _editGroupSecurity_
    )  
  
#### Parameters

 _teamId_
    The Id to give the team.
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

#### Return Value

An instance of the [DriveWorks.Security.TeamDetails](topic10703.md) type representing the newly created team.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)   
[Overload List](topic3295.md)


