Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSqlConnection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : GetSqlConnection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connectionString_
    The connection string to use for connection.

_userName_
    The username to use for the connection.

_password_
    The password to use for the connection.

Glossary Item Box

Gets a SQL connection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSqlConnection( _
       ByVal _connectionString_ As String, _
       ByVal _userName_ As String, _
       ByVal _password_ As String _
    ) As SqlConnection  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim connectionString As String
    Dim userName As String
    Dim password As String
    Dim value As SqlConnection
     
    value = instance.GetSqlConnection(connectionString, userName, password)  
  
C#|   
---|---  
      
    
    public SqlConnection GetSqlConnection( 
       string _connectionString_ ,
       string _userName_ ,
       string _password_
    )  
  
#### Parameters

 _connectionString_
    The connection string to use for connection.
_userName_
    The username to use for the connection.
_password_
    The password to use for the connection.

#### Return Value

An instance of the System.Data.SqlClient.SqlConnection class representing an open connection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


