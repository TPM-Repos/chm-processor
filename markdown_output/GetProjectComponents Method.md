Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectComponents Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupOptionsEnvironment Class](topic9759.md) : GetProjectComponents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all components in the source group along with any project specific information and hierarchies. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectComponents() As Task(Of IEnumerable(Of ComponentItemModel))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupOptionsEnvironment](topic9759.md)
    Dim value As Task(Of IEnumerable(Of ComponentItemModel))
     
    value = instance.GetProjectComponents()  
  
C#|   
---|---  
      
    
    public Task<IEnumerable<ComponentItemModel>> GetProjectComponents()  
  
#### Return Value

A Task that when awaited will return a collection of project component information.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupOptionsEnvironment Class](topic9759.md)   
[CopyGroupOptionsEnvironment Members](topic9760.md)


