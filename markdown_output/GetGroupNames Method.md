Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGroupNames Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : GetGroupNames Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all the groups on the server that are available to connect to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGroupNames() As IEnumerable(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim value As IEnumerable(Of String)
     
    value = instance.GetGroupNames()  
  
C#|   
---|---  
      
    
    public IEnumerable<string> GetGroupNames()  
  
# Remarks

Some group names will not be returned, if they are not being hosted by this server.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


