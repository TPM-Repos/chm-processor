Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Import Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [CaptureImportManager Class](topic2468.md) : Import Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Performs the import process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Import() As Dictionary(Of Guid,Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CaptureImportManager](topic2468.md)
    Dim value As Dictionary(Of Guid,Guid)
     
    value = instance.Import()  
  
C#|   
---|---  
      
    
    public Dictionary<Guid,Guid> Import()  
  
#### Return Value

A dictionary mapping the original captured component identifiers to their new captured component identifiers for components which required remapping.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CaptureImportManager Class](topic2468.md)   
[CaptureImportManager Members](topic2469.md)


