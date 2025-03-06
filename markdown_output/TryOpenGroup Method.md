       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryOpenGroup Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) : TryOpenGroup Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_groupConnectionString_
    The connection string which describes the group to which to connect.

_groupCredentials_
    The credentials to use to connect to the group, or a null reference to prompt the user for credentials if the implementation supports it.

Glossary Item Box

Tries to open the specified group with the given credentials. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryOpenGroup( _
       ByVal _groupConnectionString_ As String, _
       ByVal _groupCredentials_ As [IProviderCredentials](topic10588.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim groupConnectionString As String
    Dim groupCredentials As [IProviderCredentials](topic10588.md)
    Dim value As Boolean
     
    value = instance.TryOpenGroup(groupConnectionString, groupCredentials)  
  
C#|   
---|---  
      
    
    bool TryOpenGroup( 
       string _groupConnectionString_ ,
       [IProviderCredentials](topic10588.md) _groupCredentials_
    )  
  
#### Parameters

 _groupConnectionString_
    The connection string which describes the group to which to connect.
_groupCredentials_
    The credentials to use to connect to the group, or a null reference to prompt the user for credentials if the implementation supports it.

#### Return Value

True if the group was successfully opened, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)


