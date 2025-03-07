Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DbExecute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : DbExecute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dsn_
    The connection string or ODBC DSN to which to connect.

_sql_
    The SQL command to execute.

_username_
    Optionally, the user name to use to connect.

_password_
    Optionally, the user password to use to connect.

_preview_
    Indicates whether the result should be committed or not.

Glossary Item Box

Executes a query against a database. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DbExecute( _
       ByVal _dsn_ As String, _
       ByVal _sql_ As String, _
       ByVal _username_ As String, _
       ByVal _password_ As String, _
       ByVal _preview_ As Boolean _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim dsn As String
    Dim sql As String
    Dim username As String
    Dim password As String
    Dim preview As Boolean
    Dim value As Object
     
    value = instance.DbExecute(dsn, sql, username, password, preview)  
  
C#|   
---|---  
      
    
    public object DbExecute( 
       string _dsn_ ,
       string _sql_ ,
       string _username_ ,
       string _password_ ,
       bool _preview_
    )  
  
#### Parameters

 _dsn_
    The connection string or ODBC DSN to which to connect.
_sql_
    The SQL command to execute.
_username_
    Optionally, the user name to use to connect.
_password_
    Optionally, the user password to use to connect.
_preview_
    Indicates whether the result should be committed or not.

#### Return Value

A number indicating how many records were affected, or a string containing the error message if something went wrong.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


