Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Cell Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRow Class](topic5600.md) : Cell Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_header_
    The column header for the cell to fetch.

Glossary Item Box

Gets a cell with the specified header from this row. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Cell( _
       ByVal _header_ As String _
    ) As [TableExportCell](topic5560.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportRow](topic5600.md)
    Dim header As String
    Dim value As [TableExportCell](topic5560.md)
     
    value = instance.Cell(header)  
  
C#|   
---|---  
      
    
    public [TableExportCell](topic5560.md) this[ 
       string _header_
    ]; {get;}  
  
#### Parameters

 _header_
    The column header for the cell to fetch.

# Remarks

If a cell by the specified header does not exist, it will be created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportRow Class](topic5600.md)   
[TableExportRow Members](topic5601.md)


