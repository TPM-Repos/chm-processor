Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : QueryData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dsn_
    The data source name which identifies the ODBC or SQL connection to connect to.

_sql_
    The SQL string to execute against the connection.

_username_
    The username to use for the connection.

_password_
    The password to use for the connection.

Glossary Item Box

Performs a DriveWorks QueryData operation given an arbitrary SQL statement. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function QueryData( _
       ByVal _dsn_ As String, _
       ByVal _sql_ As String, _
       ByVal _username_ As String, _
       ByVal _password_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim dsn As String
    Dim sql As String
    Dim username As String
    Dim password As String
    Dim value As String
     
    value = instance.QueryData(dsn, sql, username, password)  
  
C#|   
---|---  
      
    
    public string QueryData( 
       string _dsn_ ,
       string _sql_ ,
       string _username_ ,
       string _password_
    )  
  
#### Parameters

 _dsn_
    The data source name which identifies the ODBC or SQL connection to connect to.
_sql_
    The SQL string to execute against the connection.
_username_
    The username to use for the connection.
_password_
    The password to use for the connection.

#### Return Value

The requested data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


