Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConnectedClients Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : GetConnectedClients Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets details of all current connections to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConnectedClients() As IEnumerable(Of ConnectedClientDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim value As IEnumerable(Of ConnectedClientDetails)
     
    value = instance.GetConnectedClients()  
  
C#|   
---|---  
      
    
    public IEnumerable<ConnectedClientDetails> GetConnectedClients()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


