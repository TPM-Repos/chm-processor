Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Columns Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : Columns Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the columns in the data export document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property Columns As DataExportColumnDefinition()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim value() As DataExportColumnDefinition
     
    value = instance.Columns  
  
C#|   
---|---  
      
    
    DataExportColumnDefinition[] Columns {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


