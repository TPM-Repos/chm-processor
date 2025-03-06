TryGet Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTableColumns Class](topic3968.md) : TryGet Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    Name of the column to find.

_column_
    The resulting column or null.

Glossary Item Box

Attempts to find a matching column based on the name specified. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGet( _
       ByVal _columnName_ As String, _
       ByRef _column_ As [ProjectCalculationTableColumn](topic3946.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTableColumns](topic3968.md)
    Dim columnName As String
    Dim column As [ProjectCalculationTableColumn](topic3946.md)
    Dim value As Boolean
     
    value = instance.TryGet(columnName, column)  
  
C#|   
---|---  
      
    
    public bool TryGet( 
       string _columnName_ ,
       ref [ProjectCalculationTableColumn](topic3946.md) _column_
    )  
  
#### Parameters

 _columnName_
    Name of the column to find.
_column_
    The resulting column or null.

#### Return Value

True if the column is found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTableColumns Class](topic3968.md)   
[ProjectCalculationTableColumns Members](topic3969.md)


