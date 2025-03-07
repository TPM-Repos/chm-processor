Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteDriveAppByAlias Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : DeleteDriveAppByAlias Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppAlias_
    The alias of the DriveApp to delete.

Glossary Item Box

Deletes the DriveApp reference from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteDriveAppByAlias( _
       ByVal _driveAppAlias_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppAlias As String
    Dim value As Boolean
     
    value = instance.DeleteDriveAppByAlias(driveAppAlias)  
  
C#|   
---|---  
      
    
    public bool DeleteDriveAppByAlias( 
       string _driveAppAlias_
    )  
  
#### Parameters

 _driveAppAlias_
    The alias of the DriveApp to delete.

#### Return Value

True if successfully deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


