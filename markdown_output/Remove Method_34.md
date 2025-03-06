Remove Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRows Class](topic5612.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_row_
    The row to remove.

Glossary Item Box

Removes the specified row from this collection of rows. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _row_ As [TableExportRow](topic5600.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TableExportRows](topic5612.md)
    Dim row As [TableExportRow](topic5600.md)
    Dim value As Boolean
     
    value = instance.Remove(row)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [TableExportRow](topic5600.md) _row_
    )  
  
#### Parameters

 _row_
    The row to remove.

#### Return Value

True if the row was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TableExportRows Class](topic5612.md)   
[TableExportRows Members](topic5613.md)


