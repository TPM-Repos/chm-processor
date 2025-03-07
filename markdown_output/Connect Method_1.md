Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Connect Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : Connect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serverName_
    The name of the server to which to connect.

Glossary Item Box

Connects to the specified remote group server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function Connect( _
       ByVal _serverName_ As String _
    ) As [RemoteGroupManager](topic5174.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim serverName As String
    Dim value As [RemoteGroupManager](topic5174.md)
     
    value = [RemoteGroupManager](topic5174.md).Connect(serverName)  
  
C#|   
---|---  
      
    
    public static [RemoteGroupManager](topic5174.md) Connect( 
       string _serverName_
    )  
  
#### Parameters

 _serverName_
    The name of the server to which to connect.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


