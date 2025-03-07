Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IncludeFiles Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [FilePickingOptions Class](topic9902.md) : IncludeFiles Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Designed to negate exclude folders, not include files outside the root. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IncludeFiles As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FilePickingOptions](topic9902.md)
    Dim value As HashSet(Of String)
     
    value = instance.IncludeFiles  
  
C#|   
---|---  
      
    
    public HashSet<string> IncludeFiles {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FilePickingOptions Class](topic9902.md)   
[FilePickingOptions Members](topic9903.md)


