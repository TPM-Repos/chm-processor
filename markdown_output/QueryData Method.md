![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryData Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2567.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function QueryData( _
       ByVal _dsn_ As String, _
       ByVal _sql_ As String, _
       ByVal _username_ As String, _
       ByVal _password_ As String _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)

©2024 DriveWorks Ltd. All Rights Reserved.
