Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectCapturedComponentIds Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentManager Class](topic4094.md) : GetProjectCapturedComponentIds Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a collection of captured component Ids, as specified in the project file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectCapturedComponentIds() As IEnumerable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentManager](topic4094.md)
    Dim value As IEnumerable(Of Guid)
     
    value = instance.GetProjectCapturedComponentIds()  
  
C#|   
---|---  
      
    
    public IEnumerable<Guid> GetProjectCapturedComponentIds()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentManager Class](topic4094.md)   
[ProjectComponentManager Members](topic4095.md)


