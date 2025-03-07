Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryDataValues(String,String,String,String,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) > [QueryDataValues Method](topic2568.md) : QueryDataValues(String,String,String,String,Boolean) Method  
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

_includeHeaders_
    A flag to indicate whether column headers should be included in the result.

Glossary Item Box

Performs a DriveWorks QueryData operation given an arbitrary SQL statement. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function QueryDataValues( _
       ByVal _dsn_ As String, _
       ByVal _sql_ As String, _
       ByVal _username_ As String, _
       ByVal _password_ As String, _
       ByVal _includeHeaders_ As Boolean _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim dsn As String
    Dim sql As String
    Dim username As String
    Dim password As String
    Dim includeHeaders As Boolean
    Dim value As Object
     
    value = instance.QueryDataValues(dsn, sql, username, password, includeHeaders)  
  
C#|   
---|---  
      
    
    public object QueryDataValues( 
       string _dsn_ ,
       string _sql_ ,
       string _username_ ,
       string _password_ ,
       bool _includeHeaders_
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
_includeHeaders_
    A flag to indicate whether column headers should be included in the result.

#### Return Value

The requested data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)   
[Overload List](topic2568.md)


