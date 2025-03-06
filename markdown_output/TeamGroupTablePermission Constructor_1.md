TeamGroupTablePermission Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [TeamGroupTablePermission Class](topic10718.md) : TeamGroupTablePermission Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_teamId_
    The unique identifier of the team to which the permission applies.

_groupTableId_
    The unique identifier of the group data table to which permission is given.

_permissionType_
    The type of the permission which is enabled.

Glossary Item Box

Initializes a new instance of the [TeamGroupTablePermission](topic10718.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _teamId_ As Guid, _
       ByVal _groupTableId_ As Guid, _
       ByVal _permissionType_ As [GroupTablePermission](topic10616.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim teamId As Guid
    Dim groupTableId As Guid
    Dim permissionType As [GroupTablePermission](topic10616.md)
     
    Dim instance As New [TeamGroupTablePermission](topic10718.md)(teamId, groupTableId, permissionType)  
  
C#|   
---|---  
      
    
    public TeamGroupTablePermission( 
       Guid _teamId_ ,
       Guid _groupTableId_ ,
       [GroupTablePermission](topic10616.md) _permissionType_
    )  
  
#### Parameters

 _teamId_
    The unique identifier of the team to which the permission applies.
_groupTableId_
    The unique identifier of the group data table to which permission is given.
_permissionType_
    The type of the permission which is enabled.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TeamGroupTablePermission Class](topic10718.md)   
[TeamGroupTablePermission Members](topic10719.md)


