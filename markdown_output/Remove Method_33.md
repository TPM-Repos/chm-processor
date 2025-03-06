Remove Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRow Class](topic5600.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_cell_
    The cell to remove from this row.

Glossary Item Box

Removes the specified cell from this row. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _cell_ As [TableExportCell](topic5560.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportRow](topic5600.md)
    Dim cell As [TableExportCell](topic5560.md)
    Dim value As Boolean
     
    value = instance.Remove(cell)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [TableExportCell](topic5560.md) _cell_
    )  
  
#### Parameters

 _cell_
    The cell to remove from this row.

#### Return Value

True if the cell was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportRow Class](topic5600.md)   
[TableExportRow Members](topic5601.md)


