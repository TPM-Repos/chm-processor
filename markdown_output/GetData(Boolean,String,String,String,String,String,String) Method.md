![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetData(Boolean,String,String,String,String,String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2563.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) > [GetData Method](topic2561.md) : GetData(Boolean,String,String,String,String,String,String) Method  
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

_tableName_
    The table from which to get data.

_fieldName_
    The name of the field from which results should be retrieved.

_whereClause_
    The where clause used to filter the results.

Glossary Item Box

Performs a DriveWorks GetData operation given a table, result field, and where clause. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetData( _
       ByVal _isArray_ As Boolean, _
       ByVal _dsn_ As String, _
       ByVal _userName_ As String, _
       ByVal _password_ As String, _
       ByVal _tableName_ As String, _
       ByVal _fieldName_ As String, _
       ByVal _whereClause_ As String _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim isArray As Boolean
    Dim dsn As String
    Dim userName As String
    Dim password As String
    Dim tableName As String
    Dim fieldName As String
    Dim whereClause As String
    Dim value As String
     
    value = instance.GetData(isArray, dsn, userName, password, tableName, fieldName, whereClause)  
  
C#|   
---|---  
      
    
    public string GetData( 
       bool _isArray_ ,
       string _dsn_ ,
       string _userName_ ,
       string _password_ ,
       string _tableName_ ,
       string _fieldName_ ,
       string _whereClause_
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
_tableName_
    The table from which to get data.
_fieldName_
    The name of the field from which results should be retrieved.
_whereClause_
    The where clause used to filter the results.

#### Return Value

The requested data.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)   
[Overload List](topic2561.md)

©2024 DriveWorks Ltd. All Rights Reserved.
