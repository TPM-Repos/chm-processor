Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Columns Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : Columns Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

An array of all the columns that are used from the table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Columns As DataExportColumnDefinition()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim value() As DataExportColumnDefinition
     
    value = instance.Columns  
  
C#|   
---|---  
      
    
    public DataExportColumnDefinition[] Columns {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


