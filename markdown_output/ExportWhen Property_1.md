Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExportWhen Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : ExportWhen Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/Sets when the data will be exported during the specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ExportWhen As [DataExportWhen](topic2348.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim value As [DataExportWhen](topic2348.md)
     
    instance.ExportWhen = value
     
    value = instance.ExportWhen  
  
C#|   
---|---  
      
    
    public [DataExportWhen](topic2348.md) ExportWhen {get; set;}  
  
# Remarks

The value can either be OnFinished or OnRelease.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


