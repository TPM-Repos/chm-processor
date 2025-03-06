RenameColumn Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) : RenameColumn Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    The name of the column to rename.

_newName_
    The new name to give the column.

Glossary Item Box

Renames a column. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RenameColumn( _
       ByVal _columnName_ As String, _
       ByVal _newName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim columnName As String
    Dim newName As String
     
    instance.RenameColumn(columnName, newName)  
  
C#|   
---|---  
      
    
    public void RenameColumn( 
       string _columnName_ ,
       string _newName_
    )  
  
#### Parameters

 _columnName_
    The name of the column to rename.
_newName_
    The new name to give the column.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)


