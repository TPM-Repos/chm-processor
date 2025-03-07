Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddRow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : AddRow Method  
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
      
    
    Function AddRow( _
       ByVal _fields_ As IDictionary(Of String,IHasRule) _
    ) As [DataExportRowDefinition](topic2635.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim fields As IDictionary(Of String,IHasRule)
    Dim value As [DataExportRowDefinition](topic2635.md)
     
    value = instance.AddRow(fields)  
  
C#|   
---|---  
      
    
    [DataExportRowDefinition](topic2635.md) AddRow( 
       IDictionary<string,IHasRule> _fields_
    )  
  
#### Parameters

 _fields_
    The dictionary of fields that are specified on this row. Key is the field name and the value is the rule for the cell.

#### Return Value

Returns the added row.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


