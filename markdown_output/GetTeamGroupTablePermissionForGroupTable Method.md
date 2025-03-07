Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionForGroupTable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionForGroupTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupTableId_
    The identifier of the group data table to get the permissions of.

_userId_
    The identifier of the user to get the permissions of.

Glossary Item Box

Returns the effective permission that a user has for the specified group data table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionForGroupTable( _
       ByVal _groupTableId_ As Guid, _
       ByVal _userId_ As Guid _
    ) As [GroupTablePermission](topic10616.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim groupTableId As Guid
    Dim userId As Guid
    Dim value As [GroupTablePermission](topic10616.md)
     
    value = instance.GetTeamGroupTablePermissionForGroupTable(groupTableId, userId)  
  
C#|   
---|---  
      
    
    public [GroupTablePermission](topic10616.md) GetTeamGroupTablePermissionForGroupTable( 
       Guid _groupTableId_ ,
       Guid _userId_
    )  
  
#### Parameters

 _groupTableId_
    The identifier of the group data table to get the permissions of.
_userId_
    The identifier of the user to get the permissions of.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


