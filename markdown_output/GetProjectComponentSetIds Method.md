Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectComponentSetIds Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentManager Class](topic4094.md) : GetProjectComponentSetIds Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of all captured component sets within the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectComponentSetIds() As IEnumerable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentManager](topic4094.md)
    Dim value As IEnumerable(Of Guid)
     
    value = instance.GetProjectComponentSetIds()  
  
C#|   
---|---  
      
    
    public IEnumerable<Guid> GetProjectComponentSetIds()  
  
#### Return Value

A collection of component set GUIDs.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentManager Class](topic4094.md)   
[ProjectComponentManager Members](topic4095.md)


