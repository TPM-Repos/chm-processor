Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetOdbcConnection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : GetOdbcConnection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_databaseName_
    The DSN name to which to connect.

_userName_
    The username to use for the connection.

_password_
    The password to use for the connection.

Glossary Item Box

Gets an ODBC connection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetOdbcConnection( _
       ByVal _databaseName_ As String, _
       ByVal _userName_ As String, _
       ByVal _password_ As String _
    ) As OdbcConnection  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim databaseName As String
    Dim userName As String
    Dim password As String
    Dim value As OdbcConnection
     
    value = instance.GetOdbcConnection(databaseName, userName, password)  
  
C#|   
---|---  
      
    
    public OdbcConnection GetOdbcConnection( 
       string _databaseName_ ,
       string _userName_ ,
       string _password_
    )  
  
#### Parameters

 _databaseName_
    The DSN name to which to connect.
_userName_
    The username to use for the connection.
_password_
    The password to use for the connection.

#### Return Value

An instance of the System.Data.Odbc.OdbcConnection class representing an open connection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


