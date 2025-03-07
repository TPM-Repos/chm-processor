Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetGroupDetails Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupManager Class](topic5174.md) : GetGroupDetails Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all the groups on the server and their details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetGroupDetails() As IEnumerable(Of SharedGroupDetails)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupManager](topic5174.md)
    Dim value As IEnumerable(Of SharedGroupDetails)
     
    value = instance.GetGroupDetails()  
  
C#|   
---|---  
      
    
    public IEnumerable<SharedGroupDetails> GetGroupDetails()  
  
# Remarks

This returns all groups - even the ones that this server is not hosting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupManager Class](topic5174.md)   
[RemoteGroupManager Members](topic5175.md)


