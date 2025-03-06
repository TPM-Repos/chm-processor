       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTables Class](topic4000.md) : TryGetTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name (or display name) of the table to get.

_table_
    The instance of the found table, or null if nothing is found.

Glossary Item Box

Attempts to get a table with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetTable( _
       ByVal _name_ As String, _
       ByRef _table_ As [ProjectCalculationTable](topic3926.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTables](topic4000.md)
    Dim name As String
    Dim table As [ProjectCalculationTable](topic3926.md)
    Dim value As Boolean
     
    value = instance.TryGetTable(name, table)  
  
C#|   
---|---  
      
    
    public bool TryGetTable( 
       string _name_ ,
       ref [ProjectCalculationTable](topic3926.md) _table_
    )  
  
#### Parameters

 _name_
    The name (or display name) of the table to get.
_table_
    The instance of the found table, or null if nothing is found.

#### Return Value

True if an instance is found.

# Remarks

This is not case sensitive.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTables Class](topic4000.md)   
[ProjectCalculationTables Members](topic4001.md)


