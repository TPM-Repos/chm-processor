       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTable(String,GroupDataTable) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTables Class](topic3136.md) > [TryGetTable Method](topic3145.md) : TryGetTable(String,GroupDataTable) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to find.

_table_
    Reference to set to the found table, if it's found.

Glossary Item Box

Attempts to find a table with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetTable( _
       ByVal _tableName_ As String, _
       ByRef _table_ As [GroupDataTable](topic3110.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTables](topic3136.md)
    Dim tableName As String
    Dim table As [GroupDataTable](topic3110.md)
    Dim value As Boolean
     
    value = instance.TryGetTable(tableName, table)  
  
C#|   
---|---  
      
    
    public bool TryGetTable( 
       string _tableName_ ,
       ref [GroupDataTable](topic3110.md) _table_
    )  
  
#### Parameters

 _tableName_
    The name of the table to find.
_table_
    Reference to set to the found table, if it's found.

#### Return Value

True if the table was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupDataTables Class](topic3136.md)   
[GroupDataTables Members](topic3137.md)   
[Overload List](topic3145.md)


