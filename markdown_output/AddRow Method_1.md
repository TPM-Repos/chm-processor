Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddRow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : AddRow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fields_
    The dictionary of fields that are specified on this row. Key is the field name and the value is the rule for the cell.

Glossary Item Box

Adds a row to the list of export rows. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddRow( _
       ByVal _fields_ As IDictionary(Of String,IHasRule) _
    ) As [DataExportRowDefinition](topic2635.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim fields As IDictionary(Of String,IHasRule)
    Dim value As [DataExportRowDefinition](topic2635.md)
     
    value = instance.AddRow(fields)  
  
C#|   
---|---  
      
    
    public [DataExportRowDefinition](topic2635.md) AddRow( 
       IDictionary<string,IHasRule> _fields_
    )  
  
#### Parameters

 _fields_
    The dictionary of fields that are specified on this row. Key is the field name and the value is the rule for the cell.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


