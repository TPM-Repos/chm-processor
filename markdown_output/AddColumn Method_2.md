![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddColumn Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5423.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : AddColumn Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the column.

_type_
    The data type for this column.

_columnType_
    The type of column - Common, Control or Not Specified.

Glossary Item Box

Adds a column that is present in the target table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddColumn( _
       ByVal _name_ As String, _
       ByVal _type_ As String, _
       ByVal _columnType_ As [ColumnType](topic2346.md) _
    ) As DataExportColumnDefinition  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
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
    The type of column - Common, Control or Not Specified.

#### Return Value

The column definition.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)

©2024 DriveWorks Ltd. All Rights Reserved.
