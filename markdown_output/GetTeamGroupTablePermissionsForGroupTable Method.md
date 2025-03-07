Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTeamGroupTablePermissionsForGroupTable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : GetTeamGroupTablePermissionsForGroupTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupTableId_
    The unique identifier of the group data table to get the permissions for.

Glossary Item Box

Returns a collection group data table permissions that the specified group data table has. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTeamGroupTablePermissionsForGroupTable( _
       ByVal _groupTableId_ As Guid _
    ) As [TeamGroupTablePermission()](topic10718.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


