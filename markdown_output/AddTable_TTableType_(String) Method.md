_TTableType_
    The type of table to create.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddTable<TTableType>(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTables Class](topic3136.md) > [AddTable Method](topic3142.md) : AddTable<TTableType>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give the new table.

Glossary Item Box

Adds a table of the specified type to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddTable(Of TTableType As [GroupDataTable](topic3110.md))( _
       ByVal _name_ As String _
    ) As TTableType  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTables](topic3136.md)
    Dim name As String
    Dim value As TTableType
     
    value = instance.AddTable(Of TTableType)(name)  
  
C#|   
---|---  
      
    
    public TTableType AddTable<TTableType>( 
       string _name_
    )
    where TTableType: [GroupDataTable](topic3110.md)  
  
#### Parameters

 _name_
    The name to give the new table.

#### Type Parameters

_TTableType_
    The type of table to create.

#### Return Value

The created table.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupDataTables Class](topic3136.md)   
[GroupDataTables Members](topic3137.md)   
[Overload List](topic3142.md)


