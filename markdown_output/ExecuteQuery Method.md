Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecuteQuery Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [DataGrid Class](topic7838.md) : ExecuteQuery Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connectionCache_
    An optional cache of open connections, represented by a writable dictionary keyed on connection string.

Glossary Item Box

Executes the query represented by the data grid, and returns the result as a data table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ExecuteQuery( _
       ByVal _connectionCache_ As IDictionary(Of String,OdbcConnection) _
    ) As DataTable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DataGrid](topic7838.md)
    Dim connectionCache As IDictionary(Of String,OdbcConnection)
    Dim value As DataTable
     
    value = instance.ExecuteQuery(connectionCache)  
  
C#|   
---|---  
      
    
    public DataTable ExecuteQuery( 
       IDictionary<string,OdbcConnection> _connectionCache_
    )  
  
#### Parameters

 _connectionCache_
    An optional cache of open connections, represented by a writable dictionary keyed on connection string.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DataGrid Class](topic7838.md)   
[DataGrid Members](topic7839.md)


