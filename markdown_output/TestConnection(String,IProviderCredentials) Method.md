TestConnection(String,IProviderCredentials) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) > [TestConnection Method](topic258.md) : TestConnection(String,IProviderCredentials) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connectionString_
    The connection string for the group.

_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.

Glossary Item Box

Tests the connection to the specified group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function TestConnection( _
       ByVal _connectionString_ As String, _
       ByVal _groupCredentials_ As [IProviderCredentials](topic10588.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim connectionString As String
    Dim groupCredentials As [IProviderCredentials](topic10588.md)
    Dim value As Boolean
     
    value = instance.TestConnection(connectionString, groupCredentials)  
  
C#|   
---|---  
      
    
    bool TestConnection( 
       string _connectionString_ ,
       [IProviderCredentials](topic10588.md) _groupCredentials_
    )  
  
#### Parameters

 _connectionString_
    The connection string for the group.
_groupCredentials_
    The credentials to use to connect to the group, or a null rereference to prompt the user for credentials if the implementation supports it.

#### Return Value

True if the connection was successful, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)   
[Overload List](topic258.md)


