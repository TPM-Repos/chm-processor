       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTable Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4326.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTables Class](topic4311.md) : TryGetTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the table to retrieve.

_table_
    A reference to a variable which will receive the table.

Glossary Item Box

Tries to get a table with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetTable( _
       ByVal _name_ As String, _
       ByRef _table_ As [ProjectDataTable](topic4282.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTables](topic4311.md)
    Dim name As String
    Dim table As [ProjectDataTable](topic4282.md)
    Dim value As Boolean
     
    value = instance.TryGetTable(name, table)  
  
C#|   
---|---  
      
    
    public bool TryGetTable( 
       string _name_ ,
       ref [ProjectDataTable](topic4282.md) _table_
    )  
  
#### Parameters

 _name_
    The name of the table to retrieve.
_table_
    A reference to a variable which will receive the table.

#### Return Value

True if the table was found and returned, otherwise false.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| Thrown if the name argument is a null reference.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTables Class](topic4311.md)   
[ProjectDataTables Members](topic4312.md)

©2024 DriveWorks Ltd. All Rights Reserved.
