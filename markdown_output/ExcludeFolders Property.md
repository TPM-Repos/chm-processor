Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExcludeFolders Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [FilePickingOptions Class](topic9902.md) : ExcludeFolders Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Collection of directories that should not be included. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ExcludeFolders As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FilePickingOptions](topic9902.md)
    Dim value As HashSet(Of String)
     
    value = instance.ExcludeFolders  
  
C#|   
---|---  
      
    
    public HashSet<string> ExcludeFolders {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FilePickingOptions Class](topic9902.md)   
[FilePickingOptions Members](topic9903.md)


