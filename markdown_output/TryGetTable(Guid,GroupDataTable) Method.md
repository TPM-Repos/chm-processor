       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTable(Guid,GroupDataTable) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3147.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTables Class](topic3136.md) > [TryGetTable Method](topic3145.md) : TryGetTable(Guid,GroupDataTable) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The Id of the table to find.

_table_
    The retrieved group table if found, otherwise null.

Glossary Item Box

Tries to find a table with the specified Id. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetTable( _
       ByVal _id_ As Guid, _
       ByRef _table_ As [GroupDataTable](topic3110.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTables](topic3136.md)
    Dim id As Guid
    Dim table As [GroupDataTable](topic3110.md)
    Dim value As Boolean
     
    value = instance.TryGetTable(id, table)  
  
C#|   
---|---  
      
    
    public bool TryGetTable( 
       Guid _id_ ,
       ref [GroupDataTable](topic3110.md) _table_
    )  
  
#### Parameters

 _id_
    The Id of the table to find.
_table_
    The retrieved group table if found, otherwise null.

#### Return Value

True if a matching table was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupDataTables Class](topic3136.md)   
[GroupDataTables Members](topic3137.md)   
[Overload List](topic3145.md)

©2024 DriveWorks Ltd. All Rights Reserved.
