Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IncludeFolders Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [FilePickingOptions Class](topic9902.md) : IncludeFolders Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Designed to negate excluded folders, not add folders outside the root. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IncludeFolders As HashSet(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FilePickingOptions](topic9902.md)
    Dim value As HashSet(Of String)
     
    value = instance.IncludeFolders  
  
C#|   
---|---  
      
    
    public HashSet<string> IncludeFolders {get;}  
  
# Remarks

Having things outside the root folder would mean either: 1. Some unpredictable/complex copying/extracting behaviour 2. Some things would have to be referenced or impossible due to rules etc

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FilePickingOptions Class](topic9902.md)   
[FilePickingOptions Members](topic9903.md)


