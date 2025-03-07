Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteDriveAppById Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : DeleteDriveAppById Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The unique identifier of the DriveApp to delete.

Glossary Item Box

Deletes the DriveApp reference from the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteDriveAppById( _
       ByVal _id_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim id As Guid
    Dim value As Boolean
     
    value = instance.DeleteDriveAppById(id)  
  
C#|   
---|---  
      
    
    public bool DeleteDriveAppById( 
       Guid _id_
    )  
  
#### Parameters

 _id_
    The unique identifier of the DriveApp to delete.

#### Return Value

True if successfully deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


