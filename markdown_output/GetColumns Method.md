Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetColumns Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IExportableTable Interface](topic2199.md) : GetColumns Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns a collection of column names for this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetColumns() As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IExportableTable](topic2199.md)
    Dim value() As String
     
    value = instance.GetColumns()  
  
C#|   
---|---  
      
    
    string[] GetColumns()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IExportableTable Interface](topic2199.md)   
[IExportableTable Members](topic2200.md)


