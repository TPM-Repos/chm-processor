       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Rename Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTables Class](topic4000.md) : Rename Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to change the name of.

_newTableName_
    The new name to give the table.

Glossary Item Box

Renames a table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Rename( _
       ByVal _tableName_ As String, _
       ByVal _newTableName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectCalculationTables](topic4000.md)
    Dim tableName As String
    Dim newTableName As String
     
    instance.Rename(tableName, newTableName)  
  
C#|   
---|---  
      
    
    public void Rename( 
       string _tableName_ ,
       string _newTableName_
    )  
  
#### Parameters

 _tableName_
    The name of the table to change the name of.
_newTableName_
    The new name to give the table.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTables Class](topic4000.md)   
[ProjectCalculationTables Members](topic4001.md)


