       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetCell Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5610.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRow Class](topic5600.md) : TryGetCell Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_header_
    The header of the column to get the corresponding cell for.

_cell_
    The reference to set the cell to if found.

Glossary Item Box

Attempts to get the cell for the specified header. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetCell( _
       ByVal _header_ As String, _
       ByRef _cell_ As [TableExportCell](topic5560.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportRow](topic5600.md)
    Dim header As String
    Dim cell As [TableExportCell](topic5560.md)
    Dim value As Boolean
     
    value = instance.TryGetCell(header, cell)  
  
C#|   
---|---  
      
    
    public bool TryGetCell( 
       string _header_ ,
       ref [TableExportCell](topic5560.md) _cell_
    )  
  
#### Parameters

 _header_
    The header of the column to get the corresponding cell for.
_cell_
    The reference to set the cell to if found.

#### Return Value

True if the cell was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportRow Class](topic5600.md)   
[TableExportRow Members](topic5601.md)

©2024 DriveWorks Ltd. All Rights Reserved.
