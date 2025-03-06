       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateDriveApp Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : TryUpdateDriveApp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppDetails_
    The [DriveAppDetails](topic2750.md) object that represents the DriveApp to update.

Glossary Item Box

Updates a DriveApp in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateDriveApp( _
       ByVal _driveAppDetails_ As [DriveAppDetails](topic2750.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppDetails As [DriveAppDetails](topic2750.md)
    Dim value As Boolean
     
    value = instance.TryUpdateDriveApp(driveAppDetails)  
  
C#|   
---|---  
      
    
    public bool TryUpdateDriveApp( 
       [DriveAppDetails](topic2750.md) _driveAppDetails_
    )  
  
#### Parameters

 _driveAppDetails_
    The [DriveAppDetails](topic2750.md) object that represents the DriveApp to update.

#### Return Value

True if successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


