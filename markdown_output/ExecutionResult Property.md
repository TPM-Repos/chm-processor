Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecutionResult Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTask Class](topic13678.md) : ExecutionResult Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the execution result of the task (Default is [TaskExecutionResult.Success](topic13454.md)). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ExecutionResult As [TaskExecutionResult](topic13454.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationTask](topic13678.md)
    Dim value As [TaskExecutionResult](topic13454.md)
     
    instance.ExecutionResult = value
     
    value = instance.ExecutionResult  
  
C#|   
---|---  
      
    
    public [TaskExecutionResult](topic13454.md) ExecutionResult {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationTask Class](topic13678.md)   
[GenerationTask Members](topic13679.md)


