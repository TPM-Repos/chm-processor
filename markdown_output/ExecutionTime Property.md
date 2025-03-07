Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecutionTime Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : ExecutionTime Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the amount of time it took for this node to execute. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ExecutionTime As TimeSpan  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim value As TimeSpan
     
    value = instance.ExecutionTime  
  
C#|   
---|---  
      
    
    public TimeSpan ExecutionTime {get;}  
  
#### Property Value

The time it took for this node to execute, or an empty TimeSpan if it hasn't executed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


