Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlColumns Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : ControlColumns Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of control columns. Control columns depict where export row data is to match the existing data for updating/appending rows. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ControlColumns As DataExportColumnDefinition()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim value() As DataExportColumnDefinition
     
    value = instance.ControlColumns  
  
C#|   
---|---  
      
    
    public DataExportColumnDefinition[] ControlColumns {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


