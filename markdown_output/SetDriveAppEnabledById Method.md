SetDriveAppEnabledById Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : SetDriveAppEnabledById Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The unique identifier of the DriveApp to enable/disable.

_enabled_
    The new enabled value to update the DriveApp with.

Glossary Item Box

Updates whether a DriveApp is enabled in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function SetDriveAppEnabledById( _
       ByVal _id_ As Guid, _
       ByVal _enabled_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim id As Guid
    Dim enabled As Boolean
    Dim value As Boolean
     
    value = instance.SetDriveAppEnabledById(id, enabled)  
  
C#|   
---|---  
      
    
    public bool SetDriveAppEnabledById( 
       Guid _id_ ,
       bool _enabled_
    )  
  
#### Parameters

 _id_
    The unique identifier of the DriveApp to enable/disable.
_enabled_
    The new enabled value to update the DriveApp with.

#### Return Value

True if successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


