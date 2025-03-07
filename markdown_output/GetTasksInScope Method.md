Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTasksInScope Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) : GetTasksInScope Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_scope_
    

Glossary Item Box

Gets all scoped tasks in the given scope. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTasksInScope( _
       ByVal _scope_ As String _
    ) As IEnumerable(Of ReleasedComponentTask)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim scope As String
    Dim value As IEnumerable(Of ReleasedComponentTask)
     
    value = instance.GetTasksInScope(scope)  
  
C#|   
---|---  
      
    
    public IEnumerable<ReleasedComponentTask> GetTasksInScope( 
       string _scope_
    )  
  
#### Parameters

 _scope_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)


