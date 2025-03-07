Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommonColumns Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : CommonColumns Property  
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
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim value() As DataExportColumnDefinition
     
    value = instance.CommonColumns  
  
C#|   
---|---  
      
    
    public DataExportColumnDefinition[] CommonColumns {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)


