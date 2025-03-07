Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddColumn Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [OdbcExport Class](topic3763.md) : AddColumn Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the column.

_type_
    The data type for this column.

_columnType_
    The type of column; Control, Common or NotSpecified.

Glossary Item Box

Adds a column that is present in the target table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddColumn( _
       ByVal _name_ As String, _
       ByVal _type_ As String, _
       ByVal _columnType_ As [ColumnType](topic2346.md) _
    ) As DataExportColumnDefinition  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcExport](topic3763.md)
    Dim name As String
    Dim type As String
    Dim columnType As [ColumnType](topic2346.md)
    Dim value As DataExportColumnDefinition
     
    value = instance.AddColumn(name, type, columnType)  
  
C#|   
---|---  
      
    
    public DataExportColumnDefinition AddColumn( 
       string _name_ ,
       string _type_ ,
       [ColumnType](topic2346.md) _columnType_
    )  
  
#### Parameters

 _name_
    The name of the column.
_type_
    The data type for this column.
_columnType_
    The type of column; Control, Common or NotSpecified.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcExport Class](topic3763.md)   
[OdbcExport Members](topic3764.md)


