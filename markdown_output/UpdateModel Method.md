       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateModel Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9911.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [FilePickingOptions Class](topic9902.md) : UpdateModel Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_root_
    The folder to start from.

Glossary Item Box

Takes an existing model and updates it to match the current file system. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdateModel( _
       ByVal _root_ As [DirectoryStorageItemModel](topic9893.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FilePickingOptions](topic9902.md)
    Dim root As [DirectoryStorageItemModel](topic9893.md)
     
    instance.UpdateModel(root)  
  
C#|   
---|---  
      
    
    public void UpdateModel( 
       [DirectoryStorageItemModel](topic9893.md) _root_
    )  
  
#### Parameters

 _root_
    The folder to start from.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FilePickingOptions Class](topic9902.md)   
[FilePickingOptions Members](topic9903.md)

©2024 DriveWorks Ltd. All Rights Reserved.
