Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommonColumns Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : CommonColumns Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets A collection of common columns. Common columns are always the same for each row. Used to save calculation time. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property CommonColumns As DataExportColumnDefinition()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim value() As DataExportColumnDefinition
     
    value = instance.CommonColumns  
  
C#|   
---|---  
      
    
    public DataExportColumnDefinition[] CommonColumns {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


