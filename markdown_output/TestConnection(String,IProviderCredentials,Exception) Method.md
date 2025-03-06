![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TestConnection(String,IProviderCredentials,Exception) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic260.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) > [TestConnection Method](topic258.md) : TestConnection(String,IProviderCredentials,Exception) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connectionString_
    The connection string for the group.

_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.

_exception_
    The exception that was thrown whilst attempting the connection.

Glossary Item Box

Tests the connection to the specified group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function TestConnection( _
       ByVal _connectionString_ As String, _
       ByVal _groupCredentials_ As [IProviderCredentials](topic10588.md), _
       ByRef _exception_ As Exception _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim connectionString As String
    Dim groupCredentials As [IProviderCredentials](topic10588.md)
    Dim exception As Exception
    Dim value As Boolean
     
    value = instance.TestConnection(connectionString, groupCredentials, exception)  
  
C#|   
---|---  
      
    
    bool TestConnection( 
       string _connectionString_ ,
       [IProviderCredentials](topic10588.md) _groupCredentials_ ,
       ref Exception _exception_
    )  
  
#### Parameters

 _connectionString_
    The connection string for the group.
_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.
_exception_
    The exception that was thrown whilst attempting the connection.

#### Return Value

True if the connection was successful, otherwise False.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)   
[Overload List](topic258.md)

©2024 DriveWorks Ltd. All Rights Reserved.
