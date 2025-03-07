Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConnectedClients Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : GetConnectedClients Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all clients connected to this server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConnectedClients() As IEnumerable(Of ConnectedClientDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim value As IEnumerable(Of ConnectedClientDetails)
     
    value = instance.GetConnectedClients()  
  
C#|   
---|---  
      
    
    public IEnumerable<ConnectedClientDetails> GetConnectedClients()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


