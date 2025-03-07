Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanCurrentUserRunDriveApp Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : CanCurrentUserRunDriveApp Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppId_
    The unique identifier of the DriveApp to check permissions for.

Glossary Item Box

Gets whether or not the current user is in a team that has permission to run a chosen DriveApp. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CanCurrentUserRunDriveApp( _
       ByVal _driveAppId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppId As Guid
    Dim value As Boolean
     
    value = instance.CanCurrentUserRunDriveApp(driveAppId)  
  
C#|   
---|---  
      
    
    public bool CanCurrentUserRunDriveApp( 
       Guid _driveAppId_
    )  
  
#### Parameters

 _driveAppId_
    The unique identifier of the DriveApp to check permissions for.

#### Return Value

True if the current user has permission to run the DriveApp.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


