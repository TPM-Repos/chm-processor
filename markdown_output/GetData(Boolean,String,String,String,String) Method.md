Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetData(Boolean,String,String,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) > [GetData Method](topic2561.md) : GetData(Boolean,String,String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isArray_
    True if the result is going to be used in an array rule, and therefore should be delimited by | characters, false if a single value is expected.

_dsn_
    The data source name which identifies the ODBC connection to connect to.

_userName_
    The username to use for the connection.

_password_
    The password to use for the connection.

_sql_
    The SQL string to execute against the connection.

Glossary Item Box

Performs a DriveWorks GetData operation given an arbitrary SQL statement. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetData( _
       ByVal _isArray_ As Boolean, _
       ByVal _dsn_ As String, _
       ByVal _userName_ As String, _
       ByVal _password_ As String, _
       ByVal _sql_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim isArray As Boolean
    Dim dsn As String
    Dim userName As String
    Dim password As String
    Dim sql As String
    Dim value As String
     
    value = instance.GetData(isArray, dsn, userName, password, sql)  
  
C#|   
---|---  
      
    
    public string GetData( 
       bool _isArray_ ,
       string _dsn_ ,
       string _userName_ ,
       string _password_ ,
       string _sql_
    )  
  
#### Parameters

 _isArray_
    True if the result is going to be used in an array rule, and therefore should be delimited by | characters, false if a single value is expected.
_dsn_
    The data source name which identifies the ODBC connection to connect to.
_userName_
    The username to use for the connection.
_password_
    The password to use for the connection.
_sql_
    The SQL string to execute against the connection.

#### Return Value

The requested data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)   
[Overload List](topic2561.md)


