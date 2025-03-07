Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AllowIgnoreTaskList Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationEnvironment Class](topic11355.md) : AllowIgnoreTaskList Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the user is allowed to ignore the state of the task list when navigating and invoking transitions. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property AllowIgnoreTaskList As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationEnvironment](topic11355.md)
    Dim value As Boolean
     
    instance.AllowIgnoreTaskList = value
     
    value = instance.AllowIgnoreTaskList  
  
C#|   
---|---  
      
    
    public bool AllowIgnoreTaskList {get; set;}  
  
# Remarks

The principle consumer of this feature is the specification test feature in which the user is allowed to navigate even if they have not resolved all the tasks in the task list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationEnvironment Class](topic11355.md)   
[SpecificationEnvironment Members](topic11356.md)


