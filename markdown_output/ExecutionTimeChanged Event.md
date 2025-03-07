Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecutionTimeChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : ExecutionTimeChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs whenever the [ExecutionTime](topic6957.md) property's value has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ExecutionTimeChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.ExecutionTimeChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> ExecutionTimeChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


