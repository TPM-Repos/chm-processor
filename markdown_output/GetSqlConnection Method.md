![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSqlConnection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2566.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetSqlConnection( _
       ByVal _connectionString_ As String, _
       ByVal _userName_ As String, _
       ByVal _password_ As String _
    ) As SqlConnection  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)

©2024 DriveWorks Ltd. All Rights Reserved.
